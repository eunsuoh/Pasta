from collections import deque

# 큐 초기화
queue = deque()

# 큐에 데이터 추가
queue.append(1)
queue.append(2)
queue.append(3)

print(f"현재 큐 상태: {list(queue)}")

# 큐의 맨 앞 데이터 제거
first_item = queue.popleft()
print(f"제거된 첫 번째 아이템: {first_item}")
print(f"현재 큐 상태: {list(queue)}")

# 큐에 데이터 추가
queue.append(4)
queue.append(5)

print(f"현재 큐 상태: {list(queue)}")

# 큐의 맨 앞 데이터 제거
first_item = queue.popleft()
print(f"제거된 첫 번째 아이템: {first_item}")
print(f"현재 큐 상태: {list(queue)}")
