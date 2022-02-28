#include <iostream>
using namespace std;

int main() { // 피보나치로 풀어야함!!!아니면 시간초과 뜸
	int n;
	int dp_a[45];
	int dp_b[45];
	cin >> n;
	// 초기:''라고 하고, 한번 누르면'b', 두번 누르면 'ba', 세번누르면 'bab' ...
	dp_a[0] = 0;
	dp_b[0] = 0;
	dp_a[1] = 0;
	dp_b[1] = 1;
	dp_a[2] = 1;
	dp_b[2] = 1;

	for (int i = 3; i <= n; i++) { //초기 0번째도 해줬으니까 for문 n까지 돌려야함
		dp_a[i] = dp_a[i - 1] + dp_a[i - 2];
		dp_b[i] = dp_b[i - 1] + dp_b[i - 2];
	}
	cout << dp_a[n] << " " << dp_b[n];
}
