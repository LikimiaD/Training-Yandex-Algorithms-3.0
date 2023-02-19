#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;

    std::vector<long long> counts(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> counts[i];
    }

    long long ans = 0;
    for (int i = 0; i < n - 1; ++i) {
        ans += std::min(counts[i], counts[i + 1]);
    }

    std::cout << ans << std::endl;

    return 0;
}