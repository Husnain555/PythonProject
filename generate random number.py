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