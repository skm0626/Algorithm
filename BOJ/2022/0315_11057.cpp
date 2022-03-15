#include <iostream>
using namespace std;

int main() {
	int n;
	int dp[1001][10] = { 0, }; //배열 초기화
	int ans = 0;
	cin >> n;
	for (int i = 0; i < 10; i++){
		dp[1][i] = 1;
	}
	for (int i = 2; i <= n; i++) {
		for (int j = 0; j < 10; j++) {
			for (int k = 0; k <= j; k++) {
				dp[i][j] += dp[i - 1][k];
				dp[i][j] = dp[i][j] % 10007; // dp 배열에 큰 수가 들어가는 것을 막기 위해서 미리 10007로 나눠줌(안해주면 틀림)
			}
		}
	}
	for (int i = 0; i < 10; i++) {
		ans += dp[n][i];
	}
	cout << ans % 10007;
	return 0;
}
