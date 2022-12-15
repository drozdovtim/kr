import unittest
from kr import *


class Testsnakecase(unittest.TestCase):

    def test_snake(self):
        s = NameConverterS('S-Case')
        res = s.to_snake_case()
        self.assertEqual(res, 's__case')


class Testcamelcase(unittest.TestCase):

    def test_camel(self):
        d = NameConverterC('C-Case')
        res = d.to_camel_case()
        self.assertEqual(res, 'CCase')


if __name__ == '__main__':
    unittest.main()
