'''
Created on Jan 30, 2016

@author: grovesr

Minion interrogation
====================

You think you have Professor Boolean's password to the control center. All you 
need is confirmation, so that you can use it without being detected. You have 
managed to capture some minions so you can interrogate them to confirm.

You also have in your possession Professor Boolean's minion interrogation 
machine (yes, he interrogates his own minions). Its usage is simple: you ask 
the minion a question and put him in the machine. After some time (specific to 
the minion), you stop the machine and ask the minion for the answer. With 
certain probability (again, specific to the minion) you either get the truthful 
answer or the minion remains silent. Once you have subjected a minion to the 
machine, you cannot use it on the minion again for a long period.

The machine also has a 'guarantee' setting, which will guarantee that the 
minion will answer the question truthfully. Unfortunately, that has the 
potential to cause the minion some irreversible brain damage, so you vow to 
only use it as a last resort: on the last minion you interrogate.

Since Professor Boolean's password is periodically changed, you would like to 
know the answer as soon as possible. So you decide to interrogate the minions 
in an order which will take the least expected time (you can only use the 
machine on one minion at a time).

For example, you have captured two minions: minion A taking 10 minutes, and 
giving the answer with probability 1/2, and minion B taking 5 minutes, but 
giving the answer with probability 1/5.

If you interrogate A first, then you expect to take 12.5 minutes.
If you interrogate B first, then you expect to take 13 minutes and thus must 
interrogate A first for the shortest expected time for getting the answer.

Write a function answer(minions) which given a list of the characteristics of 
each minion, returns the lexicographically smallest ordering of minions, which 
gives you the smallest expected time of confirming the password.

The minions are numbered starting from 0.

The minions parameter will be a list of lists.

minions[i] will be a list containing exactly three elements, corresponding to 
the i^th minion.

The first element of minion[i] will be a positive integer representing the time
 the machine takes for that minion.

The ratio of the second and third elements will be the probability of that 
minion giving you the answer: the second element, a positive integer will be 
the numerator of the ratio and the third element, also a positive integer will 
be the denominator of the ratio. The denominator will always be greater than 
the numerator. That is, [time, numerator, denominator].

The return value must be a list of minion numbers (which are integers), 
depicting the optimal order in which to interrogate the minions. Since there 
could be multiple optimal orderings, return the lexicographically first optimal 
list.

There will be at-least two and no more than 50 minions.
All the integers in the input will be positive integers, no more than 1024.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) minions = [[5, 1, 5], [10, 1, 2]]
Output:
    (int list) [1, 0]

Inputs:
    (int) minions = [[390, 185, 624], [686, 351, 947], [276, 1023, 1024], [199, 148, 250]]
Output:
    (int list) [2, 3, 0, 1]

Use verify [file] to test your solution and see how it does. When you are 
finished editing your code, use submit [file] to submit your answer. If your 
solution passes the test cases, it will be removed from your home folder.

Notes to self, initially ignoring how long each experiment takes:

Possible outcomes (sample space) for each experiment are represented by the denominator
Ways to achieve an answer in each experiment are represented by the numerator

Only use the "guarante" setting on outcome 0, 0, 0, ...1

1) Placing a minion in the machine represents an experiment..
2) Experiments are run sequentially until we get an answer
3) Each experiment has probability P(i) of producing an answer and a
   probability of 1 - P(i) of not producing an answer
4) The last experiment has P(last) = 1 
5) Probability of ultimate success changes after each experiment, because the 
   remaining probabilities are reduced by one
6) P(i) is independent of P(not i), Events are independent.
'''
# from bisect import bisect_left
# def get_combos(minionId, minionDict):
#     reducedMinionDict = minionDict.copy()
#     del(reducedMinionDict[minionId])
#     shortestTime = -1
#     shortestSequence = {}
#     for k in range(len(reducedMinionDict)):
#         for combo in combinations(reducedMinionDict.keys(), k):
#             # probability = 1 for minionId because we are considering an 
#             # outcome where this minion provided the answer
#             probability = 1
#             answerTime = minionDict[minionId][0] * probability
#             noAnswerTime = 0
#             for index in combo:
#                 # add up the probabilities * times of the minion interrogations
#                 # that preceded this one.  Since they didn't provide an answer
#                 # in getting to this point, we use the inverse probability
#                 # to scale the time (i.e. the probability of not providing an 
#                 # answer)
#                 probability *= (1 - minionDict[index][1] / minionDict[index][2])
#                 noAnswerTime += minionDict[index][0]
#             time = (noAnswerTime + answerTime) * probability
#             if time <= shortestTime or shortestTime == -1:
#                 shortestTime = time
#                 listCombo = list(combo)
#                 listCombo.append(minionId)
#                 shortestSequence[shortestTime] = listCombo
#     return shortestSequence


