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



my_new_car = Car('audi', 'a4', '2018')
print(my_new_car.get_descriptive_name())
my_new_car.increment_odometer(299)
my_new_car.read_odometer()
