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
        word = input().strip().upper()

        if not all('А' <= char <= 'Я' for char in word):
            print('Слово должно содержать только русские буквы! Попробуйте еще раз.')
        elif len(word) != 5:
            print('Слово должно состоять из 5 букв! Попробуйте еще раз.')
        else:
            return word


def play_logic(target_word):
    attempts = []
    current_attempt = 0
    is_winner = False
    print('Попробуйте угадать слово:')

    while current_attempt < 6 and not is_winner:
        guess = validation()
        attempts.append(guess)
        current_attempt += 1

        for attempt in attempts:
            print(attempt)

        if guess == target_word.upper():
            is_winner = True
            print(f"Победа! Вы угадали слово с {current_attempt} попытки.")
        else:
            print('У вас осталось попыток:', 6 - current_attempt, '\n')

    if not is_winner:
        print('Вы не угадали. Загаданное слово было', target_word.upper())

    return is_winner


