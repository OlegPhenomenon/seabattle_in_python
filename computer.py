#Реализую примитивноее ИИ
import random

from ships import Ships

class Computer(Ships):
    def __init__(self, field, enemy_field):
        super().__init__(field)
        self.enemy_field = enemy_field

    #разместим корабль по правилам
    def build_ship(self, x, y, i, field):
        self.flag = False
        for num in range(i):
            if self.x+num <= 9:
                if self.field[x+num][y] == ' ':
                    self.flag = True
                else:
                    self.flag = False
            else:
                self.flag = False
        if self.flag == True:
            for num in range(i):
                self.field[x+num][y] = '#'
            return self.flag

        for num in range(i):
            if self.x - num <= 0:
                if self.field[x-num][y] == ' ':
                    self.flag = True
                else:
                    self.flag = False
            else:
                self.flag = False
        if self.flag == True:
            for num in range(i):
                self.field[x-num][y] = '#'
            return self.flag
        
        for num in range(i):
            if y+num <= 9:
                if self.field[x][y+num] == ' ':
                    self.flag = True
                else:
                    self.flag = False
            else:
                self.flag = False
        if self.flag == True:
            for num in range(i):
                self.field[x][y+num] = '#'
            return self.flag

        for num in range(i):
            if y-num >=0:
                if self.field[x][y-num] == ' ':
                    self.flag = True
                else:
                    self.flag = False
            else:
                self.flag = False
        if self.flag == True:
            for num in range(i):
                self.field[x][y-num] = '#'
            return self.flag
        return self.flag
    
     #разместить 4ех палубный корабль
    def computer_shipx4(self, field):    
        self.flag = False  
        while self.flag == False:
            self.x = random.randint(0, 9)
            self.y = random.randint(0, 9)
            self.flag = super().checks(self.x, self.y) #проверка: в правильной ли ячейке? 
            self.flag = self.build_ship(self.x, self.y, 4, field)
            if self.flag == True:
                break
            
        self.field = super().mark_around_ship(self.field)
        return self.field

     #разместить 3ех палубный корабль
    def computer_shipx3(self, field):    
        self.flag = False  
        while self.flag == False:
            self.x = random.randint(0, 9)
            self.y = random.randint(0, 9)
            self.flag = super().checks(self.x, self.y) #проверка: в правильной ли ячейке? 
            self.flag = self.build_ship(self.x, self.y, 3, field)
            if self.flag == True:
                break
        self.field = super().mark_around_ship(self.field)   
        return self.field

     #разместить 2ух палубный корабль
    def computer_shipx2(self, field):    
        self.flag = False  
        while self.flag == False:
            self.x = random.randint(0, 9)
            self.y = random.randint(0, 9)
            self.flag = super().checks(self.x, self.y) #проверка: в правильной ли ячейке? 
            self.flag = self.build_ship(self.x, self.y, 2, field)
            if self.flag == True:
                break
        self.field = super().mark_around_ship(self.field)    
        return self.field

     #разместить одно- палубный корабль
    def computer_shipx1(self, field):    
        self.flag = False  
        while self.flag == False:
            self.x = random.randint(0, 9)
            self.y = random.randint(0, 9)
            self.flag = super().checks(self.x, self.y) #проверка: в правильной ли ячейке? 
            self.flag = self.build_ship(self.x, self.y, 1, field)
            if self.flag == True:
                break
        self.field = super().mark_around_ship(self.field)    
        return self.field

    def replace_computers_ships(self, field):
        self.computer_shipx4(self.field)

        self.computer_shipx3(self.field)
        self.computer_shipx3(self.field)

        self.computer_shipx2(self.field)
        self.computer_shipx2(self.field)
        self.computer_shipx2(self.field)

        self.computer_shipx1(self.field)
        self.computer_shipx1(self.field)
        self.computer_shipx1(self.field)
        self.computer_shipx1(self.field)
        return self.field
    def computer_shoot(self, enemy_field):
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if self.enemy_field[x][y] == ' ':
                self.enemy_field[x][y] = 'x'
                break
            elif self.enemy_field[x][y] == '#':
                self.enemy_field[x][y] = '@'
            elif self.enemy_field[x][y] == '+':
                self.enemy_field[x][y] = 'x'
            elif self.enemy_field[x][y] == '@':
                self.enemy_field[x][y] = '@'
        return self.enemy_field

    def computer_display(self, field):
        super().display(field)
