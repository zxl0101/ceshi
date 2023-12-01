class father:
    def __init__(self) :
        self.__name = "张三"
        self.house = "别墅"

    def eat(self):
        print("吃")

    def sleep(self):
        print("睡")

    def __edu__back(self):
        print("本科")


class son(father):
    def show_eat(self):
        self.eat()

    def show_sleep(self):
        self.sleep()

    def show_house(self):
        print(self.house)
s=son()
s.show_eat()
s.show_house()
s.show_sleep()
