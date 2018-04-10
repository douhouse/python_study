prompt = "Please enter you age: "
current_num = 0
num = 60
active = True

while active:
    age = input(prompt)
    if age.isdigit():   #判断age是否都为数字
        age = int(age)  #如果age都为数字则将age转化为int类型

        if current_num <= num:
            current_num += 1
            if age <= 0:
                print("Are you serious?\n")
            elif age < 3:
                print("free!\n")
            elif age < 12:
                print("10$!\n")
            elif age >= 12:
                print("15$!\n")

        else:
            active = False  #当电影票卖完后提醒观众购买下一个场次的电影票
            print("Full of people! plz try another times")
    elif str(age) != 'quit':    # 输入非纯数字或quit时提示输入错误
        print("oops! try again.\n")
    elif str(age) == 'quit':    #输入quit退出程序
        print("bye!")
