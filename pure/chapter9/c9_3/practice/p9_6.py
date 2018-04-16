class Restaurant():
    '''创建一个名为Restaurant的类'''

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("restaurant name: " + self.restaurant_name + '\n'
              "cuisine type: " + self.cuisine_type)

    def open_restaurant(self):
        print("We are opening!")


class IceCreamStand(Restaurant):
    '''模拟冰激凌店'''

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.flavors = ['strawberry', 'chocolate', 'banana']


    def show_flavors(self):
        print("Here are the flavor you can choice:")
        for flavor in self.flavors:
            print('-' + flavor)


my_icecream_stand = IceCreamStand('fzx\'s', 'ice cream')
my_icecream_stand.describe_restaurant()
my_icecream_stand.open_restaurant()
my_icecream_stand.show_flavors()
