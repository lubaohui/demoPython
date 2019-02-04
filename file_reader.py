
"""
一次读取整个文件
"""

with open('pi_digits.txt') as file_object:
    """打开文件句柄，命名别名fiel_object，读取文件全量"""
    contents = file_object.read()
    print(contents)

print('\t')
print('*' * 30)
print('\t')

"""
    文件路径
"""
with open('text_files/pi_digits.txt') as file_object:
    """打开文件句柄，命名别名fiel_object，读取文件全量"""
    contents = file_object.read()
    print(contents)


print('\t')
print('*' * 30)
print('\t')

"""
    逐行读取文件
"""
with open('text_files/pi_digits.txt') as file_object:
    """打开文件句柄，命名别名fiel_object，逐行读取文件"""
    for line in file_object:
        print(line.rstrip())


print('\t')
print('*' * 30)
print('\t')

"""
    创建一个包含文件各行内容的列表
"""
with open('text_files/pi_digits.txt') as file_object:
    """打开文件句柄，命名别名fiel_object，读取文件"""
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())



print('\t')
print('*' * 30)
print('\t')

"""
    使用文件内容
"""
with open('text_files/pi_digits.txt') as file_object:
    """打开文件句柄，命名别名fiel_object，读取文件"""
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))


print('\t')
print('*' * 30)
print('\t')

"""
    包含一百万位的大型文件
"""
with open('text_files/pi_million_digits.txt') as file_object:
    """打开文件句柄，命名别名fiel_object，读取文件"""
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + '...')
print(len(pi_string))

birthday = input("Enter your birthday, in the form mmddyy: ")

if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

