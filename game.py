import random


def guess_the_number():

    def number_of_players():
        val_players = 0
        while True:
            print('Введите колличество игроков (один/два): ')
            val_players = input()
            if val_players == 'один':
                val_players = 1
                break
            if val_players == 'два':
                val_players = 2
                break
        return val_players


    def level_choose():
        val_of_range = 0
        while True:
            print('Введите уровень сложности (легкий/нормальный/сложный): ')
            level = input()
            if level == 'легкий':
                val_of_range = 11
                break
            elif level == 'нормальный':
                val_of_range = 101
                break
            elif level == 'сложный':
                val_of_range = 1001
                break
        return val_of_range


    player_number = number_of_players()
    val_range = level_choose()


    def input_number_cycle(): # -> int
        flag = True
        a = 0
        while flag:
            print(f'Введите число от 1 до {val_range - 1}: ')
            a = input()
            if str.isdigit(a):
               if int(a) >= 1 and int(a) <= val_range - 1:
                   flag = False
        return int(a)


    if player_number == 1:
        hidden_numer = random.randrange(1,val_range)
        val_in = input_number_cycle()
    if player_number == 2:
        print('Пусть игрок 1 загадает число')
        hidden_numer = input_number_cycle()
        print('игрок 2, угадывай')
        val_in = input_number_cycle()

    count = 0
    if val_range == 11:
        res_count = 5
    if val_range == 101:
        res_count = 8
    if val_range == 1001:
        res_count = 12

    while count != res_count:
        if val_in > hidden_numer:
            if player_number == 1:
                print('Число которое загадал компьютер - МЕНЬШЕ!')
            if player_number == 2:
                print('Число которое загадал 1-ый игрок - МЕНЬШЕ!')
            res_count -= 1
        elif val_in < hidden_numer:
            if player_number == 1:
                print('Число которое загадал компьютер - БОЛЬШЕ!')
            if player_number == 2:
                print('Число которое загадал 1-ый игрок - БОЛЬШЕ!')
            res_count -= 1
        elif val_in == hidden_numer:
            print(f'Поздравляю, вы угадали. Это число {val_in} !')
            break
        print(f'Осталось {res_count + 1} попыток')
        val_in = input_number_cycle()
    if count >= res_count:
        print(f'Вы проиграли. Загаданное число это {hidden_numer} !')
    print('Автор игры: Логин И.С.')
