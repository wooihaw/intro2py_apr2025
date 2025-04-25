# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 17:11:20 2025

@author: wooihaw
"""

s1 = set(range(1, 101))  # set of all numbers from 1 to 100
s2 = set(range(5, 101, 5))  # set of all numbers divisible by 5
s3 = set(range(7, 101, 7))  # set of all numbers divisible by 7

ans = s1 - (s2 | s3)
print(ans)