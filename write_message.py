print('\t')
print('*' * 30)
print('\t')
file_path = 'text_files/write_messages.txt'
"""
    写入空文件
"""
with open(file_path,'w') as file_object:
    """打开文件句柄，命名别名fiel_object，写入文件"""
    file_object.write('我爱编程。')

print('\t')
print('*' * 30)
print('\t')

"""
    写入多行
"""
with open(file_path,'w') as file_object:
    """打开文件句柄，命名别名fiel_object，写入文件"""
    file_object.write('我爱编程。\n')
    file_object.write('我爱小说。\n')


print('\t')
print('*' * 30)
print('\t')

"""
    追加文件
"""
with open(file_path,'a') as file_object:
    """打开文件句柄，命名别名fiel_object，写入文件"""
    file_object.write('我爱看电影。\n')
    file_object.write('我爱篮球。\n')



