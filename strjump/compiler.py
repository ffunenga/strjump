#!/usr/bin/env python3


from . import elements


def process(lst):
    types = [elements.Identifier, elements.Reference, str]
    for i, s in enumerate(lst):
        assert type(s) in types, "type of lst[%d] is unknown (%s)" % (i, type(s))
    identifiers = [i.identifier for i in lst if type(i) == elements.Identifier]
    references = [r for r in lst if type(r) == elements.Reference]
    assert all(r.identifier in identifiers for r in references), "reference unknown"

    identifiers = []
    __pre_refs = [0] * len(references)
    __next_idx = 0
    __pre_lenstatic = 0
    for idx, i in enumerate(lst):
        if type(i) == elements.Identifier:
            identifier = lst[idx]
            identifier.set_preceding(__pre_lenstatic, __pre_refs[:])
            identifiers.append(identifier)
            __ini_len = len(str(__pre_lenstatic + 1))
            for r in references:
                if r.identifier == identifier.identifier:
                    r.length = __ini_len
            __pre_lenstatic += len(i)
        elif type(i) == elements.Reference:
            __pre_refs[__next_idx] = 1
            __next_idx += 1
        elif type(i) == str:
            __pre_lenstatic += len(i)

    __idx = 0
    __previous = -1
    __current = 0
    __onemore = False
    while True:
        identifier = identifiers[__idx]
        x = identifier.calc_x(r.length for r in references)
        __current += x
        x = str(x)
        [r.set(x) for r in references if r.identifier == identifier.identifier]
        if __onemore:
            break
        if __previous == __current:
            __onemore = True
        __idx = (__idx + 1) % len(identifiers)
        if __idx == 0:
            __previous = __current
            __current = 0

    return ''.join(str(i) for i in lst)



