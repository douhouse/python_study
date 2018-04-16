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

    def describe_user(self):
        print("name: " + self.name.title() + '\n' +
              "age: " + str(self.age) + '\n' +
              "location: " + self.location.title())

    def greet_user(self):
        print("Hello, " + self.name.title())

fzx = User('zixuan', 'fang', 22, 'dong guan')
fzx.describe_user()
fzx.greet_user()
