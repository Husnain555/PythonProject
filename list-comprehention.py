num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# my_list = []
# for i in num:
#     my_list.append(i)
#     print(my_list)

# my_list = [n for n in num]
# print(my_list)

# using map + lambda
# my_list = map(lambda n: n*n ,num)
# print(list(my_list))

# my_list = []
# for i in num:
#     if i % 2 == 0 :
#         my_list.append(i)
#         print(my_list)


# my_list = filter(lambda x:x % 2 == 0, num)
# print(list(my_list))

# my_list = [n for n in num if n % 2 == 0]
# print (my_list)


# my_list = [(letter,num) for letter in letters for n in num if n % 2 == 0]
# new_list = map(lambda letter: letter[1] % 2 == 0, my_list)
# print(new_list)

# zipping
name = ['Husnain', 'Hassan', 'Awais', 'Zaman']
hero = ['Superman', 'Spiderman', 'Batman', 'Ironman']

# Using zip to pair the items
zipped_list = zip(name, hero)

# Convert the zip object to a list and print
print(list(zipped_list))
