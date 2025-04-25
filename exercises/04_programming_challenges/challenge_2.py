# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 17:03:22 2025

@author: wooihaw
"""

invest = float(input("Enter initial investment: "))
rate = float(input("Enter the annual rate (%): "))
years = int(input("Enter the years of invest: "))

print(f"Initial investment: RM{invest}, annual rate: {rate}%, investment year: {years}")

for i in range(years):
    invest = invest + invest * rate/100
    print(f"Year {i+1}: {invest:.2f}")