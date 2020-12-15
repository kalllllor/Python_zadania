import os
import random

wordsToReplace = ['i','oraz','nigdy','dlaczego']
replaceWorlds = ['oraz','i','prawie nigdy','czemu']
fileName = input('Podaj nazwe pliku: ')

with open(fileName) as fileIn, open(fileName+'edited.txt','w+') as fileOut:
    for word in fileIn:
        for word in wordsToReplace:
            replaceWord = random.choice(wordsToReplace)
            line=line.replace(word,replaceWord)
        fileOut.write(line)