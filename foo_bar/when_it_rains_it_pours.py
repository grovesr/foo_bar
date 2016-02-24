'''
Created on Jan 30, 2016

@author: grovesr

google foo.bar challenge 3.2

When it rains it pours
======================

It's raining, it's pouring. You and your agents are nearing the building where 
the captive rabbits are being held, but a sudden storm puts your escape plans 
at risk. The structural integrity of the rabbit hutches you've built to house 
the fugitive rabbits is at risk because they can buckle when wet. Before the 
rabbits can be rescued from Professor Boolean's lab, you must compute how much 
standing water has accumulated on the rabbit hutches.

Specifically, suppose there is a line of hutches, stacked to various heights 
and water is poured from the top (and allowed to run off the sides). We'll 
assume all the hutches are square, have side length 1, and for the purposes of 
this problem we'll pretend that the hutch arrangement is two-dimensional.

For example, suppose the heights of the stacked hutches are [1,4,2,5,1,2,3] 
(the hutches are shown below):

...X...
.X.X...
.X.X..X
.XXX.XX
XXXXXXX
1425123

When water is poured over the top at all places and allowed to runoff, it will 
remain trapped at the 'O' locations:

...X...
.XOX...
.XOXOOX
.XXXOXX
XXXXXXX
1425123

The amount of water that has accumulated is the number of Os, which, in this 
instance, is 5.

Write a function called answer(heights) which, given the heights of the 
stacked hutches from left-to-right as a list, computes the total area of 
standing water accumulated when water is poured from the top and allowed to 
run off the sides.

The heights array will have at least 1 element and at most 9000 elements. Each 
element will have a value of at least 1, and at most 100000.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int list) heights = [1, 4, 2, 5, 1, 2, 3]
Output:
    (int) 5

Inputs:
    (int list) heights = [1, 2, 3, 2, 1]
Output:
    (int) 0

Use verify [file] to test your solution and see how it does. When you are 
finished editing your code, use submit [file] to submit your answer. If your 
solution passes the test cases, it will be removed from your home folder.
'''
import cProfile
import random
def find_ge(a, x):
    '''Find leftmost item in list that is >= to x.  If nothing is >= x, find
    the leftmost largest item in the list.  In either case, return the index
    and value
    '''
    highestIndex = 0
    highestVal = 0
    if len(a) == 1:
        highestVal = a[0]
    for i,v in enumerate(a):
        if v >= x:
            return i, v
        elif v >= highestVal:
            highestIndex = i
            highestVal = v
    return highestIndex, highestVal

def answer(heights):
    zeros = 0
    lenHeights = len(heights)
    refIndex = 0
    refHeight = heights[refIndex]
    endSpanIndex = 0
    while endSpanIndex < lenHeights - 1:
        endSpanIndex, endSpanHeight = find_ge(heights[refIndex + 1:], refHeight)
        endSpanIndex += refIndex + 1
        minHeight = min(refHeight, endSpanHeight)
        if endSpanIndex > refIndex + 1:
            for k in range(refIndex + 1, endSpanIndex):
                if minHeight > heights[k]:
                    zeros += minHeight - heights[k]
        refIndex = endSpanIndex
        refHeight = heights[refIndex]
    return int(zeros)
        

if __name__ == '__main__':
    heights = [1, 4, 2, 5, 1, 2, 3]
#     heights = [1, 4, 2, 1, 4, 2]
#     heights = [1, 2, 3, 2, 1]
#     heights = [1  ,2e4,3  ,4  ,4  ,3  ,6e4,7  ,2  ,1  ,2  ,3  ,9  ,8  ,1  ,2  ,3  ,4  ,8  ]
    heights = [1  ,2  ,3  ,4  ,4  ,3  ,6  ,7  ,2  ,1  ,2  ,3  ,9  ,8  ,1  ,2  ,3  ,4  ,8  ]
#                                  1           5   6   5   4           7   6   5   4       = 43
    heights = [7, 6, 5, 4, 3, 2, 1] # 0
    heights = [1, 1, 1, 1, 1, 1, 1] # 0
    heights = [1e5, 1, 1, 1, 1, 1, 1e4] # 49995.0
    heights = [100000]
    heights = [5,4,3,2,1,2,3,4,5] # 16
#                1 2 3 4 3 2 1
    heights = [1,2,3,4,5,4,5,3,2,1] # 1
    heights = [1,2,3,4,5,6,7,8] # 0
    heights = [8,7,6,5,4,3,2,1] # 0
    heights = [2,1,1,1,1,1,1,2] # 6
    heights = [1,8,7,6,5,4,3,2] # 0
    heights = [1,2,3,4,5,4,3,2,1,2,3,4,5,4,3,2,1] # 16
    heights = [2,1,1,2,3,1,1,5,2] # 6
    heights = [1,2,1,2,1,2,1,2,1] # 3
    heights = [2,1,2,1,2,1,2,1,2] # 4
    heights = [2,100,2,1,2,1,2,100,2] # 5*99-3 = 492
#     heights = [1,1] #-0
#     heights = [1,2] #-0
#     heights = [2,1] #-0
#     heights = [2,2] # 0
#     heights = [1,1,1] # 0
#     heights = [1,1,2] # 0
#     heights = [1,1,3] # 0
#     heights = [1,2,1] # 0
#     heights = [1,2,2] # 0
#     heights = [1,2,3] # 0
#     heights = [1,3,1] # 0
#     heights = [1,3,2] # 0
#     heights = [1,3,3] # 0
#     heights = [2,1,1] # 0
#     heights = [2,1,2] # 1
#     heights = [2,1,3] # 1
#     heights = [2,2,1] # 0
#     heights = [2,2,2] # 0
#     heights = [2,2,3] # 0
#     heights = [2,3,1] # 0
#     heights = [2,3,2] # 0
#     heights = [2,3,3] # 0
#     heights = [3,1,1] # 0
#     heights = [3,1,2] # 1
#     heights = [3,1,3] # 2
#     heights = [3,2,1] # 0
#     heights = [3,2,2] # 0
#     heights = [3,2,3] # 1
#     heights = [3,3,1] # 0
#     heights = [3,3,2] # 0
#     heights = [3,3,3] # 0
    for k in range(10):
        heights = [random.randint(1,100000) for i in range(4)]
        print k
        print heights
        ans = answer(heights)
#         cProfile.run('answer(heights)')
    

    cProfile.run('answer(heights)')