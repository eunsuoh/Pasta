from collections import deque

def isPalindrome(s: str) -> bool:
    deq = deque()
    for char in s:
        if char.isalnum():  # 알파벳과 숫자인지 확인
            deq.append(char.lower())  # 소문자로 변환 후 덱에 추가
    
    while len(deq) > 1:
        if deq.popleft() != deq.pop():  # 양 끝의 문자 비교
            return False  # 회문이 아니면 False 반환
    
    return True  # 회문이면 True 반환

def check_palindrome():
    s = input("문자열 입력: ")
    if isPalindrome(s):
        print("입력한 문자열은 회문입니다.")
    else:
        print("입력한 문자열은 회문이 아닙니다.")

# 함수 호출
check_palindrome()
