#include <iostream>
#include <vector>
#include <unordered_map>

int main() {
    int n;
    std::cin >> n;

    std::vector<int> array(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> array[i];
    }

    std::vector<std::vector<int>> stack;
    std::unordered_map<int, int> ind;

    for (int i = 0; i < n; ++i) {
        ind[i] = -1;
    }

    for (int i = 0; i < n; ++i) {
        if (stack.empty()) {
            stack.push_back({ array[i], i });
        }
        else if (array[i] < stack.back()[0]) {
            for (int q = stack.size(); q > 0; --q) {
                if (array[i] < stack.back()[0]) {
                    std::vector<int> lst = stack.back();
                    stack.pop_back();
                    ind[lst[1]] = i;
                }
                else {
                    break;
                }
            }
            stack.push_back({ array[i], i });
        }
        else {
            stack.push_back({ array[i], i });
        }
    }

    for (int i = 0; i < n; ++i) {
        std::cout << ind[i] << " ";
    }

    return 0;
}