'''
Created on Jan 16, 2016

@author: grovesr
'''
import unittest
from foo_bar.challenge1 import answer1
from foo_bar.challenge2 import answer2_2

class TestChallenge1(unittest.TestCase):
    
    def test1(self):
        st="2*4*3+9 *3+ 5"
        res = answer1(st)
        self.assertEqual(res, '243**93*5++')

class TestChallenge2(unittest.TestCase):


    def test1(self):
        intervals = [[1,2],]
        res = answer2_2(intervals)
        self.assertEqual(res, 1)
        intervals = [[1,2**30-1],]
        res = answer2_2(intervals)
        self.assertEqual(res, 2**30-2)
        intervals = [[1,2],[2,2**30-1]]
        res = answer2_2(intervals)
        self.assertEqual(res, 2**30-2)
        intervals = [[1,2],[3,4]]
        res = answer2_2(intervals)
        self.assertEqual(res, 2)
        intervals = [[1,2],[4,5]]
        res = answer2_2(intervals)
        self.assertEqual(res, 2)
        intervals = [[2,4],[1,2],[4,5]]
        res = answer2_2(intervals)
        self.assertEqual(res, 4)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()