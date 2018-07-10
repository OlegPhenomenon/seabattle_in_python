from ships import Ships
from field import Field

   
class Man(Ships):
    def __init__(self, field, enemy_field):
        super().__init__(field)
        self.enemy_field = enemy_field
    #метода размещения кораблей
    def replaceX4(self, field):
        print('x4 палубный корабль')
        self.field = super().shipx4(self.field)
        self.field = super().mark_around_ship(self.field)
        return self.field
    def replaceX3(self, field):
        print('x3 палубный корабль')
        self.field = super().shipx3(self.field)
        self.field = super().mark_around_ship(self.field)
        return self.field
    def replaceX2(self, field):
        print('x2 палубный корабль')
        self.field = super().shipx2(self.field)
        self.field = super().mark_around_ship(self.field)
        return self.field
    def replaceX1(self, field):
        print('x1 палубный корабль')
        self.field = super().shipx1(self.field)
        self.field = super().mark_around_ship(self.field)
        return self.field

    def replace_ships(self, field):
        self.field = self.replaceX4(self.field)
        print('4ех палубный')
        self.display(self.field)

        self.field = self.replaceX3(self.field)
        print('3ех палубный')
        self.display(self.field)
        self.field = self.replaceX3(self.field)
        print('3ех палубный')
        self.display(self.field)

        self.field = self.replaceX2(self.field)
        print('2х палубный')
        self.display(self.field)
        self.field = self.replaceX2(self.field)
        print('2х палубный')
        self.display(self.field)
        self.field = self.replaceX2(self.field)
        print('2х палубный')
        self.display(self.field)

        self.field = self.replaceX1(self.field)
        print('1- палубный')
        self.display(self.field)
        self.field = self.replaceX1(self.field)
        print('1- палубный')
        self.display(self.field)
        self.field = self.replaceX1(self.field)
        print('1- палубный')
        self.display(self.field)
        self.field = self.replaceX1(self.field)
        print('1- палубный')
        self.display(self.field)

        return self.field

    #выстрел
    def shoot(self, enemy_field):
        while True:
            x = int(input("x: "))
            y = int(input("y: "))
            if self.enemy_field[x][y] == self.MARK:
                self.enemy_field[x][y] = '@'
            elif self.enemy_field[x][y] == '@':
                self.enemy_field[x][y] = '@'
            else:
                self.enemy_field[x][y] = 'x'
            break
        
        return self.enemy_field