# def get_probability(probabilities, numProbabilities, n):
#     probability = Fraction(1,1)
#     for k in range(numProbabilities - 1):
#         probability *= probabilities[numProbabilities - k - 2][2**k & n > 0]
#     return probability

# def get_permute_time(minionPermutation, probabilities,answerTimes, numMinions):
#     probabilityTime = Fraction(0, 1)
#     time = answerTimes[0]
#     probability = get_probability(probabilities, numMinions - 1, 0)
#     probabilityTime += probability * time
#     for n in range(1, 2**numMinions):
#         time = answerTimes[n]
#         probability = get_probability(probabilities, numMinions, n)
#         probabilityTime += probability * time
#     return probabilityTime

# def get_permute_time(minionPermutation, probabilities, numMinions):
#     probabilityTime = Fraction(0, 1)
#     k = numMinions - 1
#     time = get_time(minions, numMinions, k)
#     for n in range(2**(numMinions - 1)):
#         probability = get_probability(probabilities, numMinions, n)
#         if n == 2**(numMinions - k - 1): #1, 2, 4
#             time = get_time(minions, numMinions, k - 1)
#             k -= 1
#         print time, ' ',probability, ' (%1.5f)'%probability
#         probabilityTime += probability * time
#     print probabilityTime
#     return probabilityTime

from random import randint
from math import factorial
import cProfile

def get_num_combos(n):
    combos = []
    for r in range(n):
        res = (r, factorial(n)/factorial(r)/factorial(n-r))
        print res
        combos.append(res)
    return combos

def create_testcase(numMinions):
    minions = []
    while numMinions:
        time = randint(1,1024)
        denominator = randint(1,1024)
        numerator = randint(1, denominator - 1)
        minions.append([time, numerator, denominator])
        numMinions -= 1
    return minions

from fractions import Fraction
def answer(minions):
    # I was stumped on this one and was forced to resort to Google to get a  
    # hint.  Unfortunately, I not only found a hint, I found the answer.  Once
    # I saw it, I couldn't unsee it.  Oh well.  Anyway, the original source was:
    # https://github.com/mdegraw/GoogleFooBarSolutions
    # I changed it in minor ways by using Fraction for more accurate
    # probabilities and I used lambda for the sort instead of 
    # operator.itemgetter
    
    
    # amount of time we expect each minion to take to provide an answer.  Use
    # fractions to be more accurate
    expectedTimes= [Fraction(minion[0],
                             Fraction(minion[1],minion[2])) for minion in minions]
    # Sort the expected times, while maintaining the indexes through enumeration
    # Then extract the enumerated indexes and return them
    sortedMinionIndexes = [enum[0] for enum in sorted(enumerate(expectedTimes), 
                                                      key = lambda item: item[1])]
    return sortedMinionIndexes
    

if __name__ == '__main__':
#     minions = [[5, 1, 5], [10, 1, 2]]
    minions = [[390, 185, 624], [686, 351, 947], [276, 1023, 1024], [199, 148, 250],]
#     minions = [[513, 64, 76], [700, 746, 836], [1004, 94, 158], [611, 735, 776]] # (0, 3, 1, 2)
#     minions = create_testcase(50)
#     print minions
    print answer(minions)
#     cProfile.run('answer(minions)')