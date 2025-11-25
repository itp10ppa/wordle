# проверка слова (чтобы это было русское слово из 5 букв)
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
        print('\n' * 40)

        for attempt in attempts:
            print(attempt)

        if guess == target_word.upper():
            is_winner = True
            print(f"\nПобеда! Вы угадали слово с {current_attempt} попытки.")
        else:
            print('\nУ вас осталось попыток:', 6 - current_attempt, '\n')

    if not is_winner:
        print('Вы не угадали. Загаданное слово было', target_word.upper())

    return is_winner
