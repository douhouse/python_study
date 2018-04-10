responses = {}

polling_active = True

while polling_active:
    name = input("\n What's your name?")
    response = input("Which mountain would you like to climb someday?")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (y/n)")
    if repeat == 'n':
        polling_active = False

print("\n--- Poll Results ---")
for name, respone in responses.items():
    print(name + " like to climb " + respone.title())
