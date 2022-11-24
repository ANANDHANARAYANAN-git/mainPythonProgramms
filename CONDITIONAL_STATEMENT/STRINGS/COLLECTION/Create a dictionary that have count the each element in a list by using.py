lst=['hello','hai','orange','hello','orange','hello']
dic={}
for i in lst:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]=dic[i]+1
print(dic)

for i in dic.items():
    print(i)

for i,k in dic.items():
    print(i,k)