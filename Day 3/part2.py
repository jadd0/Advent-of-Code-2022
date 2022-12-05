sacks = [sack.split() for sack in open('text.txt', 'r').readlines()]

# split into equal parts of 3
sacks = [sacks[i * 3:(i + 1) * 3] for i in range((len(sacks) + 3 - 1) // 3 )]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
total = 0


for elves in range(len(sacks)):
  commonLetter, firstList, secondList  = [], [], []

  for item in sacks[elves][0][0]:
    commonLetter.append(item)
  
  for item in sacks[elves][1][0]:
    if item in commonLetter:
      firstList.append(item)

  for item in sacks[elves][2][0]:
    if item in firstList:
      secondList.append(item)
  
  total += (letters.index(secondList[0]) + 1)

print(total)