def get_name():
    while True:
        print("Please enter your name: ")
        print("(enter 'q' at any time to quit)")
        f_name = input("\nfirst name: ")
        if f_name == 'q':
            break
        l_name = input("last name: ")
        if l_name == 'q':
            break

        full_name = get_fomatted_name(f_name, l_name)
        print("hello " + full_name + '\n')


def get_fomatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()


get_name()
