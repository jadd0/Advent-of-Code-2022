pairs = [pair.split(',') for pair in open('text.txt').read().strip().splitlines()]
total = 0

for p1, p2 in pairs:
  p1, p2 = p1.split('-'), p2.split('-')
  p1List, p2List = [], []

  for i in range(int(p1[0]), int(p1[1])+1):
    p1List.append(i)

  for i in range(int(p2[0]), int(p2[1])+1):
    p2List.append(i)

  p1Check = all(item in p1List for item in p2List)
  p2Check = all(item in p2List for item in p1List)

  if p1Check or p2Check:
    total += 1

print(total)