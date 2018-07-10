#тут буду создавать и размещать корабли

import random
from field import Field

class Ships(Field):
    #инициализируем кораблики
    def __init__(self, field):
        #super().__init__()
        self.field = field
        self.MARK = '#'
        self.MARK2 = '.'

    #помечаем область вокруг корабля
    def mark_around_ship(self, field):
        for i in range(len(self.field)):
            for j in range(len(self.field)):
                if self.field[i][j] == self.MARK:
                    if i-1 >= 0:
                        if self.field[i-1][j] == ' ':
                            self.field[i-1][j] = self.MARK2
                    if i+1 <= 9:
                        if self.field[i+1][j] == ' ':
                            self.field[i+1][j] = self.MARK2
                    if j+1 <= 9:
                        if self.field[i][j+1] == ' ':
                            self.field[i][j+1] = self.MARK2
                    if j-1 >= 0:
                        if self.field[i][j-1] == ' ':
                            self.field[i][j-1] = self.MARK2
                    if i-1 >= 0 and j+1 <= 9:
                        if self.field[i-1][j+1] == ' ':
                            self.field[i-1][j+1] = self.MARK2
                    if i+1 <= 9 and j-1 >= 0:
                        if self.field[i+1][j-1] == ' ':
                            self.field[i+1][j-1] = self.MARK2
                    if i+1 <= 9 and j+1 <= 9:
                        if self.field[i+1][j+1] == ' ':
                            self.field[i+1][j+1] = self.MARK2
                    if i-1 >= 0 and j-1 >= 0:
                        if self.field[i-1][j-1] == ' ':
                            self.field[i-1][j-1] = self.MARK2
        return self.field
    #размещаем
    def replace(self, x, y):
        self.field[x][y] = self.MARK
        return self.field

    #Не выходит ли за границу
    def check_cell(self, x, y):
        self.flag = False
        while not self.flag:
            if self.x < 0:
                print('Неверный индекс')
                return self.flag
            elif self.x > 9:
                print('Неверный индекс')
                return self.flag
            elif self.y < 0:
                print('Неверный индекс')
                return self.flag
            elif self.y > 9:
                print('Неверный индекс')
                return self.flag
            else:
                self.flag = True
        return self.flag
    #проверка
    def checks(self, x, y):
        if self.field[x][y] == ' ':
            return True
        return False


    def new_checks_temp(self, x, y):
        if self.field[x][y] == '#' or self.field[x][y] == self.MARK2:
            print('Вы пытаетесь построить корабль поверх другого или близко к нему')
            return False
        return True

    #проверим, не разбит ли цельный корабль на разные части по разных не идущим друг за другом
    #ячейкам
    def line_ship(self, x, y):
        if x-1 >=0:
            if self.field[x-1][y] == self.MARK:
                return True
        if x+1 <= 9:
            if self.field[x+1][y] == self.MARK:
                return True
        if y+1 <= 9:
            if self.field[x][y+1] == self.MARK:
                return True
        if y-1 >= 0:
            if self.field[x][y-1] == self.MARK:
                return True
        return False
    
    #разместить 4ех палубный корабль
    def shipx4(self, field):    
        self.i = 0
        self.flag = True #Флаг корректной ячейке
        self.flag2 = True #Флаг целостности корабля
        self.flag3 = True #Флаг корректности ячейке 3
        self.flag4 = True #Флаг повверх ли строится корабль?
        while self.i<1: #тут вставим первую палубу произведя необходимые проверки
            self.x = int(input('x: '))
            self.y = int(input('y: '))
            if self.x < 0 or self.x > 9:
                print('Цифра выходит за пределы поля. Введите вновь координаты от 0 до 9.')
                continue
            if self.y < 0 or self.y > 9:
                print('Цифра выходит за пределы поля. Введите вновь координаты от 0 до 9.')
                continue
            self.flag = self.checks(self.x, self.y) #в "нормальной" ли ячейче?!
            self.flag3 = self.check_cell(self.x, self.y)
            self.flag4 = self.new_checks_temp(self.x, self.y)
            if self.flag == True and self.flag3 == True and self.flag4 == True:
                self.field = self.replace(self.x, self.y) #если все хорошо разместим в field[x][y]
                self.i += 1     #увеличим инкремент, чтобы выйти из цикла
            else:
                print('Неправильно. Попробуйте еще раз')
        #тут мы будет размещать дальнейшие палубы, есдинственное, что 
        #добавил, это проверку на целостность корабля
        while self.i < 4:   
            self.x = int(input('x: '))
            self.y = int(input('y: '))
            if self.x < 0 or self.x > 9:
                print('Цифра выходит за пределы поля. Введите вновь координаты от 0 до 9.')
                continue
            if self.y < 0 or self.y > 9:
                print('Цифра выходит за пределы поля. Введите вновь координаты от 0 до 9.')
                continue
            self.flag = self.checks(self.x, self.y)
            self.flag2 = self.line_ship(self.x, self.y) #проверка на целостность
            self.flag3 = self.check_cell(self.x, self.y)
            self.flag4 = self.new_checks_temp(self.x, self.y)
            if self.flag == True and self.flag2 == True and self.flag3 == True and self.flag4 == True:
                self.field = self.replace(self.x, self.y)
                self.i += 1
            else:
                print('Неправильно. Попробуйте еще раз')
        return self.field

     #разместить 3ех палубный корабль
    def shipx3(self, field):    
        self.i = 0
        self.flag = True #Флаг корректной ячейке
        self.flag2 = True #Флаг целостности корабля
        self.flag3 = True #Флаг корректности ячейке 3
        self.flag4 = True
        while self.i<1: #тут вставим первую палубу произведя необходимые проверки
            self.x = int(input('x: '))
            self.y = int(input('y: '))
            if self.x < 0 or self.x > 9:
                print('Цифра выходит за пределы поля. Введите вновь координаты от 0 до 9.')
                continue
            if self.y < 0 or self.y > 9:
                print('Цифра выходит за пределы поля. Введите вновь координаты от 0 до 9.')
                continue
            self.flag = self.checks(self.x, self.y) #в "нормальной" ли ячейче?!
            self.flag3 = self.check_cell(self.x, self.y)
            self.flag4 = self.new_checks_temp(self.x, self.y)
            if self.flag == True and self.flag3 == True and self.flag4 == True:
                self.field = self.replace(self.x, self.y) #если все хорошо разместим в field[x][y]
                self.i += 1     #увеличим инкремент, чтобы выйти из цикла
            else:
                print('Неправильно. Попробуйте еще раз')
        #тут мы будет размещать дальнейшие палубы, есдинственное, что 
        #добавил, это проверку на целостность корабля
        while self.i < 3:   
            self.x = int(input('x: '))
            self.y = int(input('y: '))
            if self.x < 0 or self.x > 9:
                print('Цифра выходит за пределы поля. Введите вновь координаты от 0 до 9.')
                continue
            if self.y < 0 or self.y > 9:
                print('Цифра выходит за пределы поля. Введите вновь координаты от 0 до 9.')
                continue
            self.flag = self.checks(self.x, self.y)
            self.flag2 = self.line_ship(self.x, self.y) #проверка на целостность
            self.flag3 = self.check_cell(self.x, self.y)
            self.flag4 = self.new_checks_temp(self.x, self.y)
            if self.flag == True and self.flag2 == True and self.flag3 == True and self.flag4 == True:
                self.field = self.replace(self.x, self.y)
                self.i += 1
            else:
                print('Неправильно. Попробуйте еще раз')
        return self.field

     #разместить 2ух палубный корабль
    def shipx2(self, field):    
        self.i = 0
        self.flag = True #Флаг корректной ячейке
        self.flag2 = True #Флаг целостности корабля
        self.flag3 = True #Флаг корректности ячейке 3
        self.flag4 = True
        while self.i<1: #тут вставим первую палубу произведя необходимые проверки
            self.x = int(input('x: '))
            self.y = int(input('y: '))
            if self.x < 0 or self.x > 9:
                print('Цифра выходит за пределы поля. Введите вновь координаты от 0 до 9.')
                continue
            if self.y < 0 or self.y > 9:
                print('Цифра выходит за пределы поля. Введите вновь координаты от 0 до 9.')
                continue
            self.flag = self.checks(self.x, self.y) #в "нормальной" ли ячейче?!
            self.flag3 = self.check_cell(self.x, self.y)
            self.flag4 = self.new_checks_temp(self.x, self.y)
            if self.flag == True and self.flag3 == True and self.flag4 == True:
                self.field = self.replace(self.x, self.y) #если все хорошо разместим в field[x][y]
                self.i += 1     #увеличим инкремент, чтобы выйти из цикла
            else:
                print('Неправильно. Попробуйте еще раз')
        #тут мы будет размещать дальнейшие палубы, есдинственное, что 
        #добавил, это проверку на целостность корабля
        while self.i < 2:   
            self.x = int(input('x: '))
            self.y = int(input('y: '))
            if self.x < 0 or self.x > 9:
                print('Цифра выходит за пределы поля. Введите вновь координаты от 0 до 9.')
                continue
            if self.y < 0 or self.y > 9:
                print('Цифра выходит за пределы поля. Введите вновь координаты от 0 до 9.')
                continue
            self.flag = self.checks(self.x, self.y)
            self.flag2 = self.line_ship(self.x, self.y) #проверка на целостность
            self.flag3 = self.check_cell(self.x, self.y)
            self.flag4 = self.new_checks_temp(self.x, self.y)
            if self.flag == True and self.flag2 == True and self.flag3 == True and self.flag4 == True:
                self.field = self.replace(self.x, self.y)
                self.i += 1
            else:
                print('Неправильно. Попробуйте еще раз')
        return self.field

     #разместить одно- палубный корабль
    def shipx1(self, field):    
        self.i = 0
        self.flag = True #Флаг корректной ячейке
        self.flag2 = True #Флаг целостности корабля
        self.flag3 = True #Флаг корректности ячейке 3
        self.flag4 = True
        while self.i<1: #тут вставим первую палубу произведя необходимые проверки
            self.x = int(input('x: '))
            self.y = int(input('y: '))
            if self.x < 0 or self.x > 9:
                print('Цифра выходит за пределы поля. Введите вновь координаты от 0 до 9.')
                continue
            if self.y < 0 or self.y > 9:
                print('Цифра выходит за пределы поля. Введите вновь координаты от 0 до 9.')
                continue
            self.flag = self.checks(self.x, self.y) #в "нормальной" ли ячейче?!
            self.flag3 = self.check_cell(self.x, self.y)
            self.flag4 = self.new_checks_temp(self.x, self.y)
            if self.flag == True and self.flag3 == True and self.flag4 == True:
                self.field = self.replace(self.x, self.y) #если все хорошо разместим в field[x][y]
                self.i += 1     #увеличим инкремент, чтобы выйти из цикла
            else:
                print('Неправильно. Попробуйте еще раз')
        return self.field

    
