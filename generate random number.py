import random
value =  random.random()
print(value)
value1 = random.uniform(1,10)
print(value1)
value2 = random.randint(1,10)
print(value2)
value3 = random.choice(['husnain','babar','hassan'])
print(value3)
value4 = random.sample(range(1,10),2)
# This method return us a array or we call list
print(value4)
value5 = random.randrange(1,10,2)
print(value5)
colors = ['red','green','blue']
value6 = random.choice(colors)
print(value6)
deck = list(range(1,52))
random.shuffle(deck)
print(deck)


# fake detail card make


for num in range(100):
    first_name = random.choice(['Husnain','Babar','Hasan'])
    last_name = random.choice(['Said','Ali','Hassan'])
    address = random.choice(['Safi','Khan','Mohammed'])
    email = first_name.lower()+'.'+last_name.lower()+'@gmail.com'
    phone_number = '01'+str(random.randint(100000000,999999999))
    print(f'{first_name} {last_name} \n{address} \n{email} \n{phone_number}')
