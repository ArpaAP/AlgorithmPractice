N, r, c = map(int, input().split())

# 아직 채워지지 않은 칸은 -1로 초기화하고, 구멍 위치는 0으로 표시
board = [[-1 for _ in range(N)] for _ in range(N)]
board[r][c] = 0

count = 0


def tromino(top, left, n, missing_r, missing_c):
    global count

    # 영역이 2x2이면, 구멍을 제외한 나머지 3칸에 같은 번호를 채움
    if n == 2:
        count += 1
        for i in range(top, top + n):
            for j in range(left, left + n):
                if i == missing_r and j == missing_c:
                    continue
                board[i][j] = count
        return

    h = n // 2

    if missing_r < top + h:
        if missing_c < left + h:
            missing_quad = 0  # 왼쪽 위
        else:
            missing_quad = 1  # 오른쪽 위
    else:
        if missing_c < left + h:
            missing_quad = 2  # 왼쪽 아래
        else:
            missing_quad = 3  # 오른쪽 아래

    # 중앙에 놓을 트로미노 (3칸)를 한 번의 count 번호로 채움
    count += 1
    # 각 사분면에 가상의 구멍(트로미노를 놓은 자리)을 만들어 줌
    if missing_quad != 0:
        board[top + h - 1][left + h - 1] = count
    if missing_quad != 1:
        board[top + h - 1][left + h] = count
    if missing_quad != 2:
        board[top + h][left + h - 1] = count
    if missing_quad != 3:
        board[top + h][left + h] = count

    # 각 사분면에 대해 재귀 호출을 수행
    # 재귀 호출 시, 각 사분면의 구멍 좌표는 원래 구멍이 있던 곳 또는 중앙에 놓은 트로미노 칸이 된다.

    # top-left
    if missing_quad == 0:
        tromino(top, left, h, missing_r, missing_c)
    else:
        tromino(top, left, h, top + h - 1, left + h - 1)

    # top-right
    if missing_quad == 1:
        tromino(top, left + h, h, missing_r, missing_c)
    else:
        tromino(top, left + h, h, top + h - 1, left + h)

    # bottom-left
    if missing_quad == 2:
        tromino(top + h, left, h, missing_r, missing_c)
    else:
        tromino(top + h, left, h, top + h, left + h - 1)

    # bottom-right
    if missing_quad == 3:
        tromino(top + h, left + h, h, missing_r, missing_c)
    else:
        tromino(top + h, left + h, h, top + h, left + h)


# 전체 보드(0,0)에서 시작하여 N×N 영역을 채우기.
tromino(0, 0, N, r, c)

# 최종 결과 출력
for row in board:
    print(*row)
