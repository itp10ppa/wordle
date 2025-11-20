import random


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
        guess = input('Введите вашу догадку: ').strip()

        if not all('а' <= char <= 'я' for char in guess):
            print('Слово должно содержать только русские буквы! Попробуйте еще раз.')
        elif len(guess) != 5:
            print('Слово должно состоять из 5 букв! Попробуйте еще раз.')
        else:
            return guess



def play_vs_computer():
    words = ['ангар', 'касса', 'стиль', 'принт']
    target_word = random.choice(words)
    print(target_word)

    attempts = []
    current_attempt = 0
    is_winner = False

    print('Компьютер загадал слово. Введите русское слово из 5 букв, чтобы угадать. У вас 6 попыток. Удачи!')

    while current_attempt < 6 and not is_winner:
        gues = validation()
        attempts.append(gues)
        current_attempt += 1

        for attempt in attempts:
            print(attempt.upper())

        if gues == target_word:
            is_winner = True
            print('WIN')

    if not is_winner:
        print('Вы не угадали. Загаданное слово было', target_word.upper())


def play_vs_friend():
    print()


