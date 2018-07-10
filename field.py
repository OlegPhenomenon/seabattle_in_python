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

    #Статическая функция, которая проверяет условие победы
    @staticmethod
    def check_to_victory(field):
        for x in range(len(field)):
            for y in range(len(field)):
                if field[x][y] == '#':
                    return False
        return True

    #Копирует с поля компьютера в пустое поле подбитые корабли и упавшие снаряды
    @staticmethod
    def field_to_battle_field(field, battle_field):
        for x in range(len(field)):
            for y in range(len(field)):
                if field[x][y] == '@':
                    battle_field[x][y] = '@'
                if field[x][y] == 'x':
                    battle_field[x][y] = 'x'
        return battle_field

    #отображает поле
    @staticmethod
    def display(battle_field):
        for item in battle_field:
            print(item)
        print("\n\n")
