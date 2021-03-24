'''
Реализуйте класс MoneyBox, для работы с виртуальной копилкой.

Каждая копилка имеет ограниченную вместимость, которая выражается целым числом – количеством монет,
которые можно положить в копилку. Класс должен поддерживать информацию о количестве монет в копилке,
предоставлять возможность добавлять монеты в копилку и узнавать, можно ли добавить в копилку ещё какое-то
количество монет, не превышая ее вместимость.



'''

class MoneyBox():
    def __init__(self, capacity):
        self.capacity = capacity
        self.ammount = 0

    def can_add(self, v):
        if (self.ammount + v) <= self.capacity:
            return True
        else:
            return False

    def add(self, v):
        if self.can_add(v):
            self.ammount += v
        else:
            return print(self.capacity - self.ammount)


box1 = MoneyBox(15)
box1.add(5)
box1.add(9)
box1.add(3)

