# Анализирует совпадения букв между словами и возвращает цвета для каждой буквы
def analyze_letters(user_word, target_word):
    user_word = user_word.upper()
    target_word = target_word.upper()

    result = ['gray'] * len(user_word)
    target_letters = list(target_word)

    for i in range(len(user_word)):
        if i < len(target_word) and user_word[i] == target_word[i]:
            result[i] = 'green'
            target_letters[i] = None

    for i in range(len(user_word)):
        if result[i] != 'green' and user_word[i] in target_letters:
            for j in range(len(target_letters)):
                if target_letters[j] == user_word[i]:
                    result[i] = 'yellow'
                    target_letters[j] = None
                    break

    return result


# Создает цветной кубик с буквой внутри
def create_colored_block(char, color):
    colors = {
        'green': '\033[48;5;34m\033[1;97m',  # Ярко-зеленый фон, белый жирный текст
        'yellow': '\033[48;5;178m\033[1;97m',  # Ярко-желтый фон, белый жирный текст
        'gray': '\033[48;5;240m\033[1;97m',  # Темно-серый фон, белый жирный текст
        'reset': '\033[0m'  # Сброс цвета
    }
    return f'{colors[color]} {char} {colors['reset']}'


# Отображает слово в виде цветных кубиков
def display_colored_word(word, color_pattern):
    result = ''

    for i, char in enumerate(word):
        result += create_colored_block(char, color_pattern[i]) + ' '

    return result


# Отображает историю всех попыток с цветными кубиками
def display_attempt_history(attempts, target_word):
    for i, attempt_word in enumerate(attempts, 1):
        color_pattern = analyze_letters(attempt_word, target_word)
        colored_blocks = display_colored_word(attempt_word, color_pattern)
        print(f'Попытка {i}: {colored_blocks}')
