#!/usr/bin/env python3


from . import elements


def loopattempts(min_lens):
    array = [v for k, v in min_lens]
    n = len(array)
    while True:
        yield [(k, v) for (k, _), v in zip(min_lens, array)]
        for idx in range(n):
            if idx != (n - 1):
                if array[idx] < array[idx + 1]:
                    array[idx] += 1
                    break
            else:
                array[idx] += 1


def calc_equation(static_len, preceding_refs, ref_lens):
    preceding_refs = [r.identifier for r in preceding_refs]
    return static_len + sum(v for r, v in ref_lens if r.identifier in preceding_refs)


def validate(attempt, result):
    reference, index = result
    length = len(str(index))
    return any((ref == reference and length == val) for ref, val in attempt)


def process(lst):
    identifiers = [s.identifier for s in lst if type(s) == elements.Identifier]
    references = [s.identifier for s in lst if type(s) == elements.Reference]
    assert all(r in identifiers for r in references), "reference unknown"
    for idx, i in enumerate(lst):
        if type(i) == elements.Identifier and i.identifier not in references:
            lst[idx] = i.content

    min_lens = []
    equations = []
    for idx in [i for i, s in enumerate(lst) if type(s) == elements.Identifier]:
        reference = lst[idx].reference()
        preceding = lst[:idx]
        static_len = sum(len(s) for s in preceding)
        min_len = len(str(static_len))
        preceding_refs = [s for s in preceding if type(s) == elements.Reference]
        if 0:
            print("element:", lst[idx])
            print("preceding:", preceding)
            print("static_len:", static_len)
            print("min_len:", min_len)
            print("preceding_refs:", preceding_refs)
            print("---")
        min_lens.append((reference, min_len))
        equations.append((reference, static_len, preceding_refs))

    print("min_lens:", min_lens)
    for attempt in loopattempts(min_lens):
        flag = True
        rsts = []
        for reference, static_len, preceding_refs in equations:
            rst = calc_equation(static_len, preceding_refs, attempt)
            flag = validate(attempt, (reference, rst))
            if not flag:
                break
            rsts.append(rst)
        if flag:
            router = {r.identifier: str(i) for (r, l), i in zip(attempt, rsts)}
            rst = ""
            for l in lst:
                if type(l) == elements.Reference:
                    rst += router[l.identifier]
                elif type(l) == elements.Identifier:
                    rst += l.flat()
                else:
                    rst += l
            return rst
        assert 1, "solution not found"
