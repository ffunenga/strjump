#!/usr/bin/env python3


import math
import itertools
import operator

from . import elements


def process(lst):
    types = [str, elements.Reference, elements.Identifier]
    for i, s in enumerate(lst):
        __flag = any(isinstance(s, t) for t in types)
        assert __flag, "type of lst[%d] is unknown (%s)" % (i, type(s))
        #assert type(s) in types, "type of lst[%d] is unknown (%s)" % (i, type(s))
    identifiers = [i.identifier for i in lst if isinstance(i, elements.Identifier)]
    references = [r for r in lst if isinstance(r, elements.Reference)]
    for r in references:
        assert r.identifier in identifiers, "reference unknown '%s'" % r.identifier

    # ~0.4 %
    count = 0
    S = []
    idxs_identifiers = []
    for item in lst:
        if isinstance(item, elements.Reference):
            continue
        if isinstance(item, elements.Identifier):
            S.append(count)
            idxs_identifiers.append(item.identifier)
        count += len(item)
    N = len(S)
    router0 = {k: v for v, k in enumerate(idxs_identifiers)}

    # ~3.7 %
    Cr = []
    row = [0] * N
    for item in lst:
        if isinstance(item, str):
            continue
        if isinstance(item, elements.Identifier):
            Cr.append(row)
            continue
        if isinstance(item, elements.Reference):
            row = row[:]
            row[router0[item.identifier]] = 1

    # ~71.4 %
    R = [(math.floor(math.log10(si) + 1)) for si in S]
    while True:
        flag = True
        for i, (ri, si, ci) in enumerate(zip(R, S, Cr)):
            si += sum(map(operator.mul, ci, R))
            si = int(math.floor(math.log10(si)))
            si += 1
            R[i] = si
            flag = flag and (ri == si)
        if flag:
            break

    # ~24.5 %
    CrR = (sum(map(operator.mul, ci, R)) for ci in Cr)
    X = ((si + ci) for si, ci in zip(S, CrR))
    router1 = {k: str(v) for k, v in zip(idxs_identifiers, X)}

    id_or_ref = lambda i: i.content if isinstance(i, elements.Identifier) else router1[i.identifier]
    str_or_obj = lambda i: i if type(i) == str else id_or_ref(i)
    rst = ''.join(map(str_or_obj, lst))
    return rst
