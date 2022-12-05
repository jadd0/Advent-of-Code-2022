sacks = [sack.split() for sack in open('text.txt', 'r').readlines()]

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

total = 0

for sack in sacks:
  commonLetter = {}
  sack = sack[0]
  firstpart, secondpart = sack[:len(sack)//2], sack[len(sack)//2:]

  for letter in firstpart:
    commonLetter[letter] = 1

  for letter in secondpart:
    if letter in commonLetter:
      total += (letters.index(letter) + 1)
      break

print(total)