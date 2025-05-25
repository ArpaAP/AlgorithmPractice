# AP 11.4 - Knight's Tour
import sys

sys.setrecursionlimit(10**7)


def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    T = int(input())
    starts = [tuple(map(int, input().split())) for _ in range(T)]
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

    # Count circuits from (0,0)
    sx0, sy0 = 0, 0
    visited = [[False] * M for _ in range(N)]
    visited[sx0][sy0] = True
    circuits = 0

    def dfs_circ(x, y, depth):
        nonlocal circuits
        if depth == N * M:
            for dx, dy in moves:
                if x + dx == sx0 and y + dy == sy0:
                    circuits += 1
                    break
            return
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs_circ(nx, ny, depth + 1)
                visited[nx][ny] = False

    dfs_circ(sx0, sy0, 1)
    print(circuits)

    def count_paths(sx, sy):
        visited2 = [[False] * M for _ in range(N)]
        visited2[sx][sy] = True
        cnt = 0

        def dfs(x, y, depth):
            nonlocal cnt
            if depth == N * M:
                cnt += 1
                return
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and not visited2[nx][ny]:
                    visited2[nx][ny] = True
                    dfs(nx, ny, depth + 1)
                    visited2[nx][ny] = False

        dfs(sx, sy, 1)
        return cnt

    for sx, sy in starts:
        print(count_paths(sx, sy))


if __name__ == "__main__":
    main()
