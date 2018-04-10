respone = {}

polling_active = True

while polling_active: # flag
    name = input("What's your name?\n")
    vacationland = input("\nWhere would you like to go in your holiday?\n")

    respone[name] = vacationland # 定义一个字典的新方法

    repeat = input("Would u like to let another person respond? (y/n)")
    if repeat == 'n':
        polling_active = False

print("\n---- Poll Result ----")
for name, vacationland in respone.items():
    print(name.title() + " would like go to " + vacationland.title())
