# -*- coding: utf-8 -*-

import unittest

from yum import YummyDict

empty_dict = {}
simple_dict = {'raw': 'test'}


class SimpleCheck(unittest.TestCase):
    def test_init(self):
        obj = YummyDict(empty_dict)
        self.assertIsInstance(obj, YummyDict)


class ValidationCheck(unittest.TestCase):
    pass


class InterfaceCheck(unittest.TestCase):
    def test_raw(self):
        obj = YummyDict(simple_dict)
        self.assertEqual(obj._raw_data, simple_dict)


class ReadWriteCheck(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()
