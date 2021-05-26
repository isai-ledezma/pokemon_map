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
# draw your map there


# map like variable
obstacle_definition = [list(row) for row in map_definition.split("\n")]
map_height = len(obstacle_definition)
map_width = len(obstacle_definition[0])

# tail
collected_pokemons_list = []
new_pokemon = []
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
op = 's'
while op == 's' or op == 'S':
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
        print(f'{my_position[pos_x]} {my_position[pos_y]}')

        # var for the war
        counter = 1
        enemy_life = 100
        selectec_pokemon = 0
        selectec_atack = 0
        text_in_war = None
        pokemon_probability = random.randint(1, 3)

        if obstacle_definition[my_position[pos_y]][my_position[pos_x]] == pokemon_model:
            print('has obtenido un nuevo pokemon')
            obstacle_definition[my_position[pos_y]][my_position[pos_x]] = clear_space
            pokemon_name = input('que nombre le deseas poner?')
            new_pokemon = [pokemon_name, 100]  # 100 is the life of pokemon
            collected_pokemons_list.append(new_pokemon)
        elif my_position in enemys:
            #obstacle_definition[my_position[pos_y]][my_position[pos_x]] == obligatory_enemy_spawner \
                #or
            text_in_war = 'enemigo'
            print('ohhh noooo te has encontrado con un enemigo')
        elif obstacle_definition[my_position[pos_y]][my_position[pos_x]] == scrub_model:
            probability_of_spawn = random.randint(1, 100)
            if 80 <= probability_of_spawn <= 90:
                if pokemon_probability == 1:
                    text_in_war = 'pikachu salvaje'
                elif pokemon_probability == 2:
                    text_in_war = 'charmander salvaje'
                elif pokemon_probability == 3:
                    text_in_war = 'treeko salvaje'
                print(f'ohhhhh no te has encontrado un {text_in_war} ')

        pokemons_with_life = 1
        # space for the future war
        if text_in_war:
            while True:
                counter = 1
                for c in collected_pokemons_list:
                    print(f'{counter}: [{c[0]}, {c[1]} pts de vida]')
                    counter += 1
                selectec_pokemon = int(input('que pokemon deseas usar?')) - 1
                os.system('cls')
                if selectec_pokemon in range(0, counter - 1):
                    break
                else:
                    print('no existe ese pokemon')

            while pokemons_with_life >= 1:
                print(f'pokemon actual {collected_pokemons_list[selectec_pokemon][0]} con ' +
                      f'{collected_pokemons_list[selectec_pokemon][1]} puntos de vida')

                enemy_atac = random.randint(1, 3)
                if enemy_atac == 1:
                    enemy_atac == 'golpe'
                    collected_pokemons_list[selectec_pokemon][1] -= 10
                elif enemy_atac == 2:
                    enemy_atac = 'patada'
                    collected_pokemons_list[selectec_pokemon][1] -= 20
                elif enemy_atac == 3:
                    enemy_atac = 'cachetada'
                    collected_pokemons_list[selectec_pokemon][1] -= 25
                if collected_pokemons_list[selectec_pokemon][1] >= 1:
                    print(f'el {text_in_war} ha usado {enemy_atac}')
                    print(f'te quedan {collected_pokemons_list[selectec_pokemon][1]} puntos de vida')
                    print('''\
                    1: golpe
                    2: patada
                    3: cachetada
                    any key: cambiar de pokemon''')
                    selectec_atack = input('?:')
                    if selectec_atack == '1':
                        enemy_life -= 10
                        print(f'has usado golpe a el {text_in_war} le quedan {enemy_life} pts de vida')
                    elif selectec_atack == '2':
                        enemy_life -= 20
                        print(f'has usado golpe a el {text_in_war} le quedan {enemy_life} pts de vida')
                    elif selectec_atack == '3':
                        enemy_life -= 50
                        print(f'has usado golpe a el {text_in_war} le quedan {enemy_life} pts de vida')
                    else:
                        while True:
                            counter = 1
                            for c in collected_pokemons_list:
                                print(f'{counter}: [{c[0]}, {c[1]} pts de vida]')
                                counter += 1
                            selectec_pokemon = int(input('que pokemon deseas usar?')) - 1
                            if selectec_pokemon in range(0, counter - 1):
                                break
                            else:
                                print('no existe ese pokemon')
                else:
                    counter = 0
                    pokemons_with_life = 0

                    for c in collected_pokemons_list:
                        if collected_pokemons_list[counter][1] >= 1:
                            pokemons_with_life += 1
                        counter += 1

                    if pokemons_with_life >= 1:
                        print('tu pokemon tiene muy poca vida selecciona otro')
                        print('solo se muestran los pokemones con vida suficiente')
                        counter = 1
                        for c in collected_pokemons_list:
                            if c[1] >= 1:
                                print(f'{counter}: [{c[0]}, {c[1]} pts de vida]')
                            counter += 1
                        while collected_pokemons_list[selectec_pokemon][1] <=0:
                            selectec_pokemon = int(input('que pokemon deseas usar?')) - 1
                            if collected_pokemons_list[selectec_pokemon][1] <=0:
                                print('ese pokemon tiene muy poca vida!!')
                    else:


                        end_game = True



                if enemy_life <= 0:
                    if text_in_war != 'enemigo':
                        print('has obtenido un nuevo pokemon')

                        pokemon_name = input('que nombre le deseas poner?')
                        new_pokemon = [pokemon_name, 100]  # 100 is the life of pokemon
                        collected_pokemons_list.append(new_pokemon)
                    else:
                        if [my_position[pos_x],my_position[pos_y]] in obstacle_definition:
                            obstacle_definition.remove([my_position[pos_x], my_position[pos_y]])
                        enemys.remove([my_position[pos_x], my_position[pos_y]])

                    break

            text_in_war = None

        os.system("cls")
        if not end_game:
            print('+' + wall_horizontal * map_width + '+')
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
        else:
            counter = 1
            for c in collected_pokemons_list:
                print(f'{counter}: [{c[0]}, {c[1]} pts de vida]')
                counter += 1
            counter = 0
            pokemons_with_life = 0

            for c in collected_pokemons_list:
                if collected_pokemons_list[counter][1] >= 1:
                    pokemons_with_life += 1
                counter += 1
            if pokemons_with_life >= 1:
                print('HAS GANADO!')
            elif pokemons_with_life <= 0:
                print('HAS PERDIDO!!')

            print('el juego ha terminado!!')
    print('DESEAS VOLVER A JUGAR? s para continuar, cualquier otra tecla para terminar')
    op = readchar.readchar().decode()
