'''
Created on Jan 16, 2016

@author: grovesr
'''
import unittest
from foo_bar.binary_bunnies import answer as answer4_2

class TestAnswer(unittest.TestCase):
    
    def test_59821(self):
        seq = [5, 9, 8, 2, 1]
        self.assertEqual(answer4_2(seq), '6')
    
    def test_52981(self):
        seq = [5, 2, 9, 8, 1]
        self.assertEqual(answer4_2(seq), '6')
    
    def test_12345678910(self):
        seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(answer4_2(seq), '1')
        
    def test_421356(self):
        seq = [4, 2, 1, 3, 5, 6]
        self.assertEqual(answer4_2(seq), '20')
        
    def test_3214(self):
        seq = [3, 2, 1, 4]
        self.assertEqual(answer4_2(seq), '3')
        
    def test_4321(self):
        seq = [4, 3, 2, 1]
        self.assertEqual(answer4_2(seq), '1')
        
    def test_1324(self):
        seq = [1, 3, 2, 4]
        self.assertEqual(answer4_2(seq), '2')
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()