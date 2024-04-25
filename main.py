import random
import re

from config import file_with_word, out_file, random_kirill


def create_random_kross(max_kross):
    kross = []
    for i in range(max_kross):
        temp_list = []
        for _ in range(max_kross):
            a = random.choice(random_kirill)
            temp_list.append(a)
        kross.append(temp_list)
    return kross


if __name__ == '__main__':
    with open(file_with_word, 'r', encoding='utf-8') as f:
        words = f.read().strip().split('\n')
    words = [re.sub(r'[ .|;\t\d]*', '', w) for w in words]

    words = list(map(str.strip, words))
    words = list(map(str.upper, words))
    max_len_word = max(len(x) for x in words)
    max_kross = max(max_len_word, len(words))
    while max_kross > len(words):
        words.append('')

    words = sorted(words, key=lambda A: random.random())

    kross = create_random_kross(max_kross)
    for k, w in enumerate(words):
        # print(f'{max_kross - len(w)=} {max_kross=} {len(w)=} ')
        first_position = random.randint(0, max_kross - len(w))
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
