def check_to_victory(field):
    for x in range(len(field)):
        for y in range(len(field)):
            if field[x][y] == '#':
                return False
    return True

def field_to_battle_field(field, battle_field):
    for x in range(len(field)):
        for y in range(len(field)):
            if field[x][y] == '@':
                battle_field[x][y] = '@'
            if field[x][y] == 'x':
                battle_field[x][y] = 'x'
    return battle_field

def display(battle_field):
    for item in battle_field:
        print(item)
    print("\n\n")