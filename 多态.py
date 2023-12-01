class Animal:
    def food(self):
        pass

    def eat(self):
        self.food()


class Dog(Animal):
    def food(self):
        print("吃肉")


class Cattle(Animal):
    def food(self):
        print("吃草")

#实例化一个dog
a = Dog()
#调用了dog里的food（）方法：吃肉
a.eat()
#实例化一个cattle
b=Cattle()
#调用的是cattle里的food（）方法：吃草
b.eat()