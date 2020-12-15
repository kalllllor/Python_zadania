import random

list1 = [1, 2, 12, 4]
list2 = [2, 4, 2, 8]

if len(list1)>len(list2):
    list2 = list2 + [0]*(list1-list2)
elif len(list2)>len(list1):
    list1 = list1 + [0]*(list2-list1)

result=[]

for i in range(0, len(list1)):
    result.append(list1[i] * list2[i])

print(result)