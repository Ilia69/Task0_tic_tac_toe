def check_winner_horizon(game_field):
    """Проверка, есть ли три одинаковых символа по горизонтали"""
    first_horizon = (game_field[0] == game_field[1]) and (game_field[1] == game_field[2])
    first_horizon = first_horizon and ((game_field[0] == 'x') or (game_field[0] == 'o'))

    second_horizon = (game_field[3] == game_field[4]) and (game_field[4] == game_field[5])
    second_horizon = second_horizon and ((game_field[3] == 'x') or (game_field[3] == 'o'))

    third_horizon = (game_field[6] == game_field[7]) and (game_field[7] == game_field[8])
    third_horizon = third_horizon and ((game_field[7] == 'x') or (game_field[7] == 'o'))

    return first_horizon or second_horizon or third_horizon


def check_winner_vertical(game_field):
    """Проверка, есть ли три одинаковых символа по вертикали"""
    first_vertical = (game_field[0] == game_field[3]) and (game_field[3] == game_field[6])
    first_vertical = first_vertical and ((game_field[0] == 'x') or (game_field[0] == 'o'))

    second_vertical = (game_field[1] == game_field[4]) and (game_field[4] == game_field[7])
    second_vertical = second_vertical and ((game_field[1] == 'x') or (game_field[1] == 'o'))

    third_vertical = (game_field[2] == game_field[5]) and (game_field[5] == game_field[8])
    third_vertical = third_vertical and ((game_field[2] == 'x') or (game_field[2] == 'o'))

    return first_vertical or second_vertical or third_vertical


def check_winner_diagonal(game_field):
    """Проверка, есть ли три одинаковых символа по диагонали"""
    first_diagonal = (game_field[0] == game_field[4]) and (game_field[4] == game_field[8])
    first_diagonal = first_diagonal and ((game_field[0] == 'x') or (game_field[0] == 'o'))

    second_diagonal = (game_field[2] == game_field[4]) and (game_field[4] == game_field[6])
    second_diagonal = second_diagonal and ((game_field[2] == 'x') or (game_field[2] == 'o'))

    return first_diagonal or second_diagonal


def check_winner(game_field):
    """Проверка, есть ли победитель на поле"""
    check_horizon = check_winner_horizon(game_field)
    check_vertical = check_winner_vertical(game_field)
    check_diagonal = check_winner_diagonal(game_field)

    return check_horizon or check_vertical or check_diagonal
