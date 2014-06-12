# -*- coding: utf-8 -*-

import unittest

from yum import YummyDict
from errors import YumValidationError


empty_dict = {}
simple_dict = {'raw': 'test'}
digit_key_dict = {1: 2, 'any': 'text'}
leading_underscore_key_dict = {'_leading': 'underscore', 'any': 'text'}


class SimpleCheck(unittest.TestCase):
    def test_init(self):
        obj = YummyDict(empty_dict)
        self.assertIsInstance(obj, YummyDict)


class ValidationCheck(unittest.TestCase):
    def test_invalid_input_with_digit_key(self):
        with self.assertRaises(YumValidationError):
            YummyDict(digit_key_dict)

    def test_invalid_input_with_leading_underscore_key(self):
        with self.assertRaises(YumValidationError):
            YummyDict(leading_underscore_key_dict)


class InterfaceCheck(unittest.TestCase):
    def test_raw(self):
        obj = YummyDict(simple_dict)
        self.assertEqual(obj._raw_data, simple_dict)


class ReadWriteCheck(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()
