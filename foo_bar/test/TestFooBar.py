'''
Created on Jan 16, 2016

@author: grovesr
'''
import unittest
from foo_bar.challenge1 import answer as answer1
from foo_bar.challenge2 import answer as answer2_2
from foo_bar.challenge3_1 import answer as answer3_1

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
class TestChallenge3(unittest.TestCase):
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
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()