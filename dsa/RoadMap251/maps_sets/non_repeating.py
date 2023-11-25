from os import *
from sys import *
from collections import *
from math import *


#brute force = 2 traversal method
def firstNonRepeatingCharacter(str):

    in_ = list(str)
    # print('i am input',in_)
    
    # if there are no dupes
    if (len(in_) - len(set(in_))) == 0:
        return in_[0]

    
    else:
        output_dict = OrderedDict()
        for v in in_: #O(n)
            if v in output_dict:
                output_dict[v] += 1
            else:
                output_dict[v] = 1
        
        # print('i am output dict',output_dict)
        
        for k,v in output_dict.items(): 
            if v ==1:
                return k


#A little good approach
def firstNonRepeatingCharacter(str):
    flag = 0
    for i in str:
        if str.count(i) == 1:
            print(i)
            flag = 1
            break
    if flag == 0:
        print (str[0])