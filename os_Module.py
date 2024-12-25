import os

print(os.getcwd())
# print(dir(os))
#we can change dir through chdir its os method
print(os.name)
print(os.sep)
print(os.linesep)
# mod_time = os. start('demo').st_mtime
# print(mod_time)


# print("Current working directory:", os.getcwd())
# for dirpath, dirnames, filenames in os.walk('.'):
#     print(dirpath, dirnames, filenames)

# print(os.environ.get('HOME'))
# Create a path
# file_path = os.path.join(os.getcwd(), 'test.py')
# with open('test.py', 'w') as f:
#     f.write("# This is a test file")
#
# print(file_path)
#
# if os.path.exists(file_path):
#     file_descriptor = os.open(file_path, os.O_RDONLY)
#     print(f"File opened successfully with descriptor: {file_descriptor}")
#     os.close(file_descriptor)
# else:
#     print("Error: File does not exist.")



file_path1 = os.path.join(os.getcwd(),'test.js')
# with open(file_path1,'w') as m:
#         m.write("# This is a test file created with py os module")
#         if os.path.exists(file_path1):
#             file_dis = os.open(file_path1, os.O_RDONLY)
#             print(f"File opened successfully with descriptor: {file_dis}")
#         else:
#             print(f"File does not exist.")


if os.path.exists(file_path1):
    os.remove(file_path1)
    print(f"File deleted successfully{file_path1}")