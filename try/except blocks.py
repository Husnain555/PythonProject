try:
   f = open('file123.txt')
except FileExistsError:
    print('File does not exists')
except Exception as e :
    print(e,'Something went wrong')
else:
    print('File exists')
finally:
    print('File closed')
# raise an error manually
    name = 'Husnain'
    if name == 'Husnain':
        raise NameError('Name already exists')
    else:
        print(f'Your name was added as {name} ')