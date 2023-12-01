class Women:
    def __init__(self, name, weight) -> None:
        self.name = name
        # 私有属性，只能类内部访问
        self.__weight = weight

    def show_info(self):
        print(f"姓名：{self.name},体重保密")

    def __eat(self):
        self.__weight + 1


w = Women("lucy", 150)
w.show_info()
#w.__eat() 不能在类的外部调用私有方法