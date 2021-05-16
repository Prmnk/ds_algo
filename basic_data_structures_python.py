# index based search, size is fixed, same data type, if full reconstruction is o(N) complexity - needs rebuild
# insertion at end at last, insert in middle/ removal is o(N) because items need to be moved
# can be multidimensional  - array[][][] - matrix is 2D
# applications - lookup table/hashtable/ heaps

# List in python

num = [1,2,3,4,5]

num[1] = 'Adam'

for i in num:
    print(i)

for i in range(len(num)):
    print(i)

print(num[0:2])

num_n = [2,4,6,8,9,10,4]
print(num_n[:-2]) #all items except last2

# find max
max = num_n[0]
for num in num_n:
    if num>max:
        max = num

print(max)

num_0 = [1,2,4,5,7,3,9,10,45,36,14]
list0 = []
for n in num_0:
    if n%2 ==0 :
        list0.append(n)

print(list0)

# list comprehension

num_2 = [1,2,4,5,7,3,9,10,45,36,14]
num_2.insert(5,6) # insert 6 at index = 5
print(num_2)
list1 = [n*n for n in num_2 ]

print(list1[:])

# map
list2 = map(lambda n: n*n, num_2)
list3 = filter(lambda n: n%2==0, num_2)

print(list(list3)) # map needs to be converted to a list


list_4 = []
for letter in 'abcd':
    for num in range(4):
        list_4.append((letter,num))

list_5 = ((letter,num) for letter in 'abcd' for num in range(4))
print (list_4)

# dictionary comprehension

names= ['a','b','c','d','e']
rolls= [10,20,30,50,40]

dict_1 = {}
for name, roll in zip(names,rolls):
    dict_1[roll] = name

dict_2 = {roll:name for name,roll in zip (names,rolls) if name != 'c'}   

print (dict_1)
print(dict_2)


# Set comprehension

num_5 = [1,1,3,4,2,4,2,5,6,1,4,6,7,7,8,9]

set_1 = set()
for num in num_5:
    set_1.add(num)

set_2  = {n for n in num_5}

print(set_1)
print(set_2)


