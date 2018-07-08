# В этом модуле я делаю игровое поле
class Field():
    #размер поля 10x10
    n = 10
    m = 10
    #инициализируем двойной массив в качестве 10x10 поля, добавляя в каждую ячейку 
    #пробельный символ
    def __init__(self):
        self.field = [[0]*self.m for i in range(self.n)]
        for x in range(len(self.field)):
            for y in range(len(self.field)):
                self.field[x][y] = ' '
    #отображаем поле#
    def display(self, field):
        for items in self.field:
            print(items)
    
