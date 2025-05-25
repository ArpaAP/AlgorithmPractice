// AP 11.4 - Knight's Tour
#include <iostream>
#include <vector>
#include <functional>
using namespace std;

int N, M;
int circuits = 0;
vector<pair<int, int>> moves = {{2, 1}, {1, 2}, {-1, 2}, {-2, 1}, {-2, -1}, {-1, -2}, {1, -2}, {2, -1}};

void dfs_circuit(int x, int y, int depth, vector<vector<bool>> &visited)
{
    if (depth == N * M)
    {
        for (auto &move : moves)
        {
            int nx = x + move.first;
            int ny = y + move.second;
            if (nx == 0 && ny == 0)
            {
                circuits++;
                break;
            }
        }
        return;
    }

    for (auto &move : moves)
    {
        int nx = x + move.first;
        int ny = y + move.second;
        if (nx >= 0 && nx < N && ny >= 0 && ny < M && !visited[nx][ny])
        {
            visited[nx][ny] = true;
            dfs_circuit(nx, ny, depth + 1, visited);
            visited[nx][ny] = false;
        }
    }
}

int count_paths(int sx, int sy)
{
    vector<vector<bool>> visited(N, vector<bool>(M, false));
    visited[sx][sy] = true;
    int cnt = 0;

    function<void(int, int, int)> dfs = [&](int x, int y, int depth)
    {
        if (depth == N * M)
        {
            cnt++;
            return;
        }

        for (auto &move : moves)
        {
            int nx = x + move.first;
            int ny = y + move.second;
            if (nx >= 0 && nx < N && ny >= 0 && ny < M && !visited[nx][ny])
            {
                visited[nx][ny] = true;
                dfs(nx, ny, depth + 1);
                visited[nx][ny] = false;
            }
        }
    };

    dfs(sx, sy, 1);
    return cnt;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> M;
    int T;
    cin >> T;

    vector<pair<int, int>> starts(T);
    for (int i = 0; i < T; i++)
    {
        cin >> starts[i].first >> starts[i].second;
    }

    // Count circuits from (0,0)
    vector<vector<bool>> visited(N, vector<bool>(M, false));
    visited[0][0] = true;
    circuits = 0;
    dfs_circuit(0, 0, 1, visited);
    cout << circuits << "\n";

    // Count paths for each starting point
    for (auto &start : starts)
    {
        cout << count_paths(start.first, start.second) << "\n";
    }

    return 0;
}