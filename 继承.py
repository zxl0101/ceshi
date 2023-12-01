class Animal:
    def __init__(self,name="动物") -> None:
        self.name=name
    def eat(self):
        print(self.name,"吃")

    def sleep(self):
        print(self.name,"睡")

#类名后面的（）表示继承，里的类代表是父类
class Dog(Animal):
    def run(self):  # 扩展
        print(self.name,"跑")
class ErHa(Dog):
    def maimeng(self):
        print(self.name,"卖萌")

d = Dog("大黄")
d.eat()
d.sleep()
d.run()
c =ErHa()
c.maimeng()
c.eat()
c.run()