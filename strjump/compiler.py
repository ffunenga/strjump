#!/usr/bin/env python3


import itertools

from . import elements


def xmax_A(A, R):
    p = [((10 ** ri) - 1) for ri in R]
    return [(pi - ai) for pi, ai in zip(p, A)]


def A_xmin(A, R):
    p = [(10 ** (ri - 1)) for ri in R]
    return [(ai - pi) for ai, pi in zip(A, p)]


def coefs(S, Cr, R):
    A = [sum((cij * ri) for cij, ri in zip(ci, R)) for ci in Cr]
    A = [(si + p0i) for si, p0i in zip(S, A)]
    return [(u * l) for u, l in zip(xmax_A(A, R), A_xmin(A, R))]


def validate(c_array):
    return all((ci >= 0) for ci in c_array)


def iterR(n):
    array = [1] * n
    idx = n - 1
    while True:
        yield array[::-1]
        if idx == n - 1 and array[idx] == array[idx - 1]:
            while idx > 0 and array[idx] == array[idx - 1]:
                idx -= 1
            array[idx] += 1
            for j in range(idx + 1, n):
                array[j] = 1
        else:
            idx = min(idx + 1, n - 1)
            array[idx] += 1


def process(lst):
    types = [elements.Identifier, elements.Reference, str]
    for i, s in enumerate(lst):
        assert type(s) in types, "type of lst[%d] is unknown (%s)" % (i, type(s))
    identifiers = [i.identifier for i in lst if type(i) == elements.Identifier]
    references = [r for r in lst if type(r) == elements.Reference]
    for r in references:
        assert r.identifier in identifiers, "reference unknown '%s'" % r.identifier

    S = []
    for i, item in enumerate(lst):
        if type(item) == elements.Identifier:
            pre_static = sum(len(pre) for pre in lst[:i]
                             if type(pre) != elements.Reference)
            S.append(pre_static)

    N = len(S)

    idxs_identifiers = [item.identifier for item in lst
                        if type(item) == elements.Identifier]

    Cr = []
    for i, item in enumerate(lst):
        if type(item) == elements.Identifier:
            pre_refs = [idxs_identifiers.index(pre.identifier)
                        for pre in lst[:i] if type(pre) == elements.Reference]
            Cr.append([(1 if i in pre_refs else 0) for i in range(N)])

    for R in iterR(N):
        rst = coefs(S, Cr, R)
        if validate(rst):
            break

    CrR = [sum((cij * ai) for cij, ai in zip(ci, R)) for ci in Cr]

    X = [(si + ci) for si, ci in zip(S, CrR)]

    router = {k: str(v) for k, v in zip(idxs_identifiers, X)}

    rst = ''.join((item if type(item) == str else
                   (item.content if type(item) == elements.Identifier
                                 else router[item.identifier]))
                  for item in lst)
    return rst
