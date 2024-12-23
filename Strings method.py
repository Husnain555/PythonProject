print('Hello Worlds')
#Py data types

#String
message = 'Hello Worlds'
print(message)
# Check length of string
print(len(message))
#Slicing in py
print(message[:5])
print(message[6:])
#Lower case
print(message.lower())
print(message.upper())
#find in str
print(message.find('World'))
#replace
new = message.replace('World', 'Python')
print(new)
#combining Strings
greet = 'hello'
name = 'husnain'
greetings = greet + ' ' + name
print(greetings)
#by using F string
new_greetings = f'{greet},{name} welcome'
print(new_greetings)
