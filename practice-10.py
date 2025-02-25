#  List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
list = []

for x in fruits:
    if "b" in x:
        list.append(x)
        print(list)

for x in fruits:
    if "k" in x:
        list.append(x)
        print(list)

newlist = [x for x in fruits if "c" in x]
print(newlist)

newlist = [x for x in fruits if x != "mango"]
print(newlist)

newlist = [x.upper() for x in fruits]
newlist = ["hello" for x in fruits]

print(newlist)


list = [a for a in range(10)]
newlist = [x for x in range(10) if x < 10]

print(list)
print(newlist)
