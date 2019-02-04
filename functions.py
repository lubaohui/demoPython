
#定义函数

def greet_user():
    print('Hello!')

#函数调用
greet_user()

#向函数传递信息
def greet_user(username):
    print('Hello，' + username.title() + '！')

greet_user('abao')


def describe_pet(animal_type, pet_name):
    '''显示宠物的信息'''
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

#位置实参
describe_pet('harry', 'hamster')

#关键字实参 无需考虑实参的顺序
describe_pet(animal_type='hamster', pet_name='harry')


describe_pet( pet_name='harry', animal_type='hamster')

#默认值
def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')

print('\t')
print('*' * 30)
print('\t')

#返回简单值
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')

print(musician)

print('\t')
print('*' * 30)
print('\t')

#返回字典 可返回任何负责的数据结构
def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

print('\t')
print('*' * 30)
print('\t')

#传递列表参数
def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']

greet_users(usernames)

print('\t')
print('*' * 30)
print('\t')


# 首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# 模拟打印每个设计，直到没有未打印的设计为止
# 打印每个设计后，都将其移到列表completed_models中
while unprinted_designs:
    current_design = unprinted_designs.pop()

    #模拟根据设计制作3D打印模型的过程
    print("Printing model: " + current_design)
    completed_models.append(current_design)

# 显示打印好的所有模型
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

print(unprinted_designs)


print('\t')
print('*' * 30)
print('\t')

#改写函数模式
def print_models(unprinted_designs, completed_models):
    """模拟打印每个设计，直到没有未打印的设计为止 打印每个设计后，都将其移到列表completed_models中 """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # 模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

print(unprinted_designs)

print('\t')
print('*' * 30)
print('\t')

#禁止函数修改列表 向函数传递列表副本，不传递列表原价


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)


print('\t')
print('*' * 30)
print('\t')
#任意数量的实参
def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print("\nMaking a pizza with the following toppings:")
    print(toppings)

    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


print('\t')
print('*' * 30)
print('\t')

#结合使用位置实参和任意数量实参
def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

print('\t')
print('*' * 30)
print('\t')

#使用任意数量的关键字实参

def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location='princeton',field='physics')
print(user_profile)



