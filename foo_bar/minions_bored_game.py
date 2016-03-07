'''
Created on Mar 01, 2016

@author: grovesr

google foo.bar challenge 4.3

Minion's bored game
===================

There you have it. Yet another pointless "bored" game created by the bored 
minions of Professor Boolean.

The game is a single player game, played on a board with n squares in a 
horizontal row. The minion places a token on the left-most square and rolls a 
special three-sided die. 

If the die rolls a "Left", the minion moves the token to a square one space to 
the left of where it is currently. If there is no square to the left, the game 
is invalid, and you start again.

If the die rolls a "Stay", the token stays where it is. 

If the die rolls a "Right", the minion moves the token to a square, one space 
to the right of where it is currently. If there is no square to the right, the 
game is invalid and you start again.

The aim is to roll the dice exactly t times, and be at the rightmost square on 
the last roll. If you land on the rightmost square before t rolls are done then 
the only valid dice roll is to roll a "Stay". If you roll anything else, the 
game is invalid (i.e., you cannot move left or right from the rightmost square).

To make it more interesting, the minions have leaderboards (one for each n,t 
pair) where each minion submits the game he just played: the sequence of dice 
rolls. If some minion has already submitted the exact same sequence, they 
cannot submit a new entry, so the entries in the leader-board correspond to 
unique games playable. 

Since the minions refresh the leaderboards frequently on their mobile devices, 
as an infiltrating hacker, you are interested in knowing the maximum possible 
size a leaderboard can have.

Write a function answer(t, n), which given the number of dice rolls t, and the 
number of squares in the board n, returns the possible number of unique games 
modulo 123454321. i.e. if the total number is S, then return the remainder upon 
dividing S by 123454321, the remainder should be an integer between 0 and 
123454320 (inclusive).

n and t will be positive integers, no more than 1000. n will be at least 2.


Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) t = 1
    (int) n = 2
Output:
    (int) 1

Inputs:
    (int) t = 3
    (int) n = 2
Output:
    (int) 3
'''

def binomial_coefficient(n, m):
    '''
    Calculate the n'th row of Pascal's triangle and return the m'th element
    from: https://en.wikipedia.org/wiki/Pascal's_triangle
    '''
    row = [0] * (n + 1)
    row[0] = 1
    for k in range(1, n + 1):
        row[k] = row[k - 1] * (n + 1 - k) / k
    return row[m]

def answer(t, n):
    '''
    Envision the game piece movement in two dimensions:
      The horizontal dimension represents the game board squares (1..n).
      The vertical dimension represents throws of the die (1..t).  A move to
      the right looks like a diagonal move down and to the right, since you
      are not only moving right, but advancing one throw as well.  Staying
      looks like a vertical move down and moving left looks like a diagonal
      move to the left and down.  This is basically a lattice path counting
      problem with some constraints.  The moves are picked from the set
      S = {(-1,-1), (0,-1), (1,-1)} and the path length is t.  You end up 
      with a parallelogram which you have to traverse from its upper left
      vertex to its lower right vertex.  Just count all possible paths. 
    
    To get from square 1 to n you have to move right n-1 times.
    
    If t == n - 1 then you have to move right on every throw and there is
      only one path possible.
    
    t can't be < n - 1 or you will never reach the final square in the 
      allotted throws.
    
    If t >= n then you have to throw in some downward movement.  You can move
      down by throwing an Stay (down) or by throwing Left and Right combinations.
      Each Left-Right combination takes you down 2.  
    
    So, count up the paths consisting of R-[D] only and add in the paths
      consisting of R-L-D combinations if they exist.
    This will give you some invalid paths at squares 1 and N since you can't
      move left from square 1 or do anything but stay from square N.  So
      subtract the invalid paths.  
    '''
    
    right = n - 1
    down = t - right
    # number of paths consisting of right and down moves only.
    # choose either right or down
    npaths = binomial_coefficient(t, right)
    if down >= 2:
        # add in the various L-R-D combos with number of L = indx
        for indx in range(1, down / 2 + 1):
            # (number of ways to choose number of L = indx) * (number of ways to choose number of down = down - 2 * indx)
            npaths += binomial_coefficient(t, indx) * binomial_coefficient(t - indx, down - 2 * indx) 
            # we added in some invalid paths that include square 1 and N when 
            # we added in the L-R-D combinations with number of L = indx.  We 
            # can only move R-D from square 1 and D from square N.  This 
            # removes all the lattice paths that went left from square 1 and 
            # right from square N.
            npaths -= binomial_coefficient(down, indx) * binomial_coefficient(down - indx, down - 2 * indx) 
            # TODO: remove added paths that turn left once reaching
            # square N.  The below formula is incorrect since it doesn't take 
            # into account all cases correctly
            npaths -= binomial_coefficient(down, indx) * binomial_coefficient(down - indx, down - 2 * indx) / 2
            
    res = npaths % 123454321
    return int(res)

if __name__ == '__main__':
    t = 1
    n = 2
    print answer(t, n)