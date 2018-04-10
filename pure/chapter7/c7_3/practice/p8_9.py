sandwich_orders = ['pastrami', 'pastrami', 'pastrami', 'tuna sandwich', 'beef sandwich', 'tomato sandwich']
finished_sandwiches = []

print("pastrami was sold out")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made you a " + sandwich)

    finished_sandwiches.append(sandwich)
    
print(finished_sandwiches)
