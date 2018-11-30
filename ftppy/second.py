import string
import re
str="abdabsa"
print(re.sub("a", "b", str))
print(str.find("w"))
# s=5+8
# print(int(5+8),type(int(s)))
# print(repr(5+8),type(repr(s)))
# print(repr(3-1))
str="abac ccac"

# print(str.split())
a=str.partition(" ")
print(a,type(a))
print(str.replace("c","d",2))
print(str.strip("ac"))
print("d" in str)
print(ord("a"))
print(string.digits)
print(string.ascii_lowercase)
print(string.ascii_letters)
print(string.ascii_uppercase)