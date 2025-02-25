# Lists

list1 = [1, 2, 3, 4]
list2 = [True, False]
list3 = [True, 1, 2, "a"]
list4 = ["a", "b", "c"]
list5 = list((1, 2))


print(list1)
print(list2)
print(list3)
print(list4)
print(list5)
print(len(list1))
print(type(list1))
print(list5[1])
print(list4[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon"]
print(thislist[2:5])


# Change Item Value
thislist[1] = "mango"
thislist[1:2] = ["blackcurrant", "watermelon"]
thislist.insert(2, "watermelon")
thislist.append("orange")
thislist.pop(1)

print(thislist)

itemOne = ["one", "two"]
itemTwo = ["three", "four"]
itemOne.extend(itemTwo)
itemOne.remove("two")
print(itemOne)


list6 = [1, 2, 3, 4, 5, 6]
# list6.remove(1)
list6.pop(1)
del list6[4]
list6.clear()
print(list6)

# Loop Lists

# lists = [1, 2, 3, 4, 5]
# for x in lists:
# for x in range(len(lists)):
    # print(x)

# for-loop
for i in range(0, 9):
    print(i)

#  Using a while loop:
i = 1
while i < 5 :
   print(i)
   i +=1

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
