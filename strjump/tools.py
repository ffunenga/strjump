#!/usr/bin/env python3


def repr_string(lst):
    return ''.join(s if type(s) == str else s.representation() for s in lst)
