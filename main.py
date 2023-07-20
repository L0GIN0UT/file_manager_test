import sys
import random
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info,change_dir
from game_reverse import game_reverse
from game import guess_the_number

save_info('Старт')
try:
    command = sys.argv[1]
except IndexError:
    print('Необходимо выбрать команду.\n Введите help для просмотра команд!')
else:
    if command == 'list':
        get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название файла')
        else:
            create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название папки')
        else:
            create_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название файла/папки')
        else:
            try:
                delete_file(name)
            except FileNotFoundError:
                print('Файла/папки с таким названием не существует')
    elif command == 'change':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название папки')
        else:
            try:
                change_dir(name)
            except FileNotFoundError:
                print('Папки с таким названием не существует')
    elif command == 'copy':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название файла который вы хотите скопировать')
        else:
            try:
                new_name = sys.argv[3]
            except IndexError:
                print('Отсутствует название нового файла (копии)')
            else:
                try:
                    copy_file(name, new_name)
                except FileNotFoundError:
                    print('Файла с таким названием не существует')
    elif command == 'game_guess':
        guess_the_number()
    elif command == 'game_reverse':
        game_reverse()
    elif command == 'help':
        print('list - Выводит список папок и файлов')
        print('create_file - Создает файл с именем')
        print('create_folder - Создает папку с именем')
        print('delete - Удаляет файл с именем')
        print('change - Смена папки')
        print('copy - Делает копию файла с новым именем')
        print('game_guess - Игра угадай число')
        print('game_reverse - Игра угадай число наоборот')

    save_info('Конец')
