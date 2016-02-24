'''
Created on Jan 30, 2016

@author: grovesr

google foo.bar challenge 1
'''

import re
def answer(st):
    if any(re.findall(r'[^0-9+*\s]',st)):
        # input has invalid characters
        # allow spaces
        return -1
    # collect the groups of characters separated by +
    m=re.findall(r'[\d*]+',st.replace(' ',''))
    result = ''
    numAddOperands = 0
    for grp in m:
        result += ''.join(re.findall('\d',grp)) + ''.join(re.findall('\*',grp))
        numAddOperands += 1
    result += '+' * (numAddOperands - 1)
    return result

def main():
    st="2*4*3+9 *3+ 5"
    print answer(st)

if __name__ == '__main__':
    main()
