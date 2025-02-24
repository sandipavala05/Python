# Strings

print('hello')
print("hello")
print("'hello'")

# Assign String to a Variable

a = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet,
Lorem ipsum dolor sit amet,"""
print(a)

a = "Hello, World!"
print(a[1])

# Looping Through a String
for x in "apple" :
    print(x)

x = "mango"
print(len(x))

# Use it in an if statement:

txt = "Hello World"
print("Hello" in txt)

txt = "Hello World"
if "Hello" in txt :
    print ("true statement")

txt = "Hello World"
if "Hellow" not in txt :
    print ("not present")


txt = "Hello World"
if "Hellow" in txt :
    print ("true statement")
else :
    print ("fasle statement")

# Slicing Strings
b = "Hello, World!"
print(b[1:7])
print(b[:7])
print(b[7:])
print(b[-6:-2])


# Modify Strings
a = " Hello, World!"
print(a.upper())
print(a.lower())
print(a.strip())
print(a.split(","))
print(a.replace("W", "D"))

# String Concatenation
a = "Hello,"
b = "World!"
print(a + b)
print(a + " " + b)

# Format - Strings
age = 20
txt = "John age {age}"
txt1 = f"John age {age}"
txt2 = f"John age {age:.2f}"
txt3 = f"John age {10 * 2}"
txt3 = f"John age {10 + 2}"

print(txt)
print(txt1)
print(txt2)
print(txt3)


# Escape Characters
text = "hello \"world!\" ."
text = "hello \nworld!."
print(text)