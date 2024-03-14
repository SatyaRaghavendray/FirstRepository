
content=input("enter string : ")
d={}
count=0
for i in content:
    c = content.count(i)
    d[i] = c
    if count < c:
        count = c

print(d)


words=content.split(' ')

for ele in words:
    print(ele[::-1]+" ",end="")
print()
l=['a','b','c']
for i in l:
    for j in l:
        for k in l:
            if((i!=j and j!=k and i!=k) or i==j==k):
                print(i,j,k)
