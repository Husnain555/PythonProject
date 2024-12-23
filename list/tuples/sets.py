#Like array in js python has list in it
course = ['Eng','Phy','urdu']
print(course)
#adding new ite in the list
course.append('Python')
print(course)
#adding in a spesific location
course.insert(1,'Java')
print(course)
#Extend
course2 = ['math','Chemistry']
course.extend(course2)
print(course)
course.sort()
print(course)
#reverse sort / desc
course.reverse()

print(course)
print(min(course))
print(max(course))
# for course in course:
#     print(course)
    # for index,course in enumerate(course):
    #     print(index,course)
course_str = '-'.join(course)
print(course_str)
#######################################Tuples##################
#List are mutable but tuples ere not
list = ('urdu', 'math', 'Chemistry')
list1 = list
print(list)
print(list1)
# list1[0] = 'python'
print(list)
print(list1)
#we won't able to change tuple value


#####################################################Sets###############################
#same as js sets dont has dublicates values
set = {1,2,3,4,5,2}
print(set)
set1 = {3,4,6,87}
print(set.intersection(set1))
#find differences in both
#to join
print(set.union(set1))
#finding diff
print(set.difference(set1))
