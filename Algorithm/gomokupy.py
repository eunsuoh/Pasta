import math

# 오목 판 크기 (15x15)
BOARD_SIZE = 15
WIN_COUNT = 5

# 보드 초기화
board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]

# 플레이어 상수 정의
EMPTY = 0
PLAYER = 1  # 현재 플레이어 (AI)
OPPONENT = -1  # 상대 플레이어 (사용자)

def is_winning_move(board, player):
    """해당 플레이어가 이겼는지 검사하는 함수"""
    # 가로, 세로, 대각선에서 다섯 개가 연속되면 승리로 판정
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if (check_direction(board, row, col, 1, 0, player) or  # 가로
                check_direction(board, row, col, 0, 1, player) or  # 세로
                check_direction(board, row, col, 1, 1, player) or  # 대각선 \
                check_direction(board, row, col, 1, -1, player)):  # 대각선 /
                return True
    return False

def check_direction(board, row, col, delta_row, delta_col, player):
    """특정 방향으로 연속된 돌의 개수를 검사하는 함수"""
    count = 0
    for i in range(WIN_COUNT):
        r, c = row + i * delta_row, col + i * delta_col
        if 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] == player:
            count += 1
        else:
            break
    return count == WIN_COUNT

def evaluate_board(board):
    """현재 보드 상태에 대한 평가 함수"""
    score = 0
    # 간단한 평가 기준: 연결된 돌의 수를 기반으로 점수 계산
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == PLAYER:
                score += evaluate_position(board, row, col, PLAYER)
            elif board[row][col] == OPPONENT:
                score -= evaluate_position(board, row, col, OPPONENT)
    return score

def evaluate_position(board, row, col, player):
    """각 위치에서 연속된 돌의 수를 기반으로 점수 부여"""
    score = 0
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
    for delta_row, delta_col in directions:
        count = 0
        for i in range(WIN_COUNT):
            r, c = row + i * delta_row, col + i * delta_col
            if 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] == player:
                count += 1
            else:
                break
        score += count * count  # 연속된 돌의 개수에 따라 점수 부여
    return score

def minimax(board, depth, alpha, beta, maximizing_player):
    """알파-베타 가지치기와 함께 사용하는 미니맥스 함수"""
    if is_winning_move(board, PLAYER):
        return 1000  # 플레이어가 이겼을 경우 큰 점수 반환
    elif is_winning_move(board, OPPONENT):
        return -1000  # 상대가 이겼을 경우 낮은 점수 반환
    elif depth == 0:
        return evaluate_board(board)  # 최대 깊이에 도달 시 보드 평가

    if maximizing_player:
        max_eval = -math.inf
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER
                    eval = minimax(board, depth - 1, alpha, beta, False)
                    board[row][col] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break  # 가지치기
        return max_eval
    else:
        min_eval = math.inf
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if board[row][col] == EMPTY:
                    board[row][col] = OPPONENT
                    eval = minimax(board, depth - 1, alpha, beta, True)
                    board[row][col] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break  # 가지치기
        return min_eval

def best_move(board, depth):
    """최적의 수를 찾는 함수"""
    best_val = -math.inf
    best_move = None
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER
                move_val = minimax(board, depth - 1, -math.inf, math.inf, False)
                board[row][col] = EMPTY
                if move_val > best_val:
                    best_val = move_val
                    best_move = (row, col)
    return best_move

# 예시 사용
depth = 3  # 탐색 깊이
move = best_move(board, depth)
print(f"AI가 선택한 최적의 수는: {move}")
