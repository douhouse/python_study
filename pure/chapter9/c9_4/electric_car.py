from car import Car

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
