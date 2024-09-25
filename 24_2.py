with open('24_2.txt') as f:
    lines = list(map(lambda x: x.rstrip(), f.readlines()))


def intersection(line1, line2):
    return [let for let in line1 if let in line2]


count_palindromes = 0
need_length = 7
palindromes = [1 for _ in range(4)]
for ind_line, line in enumerate(lines[:-6]):
    palindromes[0] *= len(intersection(lines[ind_line], lines[ind_line + 6]))
    palindromes[1] *= len(intersection(lines[ind_line + 1], lines[ind_line + 5]))
    palindromes[2] *= len(intersection(lines[ind_line + 2], lines[ind_line + 4]))
    palindromes[3] *= len(intersection(lines[ind_line + 3], lines[ind_line + 3]))
    count_palindromes += palindromes[0] * palindromes[1] * palindromes[2] * palindromes[3]
    palindromes = [1 for _ in range(4)]

print(count_palindromes)
