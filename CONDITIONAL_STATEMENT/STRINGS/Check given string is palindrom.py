#Check sting is palindrome
s=input("Enter the string")
s1=s[::-1]#reverse order
if s==s1:
    print("Sting is palindrome")
else:
    print("String is not palindrome")
