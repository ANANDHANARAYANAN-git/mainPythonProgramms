#Dictionary({},can't access through index,acess only through key,mutable also)
# dic={'rollno':12,'name':'anu','batch':'BD'}
# print(dic)
# print(dic['rollno'])
# print(dic['name'])
# print(dic['batch'])
#
# dic['location']='ekm'
# print(dic)
#
# dic['batch']='ml'
# print(dic)
#
# dic['rollno']=dic['rollno']+5
# print(dic)

dic={'emphid':102,'empname':'adarsh','salary':30000}
print(dic)
print(dic['salary'])
dic['company']='tcs'
print(dic)
dic['salary']=dic['salary']+5000
print(dic)
dic={}

dic1={'emphid':[102,104],'empname':['adarsh','manu'],'salary':[30000,40000]}
print(dic1['emphid'][1])
print(dic1['empname'][1])
print(dic1['salary'][0])

dic2={'name':'appu','cls':'BCA','regno':121}
print(len(dic2))
print(dic2.keys())
print(dic2.values())
print(dic2.get('cls'))#or print(dic2['cls]
dic2.update({'college':'xyz','place':2})
print(dic2)

#To remove(pop=remove item from imdex,popitem=remove last item)
dic2.pop('college')
print(dic2)
dic2.popitem()
print(dic2)
