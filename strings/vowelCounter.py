#!/usr/bin/python
# python 3.7
# -*- coding: utf-8 -*-
# ==============================================================================
#
#         FILE: vowelCounter.py
#
#        USAGE: ./vowelCounter.py
#
#  DESCRIPTION: Accepts a string from user input and returns the number of
#               vowels in that string
#
#       AUTHOR: Justen Crockett
#      VERSION: 1.0
#      CREATED: 12/05/2018
# ==============================================================================


def counter(temp_str):          # counts vowels and returns number

    count = temp_str.count('a') + \
            temp_str.count('e') + \
            temp_str.count('i') + \
            temp_str.count('o') + \
            temp_str.count('u')

    return count


def print_count(ctr):           # prints number of vowels

    print("The number of vowels in this string is: " + str(ctr))


userInput = str(input("Enter a string: "))

print_count(counter(userInput))
