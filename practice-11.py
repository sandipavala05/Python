# Sort Lists

list2 = [100, 50, 65, 82, 23]
list2 = ["orange", "mango", "kiwi", "pineapple", "banana"]

list2.sort()
list2.sort(reverse=True)

print(list2)

thislist = ["Banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
thislist.sort(key=str.lower)
print(thislist)


def myfunc(n):
  return abs(n - 82)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#  Copy Lists

thislistNew = [100, 50, 65, 82, 23, 700]
mylist = thislistNew.copy()
mylist = list(thislistNew)
mylist = thislistNew[:]

print(mylist)

# Join Lists

list_1 = ["a", "b", "c"]
list_2 = [1, 2, 3]

list3 = list_1 + list_2
print(list3)

# for x in list_2:
#   list_1.append(x)

list_1.extend(list_2)
print(list_1)


