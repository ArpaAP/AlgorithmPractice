#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<pair<int, int>> pairs(N);
    for (int i = 0; i < N; ++i)
    {
        cin >> pairs[i].first >> pairs[i].second;
    }

    vector<pair<int, int>> S;

    int endtime = pairs[0].second;
    S.push_back(pairs[0]);

    for (int i = 1; i < N; ++i)
    {
        int s = pairs[i].first;
        int e = pairs[i].second;
        if (s >= endtime)
        {
            endtime = e;
            S.emplace_back(s, e);
        }
    }

    cout << S.size() << endl;
    for (auto &pr : S)
    {
        cout << pr.first << " " << pr.second << endl;
    }

    return 0;
}
