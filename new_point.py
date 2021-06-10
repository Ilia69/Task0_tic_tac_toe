import random


def make_new_point_gamer(game_field, symbol):
    """Отмечает сделанный игроком ход на поле"""
    while True:
        error = False
        try:
            i, j = map(int, input('Ваш ход ').split())
        except ValueError:
            i, j = 0, 0
            error = True
            print('Ведите через пробел номер ряда и колонки')

        if not error and game_field[j + 3*i] == '_':
            game_field[j + 3*i] = symbol
            game_field[-1] -= 1
            break
        elif not error:
            print('Эта клетка уже занята')

    return None


def make_new_point_computer(game_field, symbol):
    """Делает случайный ход на свободную клетку поля"""
    next_point = random.randint(0, game_field[-1])
    counter = -1
    for i in range(len(game_field)):
        if game_field[i] == '_':
            counter += 1

        if counter == next_point:
            game_field[i] = symbol
            break

    game_field[-1] -= 1
    return None
