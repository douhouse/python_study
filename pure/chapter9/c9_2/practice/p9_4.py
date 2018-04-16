class Restaurant():
    '''创建一个名为Restaurant的类'''
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_serverd = 0

    def describe_restaurant(self):
        print("restaurant name: " + self.restaurant_name + '\n'
              "cuisine type: " + self.cuisine_type)

    def open_restaurant(self):
        print("We are opening!")


    def set_number_serverd(self, num):
        '''
        设置餐厅服务过的人数，传入一个num，
        若 num 大于 number_serverd 则允许修改，
        否则报错
        '''
        if num > self.number_serverd:
            self.number_serverd = num
            print("This restaurant has serverd " +
                  str(self.number_serverd) + " people!")
        else:
            print("You can't roll back a number serverd!")


    def increment_number_served(self, increment_num):
        '''
        设置餐厅服务人数的增量 increment_num,
        若 increment_num > 0, 则 self.number_serverd 自增
        '''
        if increment_num > 0:
            self.number_serverd += increment_num
        else:
            print("How you shrunk the number?")


restaurant = Restaurant('fzx\'s', 'China meal')

print(restaurant.restaurant_name, restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_serverd(100)
restaurant.increment_number_served(10)
print(restaurant.number_serverd)
