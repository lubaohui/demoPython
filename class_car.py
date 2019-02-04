
#定义类
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值"""
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """汽车有油箱"""
        print("汽车有油箱!")

#创建类的实例
my_new_car = Car('audi', 'a4', 2016)

print(my_new_car.get_descriptive_name())

#直接修改属性的值
my_new_car.odometer_reading = 23

#通过方法修改属性值
my_new_car.update_odometer(30)

#通过方法对属性的值进行递增
my_new_car.increment_odometer(10)

my_new_car.read_odometer()

print('\t')
print('*' * 30)
print('\t')

#继承

class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        """电动汽车的独特之处 初始化父类的属性，再初始化电动汽车特有的属性 """


#初始化子类
my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())


print('\t')
print('*' * 30)
print('\t')
"""
    定义子类的属性和方法
"""
class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)

        """再初始化电动汽车特有的属性 """
        self.battery_size = 70

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print("电动汽车没有油箱")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

#调用重写的父类方法
my_tesla.fill_gas_tank()



print('\t')
print('*' * 30)
print('\t')

"""
    将实例作为类的属性
"""
class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """ 初始化父类的属性，再初始化电动汽车特有的属性 """
        super().__init__(make, model, year)

        #实例作为类的属性
        self.battery = Battery(80)


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()



