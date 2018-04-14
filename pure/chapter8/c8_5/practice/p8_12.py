def get_toppings(*toppings):
    print("You ordered following toppings in your pizza: ")
    for topping in toppings:
        print('-' + topping)

get_toppings('mushroom', 'papper', 'ham')
