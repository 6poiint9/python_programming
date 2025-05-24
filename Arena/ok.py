ok = 69; 

print(type(ok))

for i in range(22, 0, 2): 
    print(i)

ok_list = [69, "whatup", 4.44, '&']

for i in ok_list: 
    print(i, end="  ")

newlist = []

print(" ")

for i in range(4): 
    obj = input(f'Enter element {i + 1}: ')
    newlist.append(obj) 

print(f'element: {newlist}') 

ok = [44, "$okjin", "pas", 494]

print(len(ok))

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#thisdict = dict(name = "John", age = 36, country = "Norway")

#print(thisdict)

thisdict["Price"] = 50.000

print(thisdict)


print(len(thisdict))

