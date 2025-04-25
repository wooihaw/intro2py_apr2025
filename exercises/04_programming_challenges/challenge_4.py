# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 17:16:29 2025

@author: wooihaw
"""

def mean(data):
    return sum(data)/len(data)

def median(data):
    n = len(data)
    if n % 2:
        return data[n // 2]
    else:
        return (data[n // 2 - 1] + data[n // 2]) / 2

with open("data/Heathrow.txt", "r") as f:
    raw_data = f.readlines()
    # print(raw_data)
    data = [float(d.strip()) for d in raw_data]
    # print(data)
    sorted_data = sorted(data)
    print(f"Lowest: {sorted_data[0]}, Highest: {sorted_data[-1]}")
    print(f"Average: {mean(sorted_data)}, Median: {median(sorted_data)}")
    