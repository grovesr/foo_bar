'''
Created on Jan 16, 2016

@author: grovesr
'''
import unittest
from foo_bar.challenge1 import answer as answer1
from foo_bar.zombit_monitoring import answer as answer2_2
from foo_bar.string_cleaning import answer as answer3_1
from foo_bar.when_it_rains_it_pours import answer as answer3_2
from foo_bar.minion_interrogation import answer as answer3_3

class TestChallenge1(unittest.TestCase):
    
    def test1(self):
        st="2*4*3+9 *3+ 5"
        res = answer1(st)
        self.assertEqual(res, '243**93*5++')

class TestChallenge2_2(unittest.TestCase):


    def test1(self):
        intervals = [[1,2],]
        res = answer2_2(intervals)
        self.assertEqual(res, 1)
    def test2(self):
        intervals = [[1,2**30-1],]
        res = answer2_2(intervals)
        self.assertEqual(res, 2**30-2)
    def test3(self):
        intervals = [[1,2],[2,2**30-1]]
        res = answer2_2(intervals)
        self.assertEqual(res, 2**30-2)
    def test4(self):
        intervals = [[1,2],[3,4]]
        res = answer2_2(intervals)
        self.assertEqual(res, 2)
    def test5(self):
        intervals = [[1,2],[4,5]]
        res = answer2_2(intervals)
        self.assertEqual(res, 2)
    def test6(self):
        intervals = [[2,4],[1,2],[4,5]]
        res = answer2_2(intervals)
        self.assertEqual(res, 4)
        
from random import randint
def create_testcase(message, word, numInsertions = None, insertionPoints = None):
    alteredMessage = message
    insertionPts = []
    if numInsertions and insertionPoints:
        raise Exception('You can''t specify insertionPoints and numInsertions')
    if not message and numInsertions is not None:
        alteredMessage = word
        numInsertions -= 1
        insertionPts.append(0)
    if numInsertions:
        for indx in range(numInsertions):
            insertionPoint = randint(0,len(alteredMessage)-1)
            insertionPts.append(insertionPoint)
            alteredMessage = alteredMessage[:insertionPoint] + word + alteredMessage[insertionPoint:]
    if insertionPoints:
        if not message:
            raise Exception('If you pass in an empty message, you can''t specify insertionPoints')
        for insertionPoint in insertionPoints:
            alteredMessage = alteredMessage[:insertionPoint] + word + alteredMessage[insertionPoint:]
        insertionPts = insertionPoints
    return alteredMessage, insertionPts
import re
class TestChallenge3_1(unittest.TestCase):
    def test1(self):
        word =    "aabaa"
        message = "rodsjkashsljkasehf"
        insertionPoints = [4, 12, 16, 21, 7]
        numInsertions = None
        chunk, insertionPoints = create_testcase(message, word, 
                                                 numInsertions = numInsertions,
                                                 insertionPoints = insertionPoints)
#         print message
#         print word
#         print insertionPoints
#         print chunk
        result = answer3_1(chunk, word)
#         print result
        self.assertIn(re.sub(word, '', message), result)

    def test2(self):
        message = "rodsjkasdfhdshsaiehf"
        word =    "rodsjkashdshsljkasehf"
        insertionPoints = None
        numInsertions = 5
        chunk, insertionPoints = create_testcase(message, word, 
                                                 numInsertions = numInsertions,
                                                 insertionPoints = insertionPoints)
#         print message
#         print word
#         print insertionPoints
#         print chunk
        result = answer3_1(chunk, word)
#         print result
        self.assertIn(re.sub(word, '', message), result)
    
    def test3(self):
        word = "g"
        message = ""
        insertionPoints = None
        numInsertions = 5
        chunk, insertionPoints = create_testcase(message, word, 
                                                 numInsertions = numInsertions,
                                                 insertionPoints = insertionPoints)
#         print message
#         print word
#         print insertionPoints
#         print chunk
        result = answer3_1(chunk, word)
#         print result
        self.assertIn(re.sub(word, '', message), result)
        
    def test4(self):
        message = 'dogfood'
        chunk = "goodgooogoogfogoood"
        word = "goo"
#         print message
#         print word
#         print chunk
        result = answer3_1(chunk, word)
#         print result
        self.assertIn(re.sub(word, '', message), result)
        
    def test5(self):
        message = 'looo'
        chunk = "lololololo"
        word = "lol"
#         print message
#         print word
#         print chunk
        result = answer3_1(chunk, word)
#         print result
        self.assertIn(re.sub(word, '', message), result)
        
    def test6(self):
        message = 'lo'
        chunk = "lolol"
        word = "lol"
#         print message
#         print word
#         print chunk
        result = answer3_1(chunk, word)
#         print result
        self.assertIn(re.sub(word, '', message), result)
    
    def test7(self):
        word =    "aabaa"
        message = "rodsjkashsljkasehf"
        numInsertions = 15
        chunk, insertionPoints = create_testcase(message, word, 
                                                 numInsertions = numInsertions,
                                                 insertionPoints = None)
