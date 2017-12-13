import sys
sys.path.append("..")
import lib.plr
import unittest
import numpy as np
import pandas as pd

#load test stock (more to be added later)
aapl = pd.read_csv("tests/assets/AAPL_data.csv")["Close"].values

class ConnectLine(unittest.TestCase):

    def test_positive(self):
        '''connect_line should fail with negative values in span_tuple'''
        self.assertRaises(ValueError, lib.plr.connect_line, aapl, (-1, 100))
        self.assertRaises(ValueError, lib.plr.connect_line, aapl, (-10, -50))
        self.assertRaises(ValueError, lib.plr.connect_line, aapl, (30, -75))

    def test_order(self):
        '''connect_line should fail when last is greater than first'''
        self.assertRaises(ValueError, lib.plr.connect_line, aapl, (10, 1))

    def test_two_input(self):
        '''connect_line should fail with more than two items in span_tuple'''
        self.assertRaises(ValueError, lib.plr.connect_line, aapl, (10, 1, 5))

    def test_int(self):
        '''connect_line should fail when elements of span_tuple are not ints'''
        self.assertRaises(ValueError, lib.plr.connect_line, aapl, (1.5, {}))

class LinePointDistance(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()
