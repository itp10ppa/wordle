from color import display_attempt_history, display_current_attempt


def validation():
    while True:
        word = input().strip().upper()

        if not all('А' <= char <= 'Я' for char in word):
            print('Слово должно содержать только русские буквы! Попробуйте еще раз.')
        elif len(word) != 5:
            print('Слово должно состоять из 5 букв! Попробуйте еще раз.')
        else:
            return word


# угадывание слов (сравнение введенного слова с загаданным)
def play_logic(target_word):
    attempts = []
    current_attempt = 0
    is_winner = False
    print('\nПопробуйте угадать слово:')

    while current_attempt < 6 and not is_winner:
        guess = validation()
        attempts.append(guess)
        current_attempt += 1


        # Отображаем историю попыток с цветными кубиками
        print("╔══════════════════════════════════════╗")
        print("║           ИСТОРИЯ ПОПЫТОК            ║")
        print("╚══════════════════════════════════════╝")
        display_attempt_history(attempts, target_word)

        # Показываем текущую попытку с расшифровкой цветов
        display_current_attempt(guess, target_word)

        if guess == target_word.upper():
            is_winner = True
            print(f"\nПобеда! Вы угадали слово с {current_attempt} попытки!")
        else:
            remaining = 6 - current_attempt
            print(f'\nУ вас осталось попыток: {remaining} \n')

    if not is_winner:
        print('Вы не угадали. Загаданное слово было', target_word.upper())

    return is_winner