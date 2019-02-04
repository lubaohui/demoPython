#coding:utf-8

import random

what_he_does = ' plays '
his_instrument = 'guitar'
his_name = 'Robert Johnson'
artist_intro = his_name + what_he_does + his_instrument
print(artist_intro)

num = 1
string = '1'
num2 = int(string)
print(num + num2)


words = 'words' * 3
print(words)

word = 'a loooooong word'
num = 12
string = 'bang!'
total = string * (len(word) - num) #      'bang!'*4 print(total)
print(total)


name = 'My name is Mike'
print(len(name))

print(name[0])

print(name[-4])

print(name[11:14])


print(name[11:15])

print(name[5:])

print(name[:5])


word = 'friends'
find_the_evil_in_your_friends = word[0]+word[2:4]+word[-3:-1]
print(find_the_evil_in_your_friends)


url = 'http://ww1.site.cn/14d2e8ejw1exjogbxdxhj20ci0kuwex.jpg'
file_name = url[-10:]
print(file_name)

phone_number = '1386-666-0006'
hiding_number = phone_number.replace(phone_number[:9],'*' * 9)
print(hiding_number)

search = '168'
num_a = '1386-168-0006'
num_b = '1681-222-0006'

print(search + ' is at ' + str(num_a.find(search)) + ' to ' + str(num_a.find(search) + len(search)) + ' of num_a')
print(search + ' is at ' + str(num_b.find(search)) + ' to ' + str(num_b.find(search) + len(search)) + ' of num_b')

print('{} a word she can get what she {} for.'.format('With', 'came'))
print('{preposition} a word she can get what she {verb} for'.format(preposition='With', verb='came'))
print('{0} a word she can get what she {1} for.'.format('With', 'came'))

city = 'shh'#input("write down the name of city:")
url = "http://apistore.baidu.com/microservice/weather?citypinyin={}".format(city)
print(url)


def abc():

    return 'hello Function!'

print(abc())




def fahrenheit_converter(C):
    fahrenheit = C * 9/5 + 32
    return str(fahrenheit) + ' ̊F'

print(fahrenheit_converter(42))

lyric_length = len('I Cry Out For Magic!')
print(lyric_length)

#梯形面积
def trapezoid_area(base_up, base_down, height):
    return 1 / 2 * (base_up + base_down) * height

#位置参数
print(trapezoid_area(1,2,3))

#关键词参数
print(trapezoid_area(base_up=1, base_down=2, height=3))


print(trapezoid_area(height=3, base_down=2, base_up=1))

#print(trapezoid_area(height=3, base_down=2, 1))

#print(trapezoid_area(base_up=1,base_down=2,3))

print(trapezoid_area(1, 2, height=3))


print('   *','  * *',' * * *','   |',sep='\n')

#列表
album = ['Black Star','David Bowie',25,True]

album.append('new song')

print(album[0],album[-1])

print('Black Star' in album)

print('false' not in album)

the_Eddie = 'Eddie'
name = 'Eddie'

print(the_Eddie == name)

print(the_Eddie is name)



def account_login():
    password = input('Password:')
    if password == '12345':
        print('Login success!')
    else:
        print('Wrong password or invalid input!')
        account_login()

#account_login()

password_list = ['*#*#','12345']

def account_login():
    password = input('Password:')
    password_correct = password == password_list[-1]
    password_reset = password == password_list[0]
    if password_correct:
        print('Login success!')
    elif password_reset:
        new_password = input('Enter a new password:')
        password_list.append(new_password)
        print('Your password has changed successfully!')
        account_login()
    else:
        print('Wrong password or invalid input!')
        account_login()

#account_login()

for every_letter in 'Hello world':
    print(every_letter)


for num in range(1,11):
    print(str(num) + ' + 1 =',num + 1)

for i in range(1,10):
    for j in range(1,10):
        print('{} X {} = {}'.format(i,j,i*j))


a_list = [1,2,3]
print(sum(a_list))



point1 = random.randrange(1,7)
point2 = random.randrange(1,7)
point3 = random.randrange(1,7)


print(point1,point2,point3)

Weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(Weekday[0])

print(Weekday)


all_in_list = [
1, #
1.0, #
'a word', #
print(1), #
True, #
[1,2], #
(1,2), #
{'key':'value'}
]

print(all_in_list)


fruit = ['pineapple','pear']
fruit.insert(1,'grape')
print(fruit)

fruit[0:0] = ['Orange']
print(fruit)


fruit.remove('grape')
print(fruit)

fruit[0] = 'Grapefruit'
print(fruit)

del fruit[0:2]
print(fruit)


periodic_table = ['H','He','Li','Be','B','C','N','O','F','Ne']
print(periodic_table[0])
print(periodic_table[-2])
print(periodic_table[0:3])
print(periodic_table[-10:-7])
print(periodic_table[-10:])
print(periodic_table[:9])


NASDAQ_code = {
    'BIDU':'Baidu',
    'SINA':'Sina',
    'YOKU':'Youku'
}