#         print message
#         print word
#         print insertionPoints
#         print chunk
        result = answer3_1(chunk, word)
#         print result
        self.assertIn(re.sub(word, '', message), result)
    
import random
class TestChallenge3_2(unittest.TestCase):
    def test1(self):
        heights = [1, 4, 2, 5, 1, 2, 3]
        self.assertEqual(answer3_2(heights), 5)
        
    def test2(self):
        heights = [1, 2, 3, 2, 1]
        self.assertEqual(answer3_2(heights), 0)
        
    def test3(self):
        heights = [1  ,2  ,3  ,4  ,4  ,3  ,6  ,7  ,2  ,1  ,2  ,3  ,9  ,8  ,1  ,2  ,3  ,4  ,8  ]
        #                          1           5   6   5   4           7   6   5   4       = 43
        self.assertEqual(answer3_2(heights), 43)
        
    def test4(self):
        heights = [1,1]
        self.assertEqual(answer3_2(heights), 0)
        
    def test5(self):
        heights = [1,2]
        self.assertEqual(answer3_2(heights), 0)
        
    def test6(self):
        heights = [2,1]
        self.assertEqual(answer3_2(heights), 0)
        
    def test7(self):
        heights = [2,2]
        self.assertEqual(answer3_2(heights), 0)
        
    def test8(self):
        heights = [1,1,1]
        self.assertEqual(answer3_2(heights), 0)
        
    def test9(self):
        heights = [1,1,2]
        self.assertEqual(answer3_2(heights), 0)
        
    def test10(self):
        heights = [1,1,3]
        self.assertEqual(answer3_2(heights), 0)
        
    def test11(self):
        heights = [1,2,1]
        self.assertEqual(answer3_2(heights), 0)
        
    def test12(self):
        heights = [1,2,2]
        self.assertEqual(answer3_2(heights), 0)
        
    def test13(self):
        heights = [1,2,3]
        self.assertEqual(answer3_2(heights), 0)
        
    def test14(self):
        heights = [1,3,1]
        self.assertEqual(answer3_2(heights), 0)
        
    def test15(self):
        heights = [1,3,2]
        self.assertEqual(answer3_2(heights), 0)
        
    def test16(self):
        heights = [1,3,3]
        self.assertEqual(answer3_2(heights), 0)
        
    def test17(self):
        heights = [2,1,1]
        self.assertEqual(answer3_2(heights), 0)
        
    def test18(self):
        heights = [2,1,2]
        self.assertEqual(answer3_2(heights), 1)
        
    def test19(self):
        heights = [2,1,3]
        self.assertEqual(answer3_2(heights), 1)
    
    def test20(self):
        heights = [2,2,1]
        self.assertEqual(answer3_2(heights), 0)
        
    def test21(self):
        heights = [2,2,2]
        self.assertEqual(answer3_2(heights), 0)
        
    def test22(self):
        heights = [2,2,3]
        self.assertEqual(answer3_2(heights), 0)
        
    def test23(self):
        heights = [2,3,1]
        self.assertEqual(answer3_2(heights), 0)
        
    def test24(self):
        heights = [2,3,2]
        self.assertEqual(answer3_2(heights), 0)
        
    def test25(self):
        heights = [2,3,3]
        self.assertEqual(answer3_2(heights), 0)
    
    def test26(self):
        heights = [3,1,1]
        self.assertEqual(answer3_2(heights), 0)
        
    def test27(self):
        heights = [3,1,2]
        self.assertEqual(answer3_2(heights), 1)
        
    def test28(self):
        heights = [3,1,3]
        self.assertEqual(answer3_2(heights), 2)
    
    def test29(self):
        heights = [3,2,1]
        self.assertEqual(answer3_2(heights), 0)
        
    def test30(self):
        heights = [3,2,2]
        self.assertEqual(answer3_2(heights), 0)
        
    def test31(self):
        heights = [3,2,3]
        self.assertEqual(answer3_2(heights), 1)
        
    def test32(self):
        heights = [3,3,1]
        self.assertEqual(answer3_2(heights), 0)
        
    def test33(self):
        heights = [3,3,2]
        self.assertEqual(answer3_2(heights), 0)
        
    def test34(self):
        heights = [3,3,3]
        self.assertEqual(answer3_2(heights), 0)

    def test35(self):
        heights = [random.randint(1,100000) for k in range(9000)]
        self.assert_(isinstance(answer3_2(heights), int))
    
class TestChallenge3_3(unittest.TestCase):
    
    def test1(self):
        minions = [[5, 1, 5], [10, 1, 2]]
        res = answer3_3(minions)
        self.assertListEqual(res, [1,0])
    
    def test2(self):
        minions = [[390, 185, 624], [686, 351, 947], [276, 1023, 1024], [199, 148, 250]]
        res = answer3_3(minions)
        self.assertListEqual(res, [2,3,0,1])
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()