list1 = 'gfhjjskkkkbdbdbdooooKADFUaufdlAFDJJSJSGGWBBaifduidaf'
dict1 ={}

for i in range(0,len(list1)):
    if list1[i] not in dict1.keys():
        dict1[list1[i]] = 1
    else:
        dict1[list1[i]] = dict1[list1[i]]+1

print (dict1)

dictres = {k:v for k,v in dict1.items() if v >1}

print (dictres)