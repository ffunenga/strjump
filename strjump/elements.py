#!/usr/bin/env python3


class Reference:

    def __init__(self, identifier):
        self.identifier = identifier

    def representation(self):
        return "{ref:%s}" % repr(self.identifier)


class Identifier:

    def __init__(self, identifier, content):
        self.identifier = identifier
        self.content = content

    def representation(self):
        return "{id=%s:'%s'}" % (repr(self.identifier), str(self.content))

    def __len__(self):
        return len(self.content)
