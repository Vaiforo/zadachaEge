with open('24_1.txt') as f:
    lines = f.readlines()

need_word = 'ABED'

words_count = 0
words = [0 for _ in range(len(need_word))]
words[0] = 1
for ind_line, line in enumerate(lines):
    for i, let in enumerate(need_word):
        words[i] *= line.count(let)
    words_count += words[-1]
    words = [1] + words[:-1]

print(words_count)
