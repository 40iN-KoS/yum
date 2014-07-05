# -*- coding: utf-8 -*-

import copy
import unittest

from main import Dict, ValidationError


empty_dict = {}
simple_dict = {'raw': 'test'}
complex_dict = {
    'string': 'text',
    'dict': {1:2, 'a':'value'},
    'list': [1, None, 'text'],
    }
digit_key_dict = {1: 2, 'any': 'text'}
leading_underscore_key_dict = {'_leading': 'underscore', 'any': 'text'}


class SimpleCheck(unittest.TestCase):
    def test_init(self):
        obj = Dict(empty_dict)
        self.assertIsInstance(obj, Dict)


class ValidationCheck(unittest.TestCase):
    def test_invalid_input_with_digit_key(self):
        with self.assertRaises(ValidationError):
            Dict(digit_key_dict)

    def test_invalid_input_with_leading_underscore_key(self):
        with self.assertRaises(ValidationError):
            Dict(leading_underscore_key_dict)


class InterfaceCheck(unittest.TestCase):
    def test_raw(self):
        obj = Dict(simple_dict)
        self.assertEqual(obj._raw_object, simple_dict)

    def test_attribute(self):
        obj = Dict(simple_dict)
        self.assertEqual(obj.raw, simple_dict['raw'])


class ReadWriteCheck(unittest.TestCase):
    def test_attribute_assignment(self):
        obj = Dict(simple_dict)
        with self.assertRaises(AttributeError):
            obj.a = 'test'

    def test_mutable_objects(self):
        d = copy.deepcopy(complex_dict)
        obj = Dict(d)
        obj.list.append('value')
        obj.dict.update({'item': 'value'})
        self.assertEqual(obj.list, complex_dict['list'])
        self.assertEqual(obj.dict, complex_dict['dict'])


if __name__ == "__main__":
    unittest.main()
