#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool desc(int a, int b) {
	return a > b;
}

int main() {
	int n, m;
	vector<int> height(300000); //그냥 int로 하니까 에러났음
	vector<int> diff(300000);
	int sum = 0;
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		cin >> height[i];
	}
	for (int j = 0; j < n - 1; j++) {
		diff[j] = height[j + 1] - height[j];
	}
	sort(diff.begin(), diff.end(), desc); //키 차이들을 내림차순으로 정렬
	for (int i = 0; i < n-m; i++) { // 이 부분 헷갈렸음
		sum += diff[m - 1 + i]; // 'm-1'은 인덱스 계산을 위한 것
	}
	cout << sum;
}
