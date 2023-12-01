class Animal:
    # 类属性
    name = "动物"

    # 这个方法一个类方法：
    @classmethod
    def show_info(cls):
        print(cls.name)
        # 类方法中不能调用普通方法
        # cls.hello()
        cls.world()

    @classmethod
    def world(self):
        print("world")

    @staticmethod
    def sm(cls):
        #这个参数cls不是类本身，他是一个普通参数
        #print(cls.name)
        print("这是静态方法")

    def hello(self):
        print("hello")


# 调用类方法：
Animal.show_info()
Animal.sm("xxx")
