#include <iostream>
#include <vector>

int main() {
    int n, k;
    std::cin >> n >> k;

    std::vector<long long> LIST(n + 1, 0);
    LIST[1] = 1;

    for (int i = 2; i <= n; i++) {
        for (int j = 1; j <= k; j++) {
            if (i - j >= 1) {
                LIST[i] += LIST[i - j];
            }
        }
    }

    std::cout << LIST[n] << std::endl;
    return 0;
}