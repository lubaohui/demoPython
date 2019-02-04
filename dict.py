NASDAQ_code = {
    'BIDU':'Baidu',
    'SINA':'Sina',
    'YOKU':'Youku'
}


print(NASDAQ_code)

#key_test = {[]: 'a Test'}
#print(key_test)

a = {'key': 123, 'key': 123}
print(a)

NASDAQ_code['YOKU2'] = 'Youku2'
print(NASDAQ_code)

NASDAQ_code.update({'FB':'Facebook','TSLA':'Tesla'})
print(NASDAQ_code)

del NASDAQ_code['FB']
print(NASDAQ_code)

letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
print(letters[0])



a_set = {1,2,3,4}
print(a_set)
a_set.add(5)
print(a_set)
a_set.discard(5)
print(a_set)

num_list = [6, 2, 7, 4, 1, 3, 5]
print(sorted(num_list))
#reverse按照逆序排序
print(sorted(num_list,reverse=True))

#列表推导式
a = []
for i in range(1,11):
    a.append(i)
print(a)

b = [i for i in range(1,11)]
print(b)

import time


a = []
t0 = time.clock()
for i in range(1,20000):
    a.append(i)
print(time.clock() - t0, "seconds process time")
t0 = time.clock()
b = [i for i in range(1,20000)]
print(time.clock() - t0, "seconds process time")

a = [i**2 for i in range(1,10)]
print(a)
c = [j+1 for j in range(1,10)]
print(c)
k = [n for n in range(1,10) if n % 2 ==0]
print(k)
z = [letter.lower() for letter in 'ABCDEFGHIGKLMN']
print(z)

#字典的推导式
d = {i:i+1 for i in range(4)}
print(d)
g = {i:j for i,j in zip(range(1,6),'abcde')}
print(g)
f= {i+1:j.upper() for i,j in zip(range(1,6),'abcde')}
print(f)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for num,letter in enumerate(letters):
    print(letter,'is',num + 1)


#字典
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])


favorite_languages = { 'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}

print("Sarah's favorite language is " + favorite_languages['sarah'].title() +  ".")

#遍历所有字典的键值对

for key, value in alien_0.items():
    print('\nKey: ' + key)
    print('Value: ' + str(value))

#遍历字典所有的键
for key in favorite_languages.keys():
    print('\nKey: ' + key)

print('*' * 20)
#按照顺序遍历字典所有的键
for key in sorted(favorite_languages.keys()):
    print('\nKey: ' + key)


print('*' * 20)
#按照顺序遍历字典所有的值
for value in sorted(favorite_languages.values()):
    print('\nValue: ' + value.title())

print('*' * 20)
#剔除🍚值
for value in set(favorite_languages.values()):
    print('\nValue: ' + value.title())


print('*' * 20)

#列表字典嵌套
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)


print('*' * 20)
#字典嵌套列表

#存储所点比萨的信息
pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'], }
# 概述所点的比萨
print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languages = {
    'jen': ['python', 'ruby'], 'sarah': ['c'],
    'edward': ['ruby', 'go'], 'phil': ['python', 'haskell'],}
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")

    for language in languages:
        print("\t" + language.title())

#字典嵌套字典
users = { 'aeinstein': {
'first': 'albert', 'last': 'einstein', 'location': 'princeton', },
'mcurie': {
'first': 'marie', 'last': 'curie', 'location': 'paris', },
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())



