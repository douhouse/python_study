class User():
    '''
    定义一个User()类，里面包含:
        形参: self, first_name, last_name, age, location, name
        方法: describe_user(), greet_user()
    '''
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        # 在这里定义一个名为 name 的形参，它由first_name, ' ', last_name 组成
        self.name = first_name + ' ' + last_name
        self.age = age
        self.location = location
        self.login_attempts = 1


    def describe_user(self):
        print("name: " + self.name.title() + '\n' +
              "age: " + str(self.age) + '\n' +
              "location: " + self.location.title())


    def greet_user(self):
        print("Hello, " + self.name.title())


    def reset_login_attempts(self):
        self.login_attempts = 0


    def increment_login_attempts(self):
        self.login_attempts += 1


class Privileges():
    '''专门处理权限的类'''

    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]
    

    def show_privileges(self):
        print("privileges:")
        for privilege in self.privileges:
            print('-' + privilege)


class Admin(User):
    '''定义一个管理员类名为Admin，继承User类'''

    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        # 在这里定义一个名为 name 的形参，它由first_name, ' ', last_name 组成
        self.name = first_name + ' ' + last_name
        self.age = age
        self.location = location
        self.login_attempts = 1

        self.privileges = Privileges()


my_admin = Admin('zixuan', 'fang', 18, 'dong guan')
my_admin.describe_user()
my_admin.increment_login_attempts()
print(my_admin.login_attempts)
my_admin.privileges.show_privileges()
