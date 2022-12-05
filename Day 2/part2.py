plays = [play.split() for play in open('text.txt').read().strip().splitlines()]

# A = 65
# X = 88

total = 0

# rock etc
scoreType = [1, 2, 3]

# win etc
scorePick = [0, 3, 6]

for p1, p2 in plays:
  p1, p2 = ord(p1) - ord('A'), ord(p2) - ord('X')
  # total += (scoreType[p2]) 

  if p2 == 0:
    total += 0
    if p1 == 0:
      total += scoreType[2]
    elif p1 == 1:
      total += scoreType[0]
    else:
      total += scoreType[1]

  elif p2 == 1:
    total += (scoreType[p1] + 3)

  elif p2 == 2:
    total += 6
    if p1 == 0:
      total += scoreType[1]
    elif p1 == 1:
      total += scoreType[2]
    else:
      total += scoreType[0]



  # if p2 == 2:
  #   total += 6
  # elif p2 == 1:
  #   total += 3
  # else:
  #   total += 0

  # # get losing score
  # if p2 == 0:
  #   if p1 == 0:
  #     total += scoreType[2]
  #   elif p1 == 1:
  #     total += scoreType[0]
  #   else:
  #     total += scoreType[1]


print(total)