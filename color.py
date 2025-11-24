def analyze_letters(user_word, target_word):

    #Анализирует совпадения букв между словами и возвращает цвета для каждой буквы
    user_word = user_word.upper()
    target_word = target_word.upper()

    result = ['gray'] * len(user_word)  # По умолчанию все буквы серые
    target_letters = list(target_word)

    # Первый проход: находим точные совпадения (зеленые)
    for i in range(len(user_word)):
        if i < len(target_word) and user_word[i] == target_word[i]:
            result[i] = 'green'
            target_letters[i] = None  # Помечаем использованную букву

    # Второй проход: находим буквы на неправильных позициях (желтые)
    for i in range(len(user_word)):
        if result[i] != 'green' and user_word[i] in target_letters:
            # Находим первую неиспользованную такую букву
            for j in range(len(target_letters)):
                if target_letters[j] == user_word[i]:
                    result[i] = 'yellow'
                    target_letters[j] = None
                    break

    return result

def create_colored_block(char, color):
    #Создает цветной кубик с буквой внутри
    colors = {
        'green': '\033[48;5;34m\033[1;97m',  # Ярко-зеленый фон, белый жирный текст
        'yellow': '\033[48;5;178m\033[1;97m',  # Ярко-желтый фон, белый жирный текст
        'gray': '\033[48;5;240m\033[1;97m',  # Темно-серый фон, белый жирный текст
        'blue': '\033[48;5;33m\033[1;97m',  # Синий фон, белый жирный текст
        'reset': '\033[0m'  # Сброс цвета
    }

    return f"{colors[color]} {char} {colors['reset']}"