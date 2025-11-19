def game_mode_selection():
    print('--- ВЫБОР РЕЖИМА ИГРЫ ---\n')
    print('1 - Играть с другом')
    print('2 - Играть с компьютером')

    while True:
        try:
            game_mode_choice = int(input('Ваш выбор (введите число): ').strip())

            if game_mode_choice == 1 or game_mode_choice == 2:
                return game_mode_choice
            else:
                raise ValueError

        except ValueError:
            print('Ошибка: вы ввели некорректное значение! Попробуйте ещё раз.')

