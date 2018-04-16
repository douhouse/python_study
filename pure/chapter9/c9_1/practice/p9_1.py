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

restaurant = Restaurant('fzx\'s', 'China meal')

print(restaurant.restaurant_name, restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
