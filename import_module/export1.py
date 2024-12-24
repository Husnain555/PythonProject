print('Importing module')
def find_index(tosearch,target):
    for index, item in enumerate(tosearch):
        if item == target:
            return index
        else:
            return 'Target not found'
