#!/bin/python3
# Author: Harry Chong
# Data: 9/3/2020
# Day 26: Nested Logic
## https://www.hackerrank.com/challenges/30-nested-logic

# Enter your code here. Read input from STDIN. Print output to STDOUT
a_day, a_month, a_year = input().split(" ") # Actal Date
e_day, e_month, e_year = input().split(" ") # Expected Date

# Convert String to Int
a_day, a_month, a_year = int(a_day), int(a_month), int(a_year)
e_day, e_month, e_year = int(e_day), int(e_month), int(e_year)

# If the book is returned after the calendar year:
if a_year > e_year: 
    print(10000)
    exit()
elif e_year > a_year:
    print(0)
    exit()

# If the book is returned before the due date:
if a_month <= e_month and a_day < e_day and a_year <= e_year:
    print(0)
    exit()

# If the book is returned after the expected return day but within the same month and year:
if a_month == e_month and a_year == e_year:
    late_days = a_day - e_day
    fee = 15 * (late_days)
    print(fee)
    exit()

# If the book is returned after the expected return month but within the same calendar year:
if a_month > e_month and a_year == e_year:
    late_months = a_month - e_month
    fee = 500 * (late_months)
    print(fee)
    exit()

