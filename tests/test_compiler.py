#!/usr/bin/env python3


import unittest
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
        #print("Result:", result)
        self.assertEqual('1:9,2:15|first|second|', result)

    def test_compiler2(self):
        string = [
            '1:',
            strjump.Identifier(1, 'f'),
            'irst,2:',
            strjump.Reference(2),
            ',|1:',
            strjump.Reference(1),
            ',|',
            strjump.Identifier(2, 's'),
            'econd|'
        ]
        #print("String to process:", '"' + strjump.tools.repr_string(string) + '"')
        result = strjump.process(string)
        #print("Result:", result)
        self.assertEqual('1:first,2:19,|1:2,|second|', result)
