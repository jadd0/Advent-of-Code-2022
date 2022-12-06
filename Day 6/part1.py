lines = open('text.txt').read().strip().splitlines()

val = 0

for line in lines:
  stack = []
  for i in range(len(line)):
    if len(stack) < 4:
      stack.append(line[i])
    else:
      if (len(set(stack)) == len(stack)):
        val = i
        break
      stack.pop(0)
      stack.append(line[i])
  print(val)
