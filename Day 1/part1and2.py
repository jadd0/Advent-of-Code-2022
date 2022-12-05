lines = open('text.txt', 'r').readlines()
arr = {}

count = 0

for line in lines:
    inp = line.strip()
    if inp != '':
      inp = int(inp)
      if count not in arr:
        arr[count] = 0
      arr[count] += inp
    else:
      count += 1

highest = 0
second = 0
third = 0

for i in arr:
  if arr[i] > highest:
    oldHighest, oldSecond, oldThird = highest, second, third
    highest = arr[i]
    second, third = oldHighest, oldSecond
  elif arr[i] > second:
    oldSecond, oldThird = second, third
    second = arr[i]
    third = oldSecond
  elif arr[i] > third:
    third = arr[i]

print(highest + second + third)
