#include <iostream>
#include <vector>
#include <algorithm>
#define MOD 10007

using namespace std;

int main()
{
    int N, K;
    int prev, tmp;
    cin >> N >> K;

    K = min(K, N - K);

    vector<int> B(K + 1, 0);

    for (int n = 0; n <= N; ++n)
    {
        prev = 1;

        for (int k = 0; k <= min(n, K); ++k)
        {
            if (k == 0)
            {
                B[k] = 1;
            }
            else
            {
                tmp = B[k];
                B[k] = (B[k] + prev) % MOD;
                prev = tmp;
            }
        }
    }

    cout << B[K] << endl;

    return 0;
}
