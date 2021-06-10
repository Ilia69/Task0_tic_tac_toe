import winner_checking
import new_point


def game_field_initial():
    """Создаёт список для пустого поля"""
    for i in range(9):
        game_field.append('_')
    game_field.append(8)

    return None


def print_game_field():
    """Выводит на экран текущее состояние игрового поля"""
    print('    0   1   2')
    for i in range(3):
        print(i, end=' | ')
        for j in range(3):
            print(game_field[j + 3*i], end=' | ')
        print('\n')

    return None


def gamer_first():
    """Предложение игроку первого хода"""
    print('Хотите сделать первый ход?')
    answer = ''
    while not (answer == 'да' or answer == 'нет'):
        answer = input("Введите 'да' или 'нет' \n")
    return answer == 'да'


game_field = []
game_field_initial()
print_game_field()

if gamer_first():
    new_point.make_new_point_gamer(game_field, 'x')
    print_game_field()

while True:
    new_point.make_new_point_computer(game_field, 'o')
    print_game_field()
    if winner_checking.check_winner(game_field):
        print('Вы проиграли :(')
        break

    new_point.make_new_point_gamer(game_field, 'x')
    print_game_field()
    if winner_checking.check_winner(game_field):
        print('Вы победили :)')
        break

    if game_field[-1] == 0 and not winner_checking.check_winner(game_field):
        print('Ничья!')
        break