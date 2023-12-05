lines = open('input.txt', 'r').readlines()

cards = [1] * len(lines)
for i, line in enumerate(lines):
        x, y = map(str.split, line.split('|'))
        n = len(set(x) & set(y))

        for j in range(i + 1, min(i + 1 + n, len(lines))):
                cards[j] += cards[i]


print(sum(cards))