def square_root (nums):
    result = []
    for i in  nums:
        result.append(i * i)
    return result
my_nums= square_root([1,2,3,4,5,6,7,8,9])
print(my_nums)





def square_root (nums1):
    for i in nums1:
        yield i*i
my_nums= square_root([1,2,3,4,5,6,7,8,9])
print (next(my_nums))
print (next(my_nums))
print (next(my_nums))
print (next(my_nums))
print (next(my_nums))
print (next(my_nums))
print (next(my_nums))
print (next(my_nums))
print (next(my_nums))
