// 6-1
// LCS (Longest Common Subsequence)

#include <iostream>
#include <string>
#include <vector>

using namespace std;

using Matrix = vector<vector<int> >;

string X, Y;
Matrix C, B;

int dp(int i, int j) {
    if (i == -1 || j == -1) return 0;

    if (C[i][j] > -1) return C[i][j];

    int r;

    if (X[i] == Y[j]) {
        r = 1 + dp(i - 1, j - 1);
        B[i][j] = 0;
    } else {
        int a = dp(i - 1, j);
        int b = dp(i, j - 1);

        r = max(a, b);
        B[i][j] = a >= b ? 1 : 2;
    }

    C[i][j] = r;
    return r;
}

void print_lcs(int i, int j) {
    if (i == -1 || j == -1) return;

    if (B[i][j] == 1) {
        print_lcs(i - 1, j);
    } else if (B[i][j] == 2) {
        print_lcs(i, j - 1);
    } else {
        print_lcs(i - 1, j - 1);
        cout << X[i];
    }
}

int main() {
    getline(cin, X);
    getline(cin, Y);

    C = Matrix(X.length(), vector<int>(Y.length(), -1));
    B = Matrix(X.length(), vector<int>(Y.length()));

    int n = X.length() - 1;
    int m = Y.length() - 1;

    int r = dp(n, m);

    cout << r << endl;

    print_lcs(n, m);
    cout << endl;
}
