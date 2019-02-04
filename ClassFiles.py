
class CocaCola:
    formula = ['caffeine','sugar','water','soda']

#类实例化
coke_for_me = CocaCola()
coke_for_you = CocaCola()

print(CocaCola.formula)
print(coke_for_me.formula)
print(coke_for_you.formula)

for element in coke_for_me.formula:
    print(element)


coke_for_China = CocaCola()
#创建实例属性
coke_for_China.local_logo = '可口可乐'

print(coke_for_China.local_logo)


class CocaCola:
    formula = ['caffeine','sugar','water','soda']
    def drink(self):
        print('Energy!')
coke = CocaCola()
coke.drink()


class CocaCola:
    formula = ['caffeine','sugar','water','soda']
    def drink(self,how_much):
        if how_much == 'a sip':
            print('Cool~')
        elif how_much == 'whole bottle':
            print('Headache!')
ice_coke = CocaCola()
ice_coke.drink('whole bottle')


class CocaCola():
    formula = ['caffeine','sugar','water','soda']
    def __init__(self):
        self.local_logo = '可口可乐'
    def drink(self):
        print('Energy!')

coke = CocaCola()
print(coke.local_logo)



class CocaCola:
    formula = ['caffeine','sugar','water','soda']
    def __init__(self):
        for element in self.formula:
            print('Coke has {}!'.format(element))
    def drink(self):
        print('Energy!')
coke = CocaCola()

class CocaCola:
    formula = ['caffeine','sugar','water','soda']
    def __init__(self,logo_name):
        self.local_logo = logo_name
    def drink(self):
        print('Energy!')
coke = CocaCola('可口可乐')
print(coke.local_logo)


class CocaCola:
    calories    = 140
    sodium      = 45
    total_carb  = 39
    caffeine    = 34
    ingredients =  [
        'High Fructose Corn Syrup',
        'Carbonated Water',
        'Phosphoric Acid',
        'Natural Flavors',
        'Caramel Color',
        'Caffeine' ]
    def __init__(self,logo_name):
        self.local_logo = logo_name
    def drink(self):
        print('You got {} cal energy!'.format(self.calories))

#类的继承
class CaffeineFree(CocaCola):
    caffeine = 0
    ingredients =  [
        'High Fructose Corn Syrup',
        'Carbonated Water',
        'Phosphoric Acid',
        'Natural Flavors',
        'Caramel Color',
    ]
coke_a = CaffeineFree('Cocacola-FREE')
coke_a.drink()


class TestA:
    attr = 1
obj_a = TestA()
TestA.attr = 42
print(obj_a.attr)


class TestA:
    attr = 1
obj_a = TestA()
obj_b = TestA()
obj_a.attr = 42
print(obj_b.attr)


class TestA:
    attr = 1
    def __init__(self):
        self.attr = 42
obj_a = TestA()
print(obj_a.attr)
#多行注释
''' 
对对对
'''

name = 'ada loveabao'
print(name.title())


print('\tPython')

print('Python\njava')

spt = ' Python '
print(spt.strip())

age = 23
message = 'Happy ' + str(age) + 'rd Birthday'
print(message)

#范围
for value in range(1,5):
    print(value)

#数字列表
numbers = list(range(1,6))
print(numbers)

#乘方运算
squares = []
for value in range(1,11):
    #square = value ** 2
    #squares.append(square)
    squares.append(value ** 2)
print(squares)

print(min(squares))
print(max(squares))
print(sum(squares))

squares2 = [value ** 2 for value in range(1,11)]

print(squares2)


squares3 = [value ** 3 for value in range(1,11)]

print(squares3)


squares4 = [value for value in range(1,11) if value%2 != 0 ]

print(squares4)

#切片
print(squares[0:5])


print(squares[:5])


print(squares[2:])

#遍历切片
for value in squares[2:]:
    print(value)

#复制列表
squares5 = squares4
print(squares5)

squares6 = squares4[:]
print(squares6)



