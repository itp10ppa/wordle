from game_manager import game_mode_selection, play_vs_friend, play_vs_computer


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
    print('Компьютер загадал слово')
    winner = play_vs_computer()

    if winner:
        print('ПОБЕДА! Искусственный интеллект побежден!')
    else:
        print('Не сдавайтесь! Попробуйте еще раз!')
else:
    print('Отвернитесь, пока ваш друг загадывает слово')
    winner = play_vs_friend()

    if winner:
        print('ПОБЕДА! Поздравляем, вы угадали слово друга!')
    else:
        print('К сожалению, вы не угадали слово.')
