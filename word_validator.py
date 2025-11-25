def dictionary():
    with open("dictionary.txt", "r", encoding="utf-8") as f:
        words = set()

        for line in f:
            if len(line) == 6:
                words.add(line.strip())

        return sorted(words)

def check_word_in_dictionary(word_to_check):
    if word_to_check.lower() in dictionary():
        return True

    return False
