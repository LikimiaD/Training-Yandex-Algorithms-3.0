#include <iostream>
#include <vector>

void insert(std::vector<int>& heap, int value) {
	heap.push_back(value);
	int index = heap.size() - 1;
	while (index > 0 && heap[index] > heap[(index - 1) / 2]) {
		std::swap(heap[index], heap[(index - 1) / 2]);
		index = (index - 1) / 2;
	}
}

int extract(std::vector<int>& heap) {
	int result = heap[0];
	heap[0] = heap.back();
	heap.pop_back();
	int index = 0;
	while (true) {
		int child = 2 * index + 1;
		if (child >= heap.size()) break;
		if (child + 1 < heap.size() && heap[child + 1] > heap[child]) {
			child++;
		}
		if (heap[index] >= heap[child]) break;
		std::swap(heap[index], heap[child]);
		index = child;
	}
	return result;
}

int main() {
	int n;
	std::cin >> n;
	std::vector<int> heap;
	for (int i = 0; i < n; i++) {
		int operation, value;
		std::cin >> operation;
		if (operation == 0) {
			std::cin >> value;
			insert(heap, value);
		}
		else {
			std::cout << extract(heap) << std::endl;
		}
	}

	return 0;
}