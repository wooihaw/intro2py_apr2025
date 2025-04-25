# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 17:27:38 2025

@author: wooihaw
"""

from collections import Counter

data = None
with open("data/alice.txt", "r") as f:
    data = f.read()
    
if data is not None:
    t = [c.lower() if c.isalpha() else ' ' for c in data]
    u = ''.join(t)
    w = u.split()
    c = Counter(w)
    print(f"Number of unique words: {len(c)}")
    print(f"10 most common words: {c.most_common(10)}")
    print(f"The word 'alice' appears {c['alice']} times")