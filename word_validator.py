def dictionary():
    with open("dictionary.txt", "r", encoding="utf-8") as f:
        words = set()

        for line in f:
            if len(line) == 6:
                words.add(line.strip())

        return sorted(words)