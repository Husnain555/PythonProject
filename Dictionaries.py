#Same as key value pair like json
students = {'name ':'Husnain','age':25}
print(students.values() )
del students['age']
print(students)
students.update({'name ':'Zaman','age':257})
print(students)