#!/usr/bin/env python3


import math
import itertools
import operator

from . import elements


def process(lst):
    types = [elements.Identifier, elements.Reference, str]
    for i, s in enumerate(lst):
        assert type(s) in types, "type of lst[%d] is unknown (%s)" % (i, type(s))
    identifiers = [i.identifier for i in lst if type(i) == elements.Identifier]
    references = [r for r in lst if type(r) == elements.Reference]
    for r in references:
        assert r.identifier in identifiers, "reference unknown '%s'" % r.identifier

    # ~4.5 ms
    count = 0
    S = []
    idxs_identifiers = []
    for item in lst:
        item_type = type(item)  # Tests: this is faster than isinstance().
        if item_type == elements.Reference:
            continue
        if item_type == elements.Identifier:
            S.append(count)
            idxs_identifiers.append(item.identifier)
        count += len(item)
    N = len(S)
    router0 = {k: v for v, k in enumerate(idxs_identifiers)}

    # ~36.5 ms
    Cr = []
    row = [0] * N
    for item in lst:
        item_type = type(item)
        if item_type == str:
            continue
        if item_type == elements.Identifier:
            Cr.append(row)
            continue
        if item_type == elements.Reference:
            row = row[:]
            row[router0[item.identifier]] = 1

    # ~700 ms
    R = [(math.floor(math.log10(si) + 1)) for si in S]
    while True:
        flag = True
        for i, (ri, si, ci) in enumerate(zip(R, S, Cr)):
            si += sum(map(operator.mul, ci, R))
            si = math.floor(math.log10(si))
            si += 1
            R[i] = si
            flag = flag and (ri == si)
        if flag:
            break

    # ~240 ms
    CrR = (sum(map(operator.mul, ci, R)) for ci in Cr)
    X = ((si + ci) for si, ci in zip(S, CrR))
    router1 = {k: str(v) for k, v in zip(idxs_identifiers, X)}

    rst = ''.join((item if type(item) == str else
                   (item.content if type(item) == elements.Identifier
                                 else router1[item.identifier]))
                  for item in lst)
    return rst
