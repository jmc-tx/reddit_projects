#changes user input to pig latin and return a string

#TODO: validate input, allow for punctuation, convert script into functions

userInput = input("Enter a string to convert to pig latin: ")

list1 = userInput.split()
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

print("Pig latin version:\n" + pString)