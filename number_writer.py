import json
numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'

with open(filename, 'w') as f_obj:
    """json.dump存储数据至json文件中"""
    json.dump(numbers, f_obj)


print('\t')
print('*' * 30)
print('\t')




