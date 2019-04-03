#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maxStreak' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER m
#  2. STRING_ARRAY data
#

def maxStreak(m, data):
    max_conse = 0
    current_conse = 0
    for attendance in data:
        #iterate through each day's record
        if 'N' in attendance:
            if(current_conse>max_conse):
                max_conse = current_conse
            current_conse = 0
        else:
            current_conse +=1
    if(current_conse>max_conse):
                max_conse = current_conse
    return max_conse


print(maxStreak(4,['NNNN','YNYY','YYYY','YNYN','YYYY','YYYY','YYYY','YYNY','YYYY','NYYN']))

