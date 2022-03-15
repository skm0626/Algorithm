#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int n;
	int arr[1001];
	int dp[1001];
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	for (int i = 0; i <n; i++) {
		dp[i] = 1;
		for (int j = 0; j < i; j++) {
			if (arr[i] < arr[j] && dp[j]+1 > dp[i]) {
				dp[i] = dp[j] + 1;
			}
		}
	}
  // dp 배열에서 가장 큰 값 찾기
	int m = 0;
	for (int i = 0; i < n; i++) {
		if (dp[i] > m) {
			m = dp[i];
		}
	}
	cout << m;
	return 0;
}
