def hello():
    num = 0
    while True:
        print('Counting')
        num += 1
        print(num)
        if num == 10000:
            print('Goodbye')
            break
    # pass
#hello()
def multiply(num1, num2):
    return num1 * num2
result = multiply(40,50)
# print(result)
def concat (a, b):
    return a + b
result1 = concat('4','5')
# print(result1)


def greeting(greeting, name = 'Husnain'):
    return f'Hello, {greeting},{name}!'
# print(greeting('Hello'))
def student(*args,**kwargs):
    print(args)
    print(kwargs)
# print(student('hello','world'))
course = ['Python','javaScript']
info = {'name':'Husnain','age':30}
print(student(*course,**info))


#finding leap year in
def is_year (year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
year = is_year(2025)
print(year)


def soloword(word):
    return 'Husnain'

print(soloword('Python'))