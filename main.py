from game_manager import play_logic, validation
import random


# Запуск игры
def run_game():
    print('\n--- ПРАВИЛА ИГРЫ --- \n'
          '\nЦель: угадать загаданное из 5 букв слово за 6 попыток.'
          '\nВводите слово из 5 букв и получайте цветные подсказки: '
          '\n ** зеленый - буква на правильном месте'
          '\n ** желтый - буква есть в слове, но на другом месте'
          '\n ** без цвета - буквы нет в слове')

    print('\n--- ВЫБОР РЕЖИМА ИГРЫ ---\n'
          '\n1 - Играть с компьютером'
          '\n2 - Играть с другом')


    while True:
        game_mode_choice = int(input('\nВаш выбор (введите число): ').strip())

        if game_mode_choice == 1 or game_mode_choice == 2:
            break
        else:
            print('Ошибка: вы ввели некорректное значение! Попробуйте ещё раз.')

    if game_mode_choice == 1:
        print('\n' * 40)
        print('Компьютер загадал слово. Введите русское слово из 5 букв, чтобы угадать. У вас 6 попыток. Удачи!')

        '''САШЕ: В строке 31 надо убрать лист и вместо него подключить словарь'''
        words = ['ангар', 'касса', 'стиль', 'принт']
        target_word = random.choice(words)
        print(target_word)

        play_logic(target_word)

    elif game_mode_choice == 2:
        print('\n' * 40)
        print('Отвернитесь, пока ваш друг загадывает слово')
        print('Введите загаданное слово:')
        friend_word = validation()
        print('\n' * 40)

        play_logic(friend_word)


print('\n' * 10)
print('=' * 40)
print(' '* 7 + 'Добро пожаловать в WORDLE!')
print('=' * 40)

run_game()


while True:
    a = input('\n\nСыграть еще раз? Да/нет: ').strip().upper()

    if a == 'ДА':
        print('\n' * 10)
        run_game()
    elif a == 'НЕТ':
        print('Очень жаль. До свидания!')
        break
    else:
        print('Ошибка: некорректное значение. Попробуйте еще раз.')
