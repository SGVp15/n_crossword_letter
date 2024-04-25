import random
import re

from config import file_with_word, out_file, random_kirill, ROWS, COLUMNS


def create_random_kross(num_cols, num_rows):
    kross = [[None for _ in range(num_cols)] for _ in range(num_rows)]

    for row in range(num_rows):
        for col in range(num_cols):
            random_char = random.choice(random_kirill)
            kross[row][col] = random_char
    return kross


if __name__ == '__main__':
    with open(file_with_word, 'r', encoding='utf-8') as f:
        words = re.sub(r'[ ,\\\'\"\.;\t\d]+', '\n', f.read())
    words = words.strip()
    words = words.split('\n')
    words = list(map(str.upper, words))
    words = [x for x in words if x]

    max_len_word = max(len(x) for x in words)
    max_kross = max(max_len_word, len(words))
    while max_kross > len(words):
        words.append('')

    words = sorted(words, key=lambda A: random.random())
    num_cols = max(COLUMNS, max_len_word)
    num_rows = max(ROWS, max_kross)
    kross = create_random_kross(num_cols, num_rows)
    for k, w in enumerate(words):
        # print(f'{num_cols - len(w)=} {max_kross=} {len(w)=} ')
        first_position = random.randint(0, num_cols - len(w))
        # print(first_position)
        for i in range(len(w)):
            kross[k][first_position + i] = w[i]

    with open(out_file, mode='w', encoding='utf-8') as f:
        for i, row in enumerate(kross):
            s = '\t'.join(row)
            try:
                s += '\t'
                s += f'{words[i]}'.capitalize()
            except IndexError:
                pass
            print(s)
            f.write(f'{s}\n')
