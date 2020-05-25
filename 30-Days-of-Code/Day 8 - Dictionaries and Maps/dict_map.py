#!/bin/python3
# Author: Harry Chong
# Data: 5/24/2020
# Day 8: Dictionaries and Maps
# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/

# Enter your code here. Read input from STDIN. Print output to STDOUT
# Denoting the number of entries in the phone book.
n = int(input())

# Setup phone book
phoneBook = {}
for i in range(0, n):
    raw = input()
    data = raw.split()
    name, phone = data[0], data[1]

    phoneBook[name] = phone

# Query phone book
while(True):
    try:
        name = input()
    except:
        exit()
    
    if name in phoneBook:
        print("{}={}".format(name, phoneBook[name]))
    else:
        print("Not found")