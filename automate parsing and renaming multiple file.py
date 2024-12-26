import os
# print(os.chdir('/Users/talk2/PycharmProjects/PythonProject'))

for f in os.listdir():
    if f.endswith('.txt'):
        os.rename(f, f.replace(' ', '_'))
        print(f)