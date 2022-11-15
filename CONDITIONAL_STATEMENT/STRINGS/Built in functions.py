#built in function

#len()-length of string

s="python programming"
print(len(s))

#capitalize()-capitalize first letter

print(s.capitalize())

#title()

print(s.title())#first letter of each word is capitalize.

#upper()

print(s.upper())

#lower()

print(s.lower())

#swapcase()

print(s.swapcase())#upper case convert to lower case and wise versa

#isupper()  checking all letters are in upper case

print(s.isupper())

#islower()  checking all letters are in lower case

print(s.islower())

#isdigit()  checking all letters are digits

print(s.isdigit())

#isalpha()

print(s.isalpha())

#count() count number of letter in given string

print(s.count("o"))

#index() calculate index(position of digit)at first time in give.

print(s.index(' '))
print(s.index("t"))

#strip(to remove given value in n sides)
s="@@@hai@@##"
print(s.strip("@"))

#lstripe(to remove value at left side)

print(s.lstrip("@"))

#rstrip(to remove value at right side)

print(s.rstrip("#"))




