#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n%2==1 or ( n%2 == 0 and 5 < n < 21):
        print("Weird")
    elif 1 < n < 6 or n > 20:
        print("Not Weird")
