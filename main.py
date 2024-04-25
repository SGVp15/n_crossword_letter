import random

random_kirill = 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ'
print(random.choice(random_kirill))


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
    with open()
    words = ['цапля', 'игра','цапля', 'игра','цапля', 'игра','цапля', 'игра', 'друг']
    max_len_word = max(len(x) for x in words)
    max_kross = max(max_len_word, len(words))
    print(max_len_word)
    kross = create_random_kross(max_kross)
    for k, w in enumerate(words):
        print(f'{max_kross - len(w)=} {max_kross=} {len(w)=} ')
        first_position = random.randint(0, max_kross - len(w))
        print(first_position)
        for i in range(len(w)):
            kross[k][first_position + i] = w[i]
    for row in kross:
        print(' '.join(row))
