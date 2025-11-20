from game_manager import game_mode_selection, play_logic, validation
import random

def run_game():
    print('=' * 40)
    print(' '* 7 + 'Добро пожаловать в WORDLE!')
    print('=' * 40)
    print('\n--- ПРАВИЛА ИГРЫ --- \n'
          '\nЦель: угадать загаданное из 5 букв слово за 6 попыток.'
          '\nВводите слово из 5 букв и получайте цветные подсказки: '
          '\n ** зеленый - буква на правильном месте'
          '\n ** желтый - буква есть в слове, но на другом месте'
          '\n ** без цвета - буквы нет в слове')


    game_mode = game_mode_selection()

    if game_mode == 2:
        print('Компьютер загадал слово. Введите русское слово из 5 букв, чтобы угадать. У вас 6 попыток. Удачи!')
        words = ['ангар', 'касса', 'стиль', 'принт']
        target_word = random.choice(words)
        print(target_word)

        play_logic(target_word)

    else:
        print('Отвернитесь, пока ваш друг загадывает слово')
        print('Введите загаданное слово:')
        friend_word = validation()
        print('\n' * 10)

        play_logic(friend_word)

run_game()


while True:
    a = input('Сыграть еще раз? Да/нет: ').strip().upper()

    if a == 'ДА':
        run_game()
    elif a == 'НЕТ':
        print('Очень жаль. До свидания!')
        break
    else:
        print('Ошибка: некорректное значение. Попробуйте еще раз.')
