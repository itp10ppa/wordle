from color import display_attempt_history
from word_validator import check_word_in_dictionary, dictionary
import random


# Сравнение введенного слова с загаданным
def play_logic(target_word):
    attempts = []
    current_attempt = 0
    is_winner = False
    target_word = target_word.upper()

    while current_attempt < 6 and not is_winner:
        while True:
            guess = input('\nПопробуйте угадать слово: ').strip().upper()

            if guess == target_word:
                is_winner = True
                break
            else:
                if not all(('А' <= char <= 'Я') or char == 'Ё' for char in guess):
                    print('Слово должно содержать только русские буквы! Попробуйте еще раз.')
                elif len(guess) != 5:
                    print('Слово должно состоять из 5 букв! Попробуйте еще раз.')
                elif not check_word_in_dictionary(guess):
                    print('Такого слова нет в словаре! Попробуйте еще раз.')
                else:
                    break

        attempts.append(guess)
        current_attempt += 1

        print('\n' * 40)
        print('╔══════════════════════════════════════╗')
        print('║           ИСТОРИЯ ПОПЫТОК            ║')
        print('╚══════════════════════════════════════╝\n')

        display_attempt_history(attempts, target_word)

        if guess == target_word.upper():
            is_winner = True
            print(f'\nПобеда! Вы угадали слово с {current_attempt} попытки!')
        else:
            remaining = 6 - current_attempt
            print(f'\nУ вас осталось попыток: {remaining} \n')

    if not is_winner:
        print('Вы не угадали. Загаданное слово было', target_word.upper())

    return is_winner


# Запуск игры
def run_game():
    print('\n--- ПРАВИЛА ИГРЫ ---')
    print('Цель: угадать загаданное из 5 букв слово за 6 попыток.')
    print('Вводите слово из 5 букв и получайте цветные подсказки:')
    print('🟩 Зеленый - буква на правильном месте')
    print('🟨 Желтый - буква есть в слове, но на другом месте')
    print('⬜ Серый - буквы нет в слове')

    print('\n--- ВЫБОР РЕЖИМА ИГРЫ ---')
    print('1 - Играть с компьютером')
    print('2 - Играть с другом')

    while True:
        try:
            game_mode_choice = int(input('\nВаш выбор (введите число): ').strip())

            if game_mode_choice == 1 or game_mode_choice == 2:
                break
            else:
                print('Ошибка: вы ввели некорректное значение! Попробуйте ещё раз.')

        except ValueError:
            print('Ошибка: введите число 1 или 2!')

    if game_mode_choice == 1:
        print('\n' * 40)
        print('Компьютер загадал слово. Введите русское слово из 5 букв, чтобы угадать. У вас 6 попыток. Удачи!')

        words = dictionary()
        target_word = random.choice(words)
        play_logic(target_word)

    elif game_mode_choice == 2:
        print('\n' * 40)
        print('Отвернитесь, пока ваш друг загадывает слово')
        friend_word = input('Введите слово, которое вы загадали: ').strip().lower()

        print('\n' * 40)
        print('Теперь угадывайте слово!')
        play_logic(friend_word)
