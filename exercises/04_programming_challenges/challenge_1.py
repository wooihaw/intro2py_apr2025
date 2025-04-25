# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 16:56:17 2025

@author: wooihaw
"""

# c + r = 35
# 2c + 4r = 94

for r in range(36):
    c = 35 - r
    if 2*c + 4*r == 94:
        print(f"There are {c} chickens and {r} rabbits.")
