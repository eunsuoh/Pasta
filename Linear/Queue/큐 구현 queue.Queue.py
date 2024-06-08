import queue

# 큐 초기화
q = queue.Queue()

# 큐에 데이터 추가
q.put(1)
q.put(2)
q.put(3)

print(f"현재 큐 상태: {list(q.queue)}")

# 큐의 맨 앞 데이터 제거
first_item = q.get()
print(f"제거된 첫 번째 아이템: {first_item}")
print(f"현재 큐 상태: {list(q.queue)}")

# 큐에 데이터 추가
q.put(4)
q.put(5)

print(f"현재 큐 상태: {list(q.queue)}")

# 큐의 맨 앞 데이터 제거
first_item = q.get()
print(f"제거된 첫 번째 아이템: {first_item}")
print(f"현재 큐 상태: {list(q.queue)}")
