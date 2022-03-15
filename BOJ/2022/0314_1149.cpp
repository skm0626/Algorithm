#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int n;
	cin >> n;
	int dp[1001][3] = { 0, }; // 0으로 초기화
	for (int i = 1; i <= n; i++) {
		for (int j = 0; j < 3; j++) {
			cin >> dp[i][j];
		}
	}
	for (int i = 1; i <= n; i++) {
		dp[i][0] += min(dp[i - 1][1], dp[i - 1][2]); // i번째 집을 빨강으로 칠할때 최소 비용
		dp[i][1] += min(dp[i - 1][0], dp[i - 1][2]); // i번째 집을 초록으로 ''
		dp[i][2] += min(dp[i - 1][0], dp[i - 1][1]); // i번째 집을 파랑으로 ''
	}
	cout << min(dp[n][0], min(dp[n][1], dp[n][2])); // 3가지 중 가장 작은 수 출력
	return 0;
}
