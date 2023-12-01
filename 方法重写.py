class Animal:
    def __init__(self,name="动物") -> None:
        self.name=name
    def eat(self):
        print(self.name,"吃")

    def sleep(self):
        print(self.name,"睡")

#类名后面的（）表示继承，里的类代表是父类
class Dog(Animal):
    #方法声明完全一样，只是实现不一样
    def eat(self):
        super().eat() #在父类基础上增加功能
        print(self.name,"吃肉")
    def run(self):  # 扩展
        print(self.name,"跑")


d = Dog("诺基")
#当子类重写了父类方法后，会调子类的方法，不再调用父类的方法了
d.eat()
d.sleep()
d.run()
