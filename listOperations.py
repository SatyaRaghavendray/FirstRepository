fruits = ['banana','pomogranite','grapes','oranges']

print(fruits)

def fruituses(fruitname):
    if fruitname == 'banana':
        print(fruitname," is use for digestion")
    elif fruitname == 'pomogranite':
        print(fruitname," is use for gain in blood quanity")
    elif fruitname == 'grapes':
        print(fruit," is use for gain iron in body")
    elif fruitname == 'oranges':
        print(fruit," is use for vitamin C gain")

for fruit in fruits:
    print(fruit," length of fruit name is", len(fruit))
    fruituses(fruit)

mixlist=[12,'hyderabad',23.4,'delhi']
for d in mixlist:
    if type(d)==int:
        print("this is integer value",d)
    elif type(d)==float:
        print("this is float value",d)
    elif type(d)==str:
        print("this is string value",d)
    elif type(d)==complex:
        print("this is complex value",d)

for i in range(len(mixlist)):
    print(mixlist[i])

newlist=[x for x in mixlist if type(x)==str]
for x in newlist:
    print(x)

newlist=[x if x!='hyderabad' else 'chennai' for x in newlist]
for x in newlist:
    print(x)

l1=['hyderabad','chennai','delhi','vizag']
l2=['mumbai','bangalore','kolkata']
#print(l1+l2)
l1.extend(l2)
print(l1)

i=0
while i<len(l1):
    print(i,l1[i])
    i+=1
