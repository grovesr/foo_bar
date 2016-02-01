'''
Created on Jan 30, 2016

@author: grovesr

String cleaning
===============

Your spy, Beta Rabbit, has managed to infiltrate a lab of mad scientists who are
turning rabbits into zombies. He sends a text transmission to you, but it is 
intercepted by a pirate, who jumbles the message by repeatedly inserting the 
same word into the text some number of times. At each step, he might have 
inserted the word anywhere, including at the beginning or end, or even into a 
copy of the word he inserted in a previous step. By offering the pirate a 
dubloon, you get him to tell you what that word was. A few bottles of rum later,
 he also tells you that the original text was the shortest possible string 
 formed by repeated removals of that word, and that the text was actually the 
 lexicographically earliest string from all the possible shortest candidates. 
 Using this information, can you work out what message your spy originally sent?

For example, if the final chunk of text was "lolol," and the inserted word was 
"lol," the shortest possible strings are "ol" (remove "lol" from the beginning) 
and "lo" (remove "lol" from the end). The original text therefore must have been 
"lo," the lexicographically earliest string.

Write a function called answer(chunk, word) that returns the shortest, 
lexicographically earliest string that can be formed by removing occurrences of 
word from chunk. Keep in mind that the occurrences may be nested, and that 
removing one occurrence might result in another. For example, removing "ab" 
from "aabb" results in another "ab" that was not originally present. Also keep 
in mind that your spy's original message might have been an empty string.

chunk and word will only consist of lowercase letters [a-z].
chunk will have no more than 20 characters.
word will have at least one character, and no more than the number of 
characters in chunk.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (string) chunk = "lololololo"
    (string) word = "lol"
Output:
    (string) "looo"

Inputs:
    (string) chunk = "goodgooogoogfogoood"
    (string) word = "goo"
Output:
    (string) "dogfood"

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.

'''
import re
def answer(chunk, word):
    leaves = set()
    # look for multiple adjacent instances of word
    wordPattern = re.compile('(' + word +')+(?=' + word + ')')
    # find all potential places where word can be removed from a chunk
    wordLookaheadPattern = re.compile('(' + word[0] + '(?=' + word[1:] + '))')
    # hold all sub chunks that have already been examined, so we don't look 
    # twice.
    examined = []
    # recursively remove word from sub chunks until no word can be found in the
    # sub chunk.  This adds a leaf that is a potential candidate for the
    # original message
    remove_word(chunk, word, wordPattern, wordLookaheadPattern, examined, leaves)
    leaves = list(leaves)
    leaves = sorted(leaves, key = len)
    minLeaves = [leaf for leaf in leaves if len(leaf) == len(leaves[0])]
    minLeaves.sort()
    return minLeaves[0]
    
def remove_word(chunk, word, wordPattern, wordLookaheadPattern, examined, leaves):
    # replace  multiple instances of word with a single instance
    chunk = re.sub(wordPattern , '', chunk)
    # get an iterator containing all places in the current chunk where word
    # can be removed
    m = re.finditer(wordLookaheadPattern, chunk)
    found = False
    for match in m:
        found = True
        # remove word from this specific chunk location
        remainder = chunk[:match.span()[0]] + chunk[match.span()[1] + len(word) - 1:]
        if remainder not in examined:
            # if we haven't already gone down this path
            # recursively remove word from this chunk starting at this location
            remove_word(remainder, word, wordPattern, wordLookaheadPattern, examined, leaves)
            examined.append(remainder)
    if not found:
        # we didn't find any more instances of word in the chunk, this is a 
        # leaf.  Accumulate it for later examination. Since leaves is a set
        # we never have more than one copy of unique leaves
        leaves.add(chunk)

if __name__ == '__main__':
    chunk = "logomologologood" #step3 insert logo at position 10
    word = "logo"
    chunk = "lolol"
    word = "lol"
#     chunk = "goodgooogoogfogoood"
#     word = "goo"
    word = 'hjajdjh'
    chunk = 'rodshjajdjhjajdjhhjkasdfhdshsaihjajdjhehf'
    message = "rodsjkasdfhdshsaiehf"
    print message
    print word
    print chunk
    print
    print answer(chunk, word)