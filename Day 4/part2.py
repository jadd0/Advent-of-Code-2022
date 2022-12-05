pairs = [pair.split(',') for pair in open('text.txt').read().strip().splitlines()]
total = 0

for p1, p2 in pairs:
  p1, p2 = p1.split('-'), p2.split('-')
  p1List, p2List = [], []

  bool = False

  for i in range(int(p1[0]), int(p1[1])+1):
    p1List.append(i)

  for i in range(int(p2[0]), int(p2[1])+1):
    p2List.append(i)

  for i in range (0,len(p1List)):
    if p1List[i] in p2List:
      bool = True
      break

  for i in range (0,len(p2List)):
    if p2List[i] in p1List:
      bool = True
      break
  
  if bool:
    total += 1

print(total)