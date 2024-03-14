city = "Hyderabad"
description = "Hyderabad is one of the top city in india. This is 2nd largest IT sector in india"

def descbycity(city):
    if city == 'Hyderabad':
        print(description)
        print("words in description are ",len(description.split(' ')))
        for word in description.split(' '):
            print(word)

descbycity(city)
print("\n","largest" in description)

print('\n', "Hyderabad"[2:4]) # returns substring of start index and end index ( start index is 0)
print('\n', "Hyderabad".upper())
print('\n', "Hyderabad".lower())
print('\n', "Hyderabad".__init__())
print('\n', "Hyderabad".capitalize())
print('\n', "Hyderabad".count('d')) # it returns no of exists of word or char in string
print('\n', "      Hyderabad  ".strip()) # it will return string by removing white spaces in string
#print('\n', "Hyderabad is famous city".center(' '))


a=10
b=city
c=18.3
print("The value of a {} the value of b {} the value of c \"{}\"".format(a,b,c))




