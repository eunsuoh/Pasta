from collections import deque

def solution(N,K):
  queue = deque(range(1, N+1))

  while len(queue) > 1: 
    for _ in range(K - 1): 
      queue.append(queue.popleft())
      queue.popleft()  
  return queue[0]

N = int(input("요소의 개수"))
K = int(input("간격의 크기"))
print(solution(N,K))
