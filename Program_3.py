list1 = ['abc', 'xyz', 'aba', '1']
count=0
for i in list1:
    if len(i)>=2:
        count+=1
print("List : ",list1)
print("Count of Strings : ",count)
