num = input("Enter a number, and I'll tell you all of the odds between 0 and this number")
num = int(num)
current_num = 0

while current_num < num:
    current_num += 1

    if current_num % 2 == 0:
        continue
    else:
        print(current_num)
