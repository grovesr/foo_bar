'''
Created on Jan 16, 2016

@author: grovesr
'''
import unittest
from foo_bar.minions_bored_game import answer as answer4_3
from foo_bar.minions_bored_game import binomial_coefficient

class TestAnswer(unittest.TestCase):
    
    def test_binomial_coefficient_n5m2(self):
        n = 5
        m = 2
        res = binomial_coefficient(n, m)
        self.assertEqual(res,10)
    
    def test_binomial_coefficient_n8m3(self):
        n = 8
        m = 3
        res = binomial_coefficient(n, m)
        self.assertEqual(res,56)
    
    def test_t1n2(self):
        t = 1
        n = 2
        self.assertEqual(answer4_3(t, n), 1)
    
    def test_t3n2(self):
        t = 3
        n = 2
        self.assertEqual(answer4_3(t, n), 3)
    
    def test_t5n4(self):
        t = 5
        n = 4
        self.assertEqual(answer4_3(t, n), 12)
        
    def test_t9n10(self):
        t = 9
        n = 10
        self.assertEqual(answer4_3(t, n), 1)
        
    def test_t4n4(self):
        t = 4
        n = 4
        self.assertEqual(answer4_3(t, n), 4)
        
    def test_t4n2(self):
        t = 4
        n = 2
        self.assertEqual(answer4_3(t, n), 4)
        
    def test_t7n4(self):
        t = 7
        n = 4
        self.assertEqual(answer4_3(t, n), 4)
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()