#!/usr/bin/env python3


class Reference:

    def __init__(self, identifier):
        self.identifier = identifier

    def compile(self, value):
        return value

    def __repr__(self):
        return "Ref(%s)" % repr(self.identifier)

    def __len__(self):
        return 0

    def __str__(self):
        return "{ref:%s}" % repr(self.identifier)


class Identifier:

    def __init__(self, identifier, content):
        assert type(content) == str
        assert len(content) == 1
        self.identifier = identifier
        self.content = content

    def reference(self):
        return Reference(self.identifier)

    def flat(self):
        return self.content

    def __repr__(self):
        return "Id(%s:'%s')" % (repr(self.identifier), self.content)

    def __len__(self):
        return len(self.content)

    def __str__(self):
        return "{id=%s:'%s'}" % (repr(self.identifier), str(self.content))
