import datetime
person = {

"name":"Husnain",
    'age' : 27
}

self = 'My name is' + person['name'] +' My age is' + str(person['age'])
self1 = f"My name is {person["name"]} My age is {person['age']}"
self2 = 'My name is {} My age is {}'.format(person['name'], person['age'])
print(self)
print(self1)
print(self2)


pi = 3.14468456
value = 'this is pi value {:.2f}'.format(pi)
print(value)


pi1 = 3.25697452
valyue = 'this is pi value is wrong {:.3f}'.format(pi1)
print(valyue)

#by adding .2f or .2f

#convertion

mb = 1
bytes = '1 mb equal in bytes is {:,}'.format(1000**2)
print(bytes)


#formating dates

date = datetime.datetime(2025,1,1,12,00,00)
new_date=date.utcnow()
print(new_date)
print(date)
