prompt = "What do you want?\n"
active = True

while active:
    pizza_toppings = input(prompt)
    if pizza_toppings == 'quit':
        active = False
    elif pizza_toppings != 'quit':
        print("\nThe " + pizza_toppings.title() + " was appended!\n")
