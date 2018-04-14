def make_pizza(size, *toppings):
    '''打印顾客点的所有配料'''
    print("Making a " + str(size) + "-inch pizza with following toppings: ")
    for topping in toppings:
        print('-' + topping)

make_pizza(13, 'fff', 'fffff', 'sdsddfs')
