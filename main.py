class Parent:
    def __init__(self, общий_атрибут):
        self.общий_атрибут = общий_атрибут

    def общий_метод(self):
        print("Это общий метод")

class Son(Parent):
    def __init__(self, общий_атрибут, уникальный_атрибут):
        self.уникальный_атрибут = уникальный_атрибут

    def уникальный_метод1(self):
        print("Это уникальный метод из class Son")

class Son2(Parent):
    def __init__(self, общий_атрибут, уникальный_атрибут2):
        self.уникальный_атрибут2 = уникальный_атрибут2

    def уникальный_метод2(self):
        print("Это уникальный метод из class Son2")

# Использование классов
родитель = Parent("Общий атрибут родителя")
родитель.общий_метод()

son1 = Son("Общий атрибут дочери 1", "Уникальный атрибут дочери 1")
son1.общий_метод()
son1.уникальный_метод1()

son2 =Son2("Общий атрибут дочери 2", "Уникальный атрибут дочери 2")
son2.общий_метод()
son2.уникальный_метод2()
