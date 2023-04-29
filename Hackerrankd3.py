#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    while True: 
        if not (1<=N<=100):
            print("You did not enter a valid input")
            continue
        elif N%2 == 1:
            print("Weird")
            break
        elif (N%2 == 0) and (2<=N<=5):
            print("Not Weird")
            break
        elif (N%2 == 0) and (6<=N<=20):
            print("Weird")
            break
        elif (N%2 == 0) and (N>20):
            print("Not Weird")
            break    
    