from field import Field
from user import Man
from computer import Computer

#размер поля 10x10
n = 10
m = 10
#инициализируем двойной массив в качестве 10x10 поля, добавляя в каждую ячейку 
#пробельный символ
USER_FIELD = [[0]*m for i in range(n)]
for x in range(len(USER_FIELD)):
    for y in range(len(USER_FIELD)):
        USER_FIELD[x][y] = ' '

COMPUTER_FIELD = [[0]*m for i in range(n)]
for x in range(len(COMPUTER_FIELD)):
    for y in range(len(COMPUTER_FIELD)):
        COMPUTER_FIELD[x][y] = ' '

BATTLE_FIELD = [[0]*m for i in range(n)]
for x in range(len(BATTLE_FIELD)):
    for y in range(len(BATTLE_FIELD)):
        BATTLE_FIELD[x][y] = ' '

user = Man(USER_FIELD, COMPUTER_FIELD) #пользователь Игрок
computer = Computer(COMPUTER_FIELD, USER_FIELD) #пользователь Компьютер
COMPUTER_FIELD = computer.replace_computers_ships(COMPUTER_FIELD) #Разместить корабли компьютера
USER_FIELD = user.replace_ships(USER_FIELD) #пользователь размещает компьютер

print("Поле игрока")
Field.display(USER_FIELD) #Поле игрока

flag = True
while True:
    COMPUTER_FIELD = user.shoot(COMPUTER_FIELD)
    flag = Field.check_to_victory(COMPUTER_FIELD)
    if flag == True:
        print("Ты поДЕБил")
        break
    USER_FIELD = computer.computer_shoot(USER_FIELD)
    flag = Field.check_to_victory(USER_FIELD)
    if flag == True:
        print("Компьютер поДЕБил")
        break
    print('Поле игрока')
    Field.display(USER_FIELD) #Поле игрока
    print('Поле компьютера')
    #переписывает объекты с компьютерного поля, в которых упал заряд, будь то
    #подбитый корабль, или просто мишень в пустое поле, которое будет отображенно
    BATTLE_FIELD = Field.field_to_battle_field(COMPUTER_FIELD, BATTLE_FIELD)
    Field.display(BATTLE_FIELD)
