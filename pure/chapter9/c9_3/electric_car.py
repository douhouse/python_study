class Car():
    '''模拟一个汽车'''


    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 100


    def get_descriptive_name(self):
        '''返回描述性信息'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()


    def read_odometer(self):
        '''打印汽车里程'''
        print("This car has " +
        str(self.odometer_reading) + ' kilometers on it.')


    def update_odometer(self, km):
        '''更改里程表中的值为km'''
        if km > self.odometer_reading:
            self.odometer_reading = km
        else:
            print("You can't roll back an odometer!")


    def increment_odometer(self, km):
        '''增加里程表中的值为km'''
        if km > 0:
            self.odometer_reading += km
        else:
            print("You can't roll back an odometer!")


    def fill_gas_tank():
        print("Gas tank has benn filled")


class ElectricCar(Car):
    '''电动车的不一样的地方'''

    def __init__(self, make, model, year):
        '''
        初始化父类的属性
        再初始化电动汽车的特有属性
        '''
        super().__init__(make, model, year)
        self.battery = Battery()


    def fill_gas_tank():
        print("Electric car doesn't has gas tank!")


class Battery():
    '''电池模拟'''

    def __init__(self, battery_size=70):
        self.battery_size = battery_size


    def describe_battry(self):
        '''打印电池信息'''
        print("battery size is: " + str(self.battery_size))
        

    def get_range(self):
        '''打印一条消息，指出电瓶的续航里程'''
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " kilometers on a fulll charge."
        print(message)


    def upgrade_battery(self):
        '''若电池容量不是85，则升级电池容量至85'''

        if self.battery_size != 85:
            self.battery_size = 85
        else:
            print("Your battery is the top level!")


my_tesela = ElectricCar('tesela', 'model s', '2018')
print(my_tesela.get_descriptive_name())
my_tesela.battery.describe_battry()
my_tesela.battery.get_range()
my_tesela.battery.upgrade_battery()
my_tesela.battery.get_range()
