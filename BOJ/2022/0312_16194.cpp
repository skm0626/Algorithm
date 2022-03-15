#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int n;
	int dp[1001];
	cin >> n;
	for (int i = 1; i <= n; i++) {
		cin >> dp[i];
	}
	for (int i = 2; i <=n; i++) { 
		for (int j = 1; j < i; j++) {
			dp[i] = min(dp[i],dp[i-j]+dp[j]); // 앞의 값들을 이용해 비교하면서 최소값 찾아내기
		}
	}
	cout << dp[n];
	return 0;
}
