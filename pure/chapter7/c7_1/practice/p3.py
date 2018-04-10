num = input("Enter a number, and I'll tell you if the number can be 10 divided evenly.\n")
num = int(num)

if num % 10 == 0:
    print("This number can be 10 divided evenly.")
else:
    print("This number can't be 10 divided evenly.")
