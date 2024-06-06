n = 15
answer = []

for i in range(1, n+1):
  if i % 3 == 0 and i % 5 == 0:
    answer.append("보석")
  elif i % 3 == 0:
    answer.append("루비")
  elif i % 5 == 0:
    answer.append("오팔")
  else:
    answer.append(str(i))

print(answer)
