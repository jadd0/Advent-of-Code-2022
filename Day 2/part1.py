plays = [play.split() for play in open('text.txt').read().strip().splitlines()]

# P1
total = 0

for p1, p2 in plays:
    p1 = ord(p1) - ord('A')
    p2 = ord(p2) - ord('X')
    total += (p2 - p1 + 4) % 3 * 3 + p2 + 1

print(total)

