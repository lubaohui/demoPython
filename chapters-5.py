

#if语句

cars = ['audi','bmw','subaru','toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

print('\t')

#检查特定值是否包括在列表中
print('bmw' in cars)

#检查特定值是否不包括在列表中
print('bmw' not in cars)


age = 19
if age > 18:
    print('age > 18')
else:
    print('age < 18')


age2 = 20
if age2 < 10:
    print('age2 < 10')
elif age2 > 15:
    print('age2 > 15')
else:
    print('age2 < 20')


#判断列表是否为空
testb = []
if testb:
    print('list is not null!')
else:
    print('list is null!')

