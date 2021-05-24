# library
import os
import readchar
import random

# var
# map
my_position = [0, 0]
new_position = my_position.copy()
pos_x = 0
pos_y = 1
map_definition = '''\
               *.            --------------|
               |             |+++++++++++++|
----------------             |+++++++++++++|
|..............|             |+++++++++++++|
|..............              |+++++++++++++|
|..............              |+++++++++++++|
|..............              -------------,|
|..............|                           ]
-----------------                          ]
|+++++++++++++++,                          ]
|+++++++++++++++|           ...............]
|+++++++++++++++|           ...............]
|+++++++++++++++|           ...............]
|+++++++++++++++|           ...............]
|+++++++++++++++|           ...............]
-----------------                          ]\
'''


#  /\
# /  \
#  ||
#  ||
#draw your map there



# map like variable
obstacle_definition = [list(row) for row in map_definition.split("\n")]
map_height = len(obstacle_definition)
map_width = len(obstacle_definition[0])

# tail
tail = []  # tail model is pokemon model
tail_length = 0
collected_pokemons = 0

# map objets
num_of_map_objets = 11
map_objets = []

# models
player_model = '@'
pokemon_model = '*'
enemy_model = '$'
scrub_model = '+'
wall_upright = '|'
wall_horizontal = '-'
clear_space = ' '
obstacles = ['|', '-']


# aleatory vars
end_game = False
pokemon_name = ''

# enemy's
num_of_enemys = 6  # without obligatory enemy's
enemys = []
enemy_spawner = '.'
obligatory_enemy_spawner = ','
while len(enemys) <= num_of_enemys:
    for y in range(map_height):
        for x in range(map_width):
            if obstacle_definition[y][x] == ',':
                new_enemy = [x, y]
                if new_enemy not in enemys:
                    enemys.append(new_enemy)
            if obstacle_definition[y][x] == '.':

                probability = random.randint(0, 10)
                if probability == 8:
                    new_enemy = [x, y]
                    if new_enemy not in enemys and len(enemys) <= num_of_enemys:
                        enemys.append(new_enemy)


# main loop
while not end_game:

    print('''\
    player_model = '@'
    pokemon_model = '*'
    enemy_model = '$'
    scrub_model = '+'\
    ''')
    print('+' + wall_horizontal * map_width + '+')

    if obstacle_definition[my_position[pos_y]][my_position[pos_x]] == '*':
        print('has obtenido un nuevo pokemon')
        print(obstacle_definition[my_position[pos_x]][my_position[pos_y]])
        print(f'{my_position[pos_x]} {my_position[pos_y]}')
        pokemon_name = input('que nombre le deseas poner?')

    for coordinate_y in range(map_height):
        print('|', end='')
        for coordinate_x in range(map_width):
            char_to_draw = clear_space

            # drawing the map


            if obstacle_definition[coordinate_y][coordinate_x] == wall_upright:
                char_to_draw = wall_upright
            if obstacle_definition[coordinate_y][coordinate_x] == wall_horizontal:
                char_to_draw = wall_horizontal
            if obstacle_definition[coordinate_y][coordinate_x] == pokemon_model:
                char_to_draw = pokemon_model
            if obstacle_definition[coordinate_y][coordinate_x] == scrub_model:
                char_to_draw = scrub_model
            for map_enemy in enemys:
                if map_enemy[pos_x] == coordinate_x and map_enemy[pos_y] == coordinate_y:
                    char_to_draw = enemy_model
                    object_in_cell = map_enemy
            if my_position[pos_x] == coordinate_x and my_position[pos_y] == coordinate_y:
                char_to_draw = player_model
            print(char_to_draw, end='')
        print('|')
    print('+' + wall_horizontal * map_width + '+')
    movement = readchar.readchar().decode()
    print(movement)
    if movement == 'c' or movement == 'C':
        break
    elif movement == 'w' or movement == 'W':
        new_position[pos_y] -= 1
        new_position[pos_y] %= map_height

    elif movement == 's' or movement == 'S':
        new_position[pos_y] += 1
        new_position[pos_y] %= map_height

    elif movement == 'a' or movement == 'A':
        new_position[pos_x] -= 1
        new_position[pos_x] %= map_width

    elif movement == 'd' or movement == 'D':
        new_position[pos_x] += 1
        new_position[pos_x] %= map_width


    if obstacle_definition[new_position[pos_y]][new_position[pos_x]] not in obstacles:
        my_position = new_position.copy()

    new_position = my_position.copy()
