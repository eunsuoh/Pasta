def solution(decimal):
  stack = []
  while decimal > 0:
    remainder = decimal % 2
    stack.append(str(remainder))
    decimal //= 2
  binary = ""
  while stack:
    binary += stack.pop()

  return binary

decimal = int(input("10진수 값은?"))
binary = solution(decimal)
print(f"10진수 {decimal}을 2진수로 변환한 값은 {binary}")

