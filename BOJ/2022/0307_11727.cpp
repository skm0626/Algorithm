#include <iostream>
using namespace std;
// https://dontdiethere.tistory.com/64 참고

int main() {
	int n;
	int dp[1001];
	cin >> n;
	dp[1] = 1; 
	dp[2] = 3; 
	dp[3] = 5; 
	for (int i = 4; i <= n; i++) { 
		dp[i] = (dp[i - 1] + dp[i - 2] * 2) % 10007;
	}
	cout << dp[n];
	return 0;
}
