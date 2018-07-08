from field import Field
from user import Man
from computer import Computer
from functions import check_to_victory, field_to_battle_field, display

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
USER_FIELD = user.replace_ships(USER_FIELD)


#print("Поле компьютера")
#computer.computer_display(COMPUTER_FIELD) #Поле компьютера
print("Поле игрока")
user.display(USER_FIELD) #Поле игрока


flag = True
while True:
    COMPUTER_FIELD = user.shoot(COMPUTER_FIELD)
    flag = check_to_victory(COMPUTER_FIELD)
    if flag == True:
        print("Ты поДЕБил")
        break
    USER_FIELD = computer.computer_shoot(USER_FIELD)
    #flag = check_to_victory(USER_FIELD)
    if flag == True:
        print("Компьютер поДЕБил")
        break
    print('Поле игрока')
    user.display(USER_FIELD) #Поле игрока
    print('Поле компьютера')
    BATTLE_FIELD = field_to_battle_field(COMPUTER_FIELD, BATTLE_FIELD)
    display(BATTLE_FIELD)
