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


def validation():
    while True:
        try:
            guess = input('Введите вашу догадку: ').strip()

            if not all('а' <= char <= 'я' for char in guess):
                print('Слово должно содержать только русские буквы! Попробуйте еще раз.')
            elif len(guess) != 5:
                print('Слово должно состоять из 5 букв! Попробуйте еще раз.')
            else:
                return guess

        except ValueError:
            print('Ошибка: вы ввели некорректное значение! Попробуйте ещё раз.')


def play_vs_computer():
    print()


def play_vs_friend():
    print()


