import unittest
from one_away import is_one_away


class DemoTest(unittest.TestCase):

    def test_one_away_fun(self):
        self.assertTrue(is_one_away("pale", "peles"))