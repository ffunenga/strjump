#!/usr/bin/env python3


import unittest
import itertools
import string
import random
import strjump


class TestCase(unittest.TestCase):

    def test_compiler1(self):
        string = [
            '1:',
            strjump.Reference(1),
            ',2:',
            strjump.Reference(2),
            '|',
            strjump.Identifier(1, 'f'),
            'irst|',
            strjump.Identifier(2, 's'),
            'econd|'
        ]
        #print("String to process:", '"' + strjump.tools.repr_string(string) + '"')
        result = strjump.process(string)
        #print("Result:", '"%s"' % result)
        self.assertEqual('1:9,2:15|first|second|', result)
