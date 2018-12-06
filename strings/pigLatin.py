#!/usr/bin/python
# python 3.7
# -*- coding: utf-8 -*-
# ==============================================================================
#
#         FILE: pigLatin.py
#
#        USAGE: ./pigLatin.py
#
#  DESCRIPTION: # Changes user input to pig latin and return a string
#
#       AUTHOR: Justen Crockett
#      VERSION: 1.0
#      CREATED: 12/05/2018
# ==============================================================================


def pig_latin(uInput):

    list1 = uInput.split()
    i = 0
    c = len(list1)
    pTempList = list()

    for i in range(c):
        tempList = list(list1[i])
        tempList.append(tempList[0])
        tempList.remove(tempList[0])
        tempList.append("-ay")
        pList = tempList.copy()
        str1 = ''.join(pList)

        while i in range(c):
            pTempList.append(str1)
            break
        i = i + 1

    pString = ' '.join(pTempList)

    return pString


userInput = input("Enter a string to convert to pig latin: ")



print("Pig latin version:\n" + pig_latin(userInput))
