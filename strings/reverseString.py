#!/usr/bin/python
# python 3.7
# -*- coding: utf-8 -*-
# ==============================================================================
#
#         FILE: reverseString.py
#
#        USAGE: ./reverseString.py
#
#  DESCRIPTION: # Reverses user input and outputs a string
#
#       AUTHOR: Justen Crockett
#      VERSION: 1.0
#      CREATED: 12/05/2018
# ==============================================================================


userInput = list(input("Enter a string: "))

userInput.reverse()

str1 = ''.join(userInput)

print(str1)