#!/usr/bin/env python3


class Reference:

    def __init__(self, identifier):
        self.identifier = identifier
        self.length = 1
        self.content = '{ref:%s}' % repr(self.identifier)

    def set(self, content):
        self.content = content
        self.length = len(content)

    def __len__(self):
        return self.length

    def representation(self):
        return "{ref:%s}" % repr(self.identifier)

    def __str__(self):
        return self.content


class Identifier:

    def __init__(self, identifier, content):
        assert type(content) == str
        assert len(content) == 1
        self.identifier = identifier
        self.content = content

    def flat(self):
        return self.content

    def set_preceding(self, pre_lenstatic, pre_refs):
        self.pre_lenstatic = pre_lenstatic
        self.quotients = pre_refs

    def calc_x(self, rlens):
        #rlens = list(rlens)
        #print("quotients:", self.quotients, "rlens:", rlens)
        return self. pre_lenstatic + sum((l * xi) for l, xi in zip(self.quotients, rlens))

    def __len__(self):
        return len(self.content)

    def representation(self):
        return "{id=%s:'%s'}" % (repr(self.identifier), str(self.content))

    def __str__(self):
        return self.content
