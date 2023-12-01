class Animal:
    name = "动物"

    def show_info(self):
        print(self.name)
# 实例化对象
# animal=Animal()


# 获取类属性值：语法：类名.类属性名
n = Animal.name
print(n, "=", n)
Animal.name = "原始动物"
print(n, "=", Animal.name)
#通过类名访问一个普通方法会出现：TypeError: show_info() missing 1 required positional argument: 'self'
#Animal.show_info()
#a=Animal
#a.show_info()
