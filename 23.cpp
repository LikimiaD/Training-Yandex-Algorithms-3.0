#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int n;
    std::cin >> n;

    std::vector<int> dp(n + 1, 0);
    std::vector<int> trash(n + 1, 0);

    for (int i = 2; i <= n; i++) {
        dp[i] = dp[i - 1] + 1;
        trash[i] = i - 1;
        if (i % 2 == 0 && dp[i / 2] + 1 < dp[i]) {
            dp[i] = dp[i / 2] + 1;
            trash[i] = i / 2;
        }
        if (i % 3 == 0 && dp[i / 3] + 1 < dp[i]) {
            dp[i] = dp[i / 3] + 1;
            trash[i] = i / 3;
        }
    }

    std::vector<int> path;
    int i = n;
    while (i != 1) {
        path.push_back(i);
        i = trash[i];
    }
    path.push_back(1);
    reverse(path.begin(), path.end());

    std::cout << dp[n] << std::endl;
    for (int x : path) {
        std::cout << x << " ";
    }
    std::cout << std::endl;

    return 0;
}