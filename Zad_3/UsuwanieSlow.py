import os

wordsToRemove = ['się','i','oraz','nigdy','dlaczego']
fileName = input('Podaj nazwe pliku: ')

with open(fileName) as fileIn, open(fileName+'edited.txt','w+') as fileOut:
    for word in fileIn:
        for word in wordsToRemove:
            line=line.replace(word, "")
    fileOut.write(line)