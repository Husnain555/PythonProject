firstName = 'Husnain'
lastName = 'Babar'

fullName = print(f'My full na me is {firstName} {lastName}')

# another methofd is format method

fullName1 = print('My full name is {} {}'.format(firstName, lastName))

# if we have an object
person = {'name': 'Husnain', 'age': 25}
fullName2 = f" My name is {person['name']} and my age is {person['age']}"
print(fullName2)
