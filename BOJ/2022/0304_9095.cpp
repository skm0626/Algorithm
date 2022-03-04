#include <iostream>
using namespace std;

int main() {
	int T,n;
	int dp[12];
	cin >> T;
	dp[1] = 1; // n=1일 때 1 ->1개
	dp[2] = 2; // n=2일 때 (1+1), 2 -> 2개
	dp[3] = 4; // n=3일 때  (1+1+1), (1+2), (2+1), 3 -> 4개
	for (int i = 4; i < 12; i++) { 
		// n 번째에서 1, 2, 3의 합으로 이루어진 경우는
		//	n - 1 번째에서 각각의 값에 1을 더하는 경우
		//	n - 2 번째에서 각각의 값에 2를 더하는 경우
		//	n - 3 번째에서 각각의 값에 3을 더하는 경우로 나타낼 수 있음
		dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
	}
	for (int i = 0; i < T; i++) {
		cin >> n;
		cout << dp[n] << endl;
	}
	return 0;
}
