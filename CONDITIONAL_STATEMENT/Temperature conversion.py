
#perform temperature conversion?

#celcius to faren heat f=c*9/5+32
#faren heat to celcius c==f-32*5/9

print("choice1=convert celcius to faren heat\nchoise2=convert faren heat to celcius")
ch=int(input("choice"))
if ch==1:
    c = float(input("enter temperature in celcius"))
    f=c*9/5+32
    print("faren heat is",f)
elif ch==2:
    f = float(input("enter temperature in faren heat"))
    c=(f-32)*5/9
    print("celcius is",c)
else:
    print("wrong choice")