#include <iostream>
#include <algorithm>
using namespace std;

int n;
int max_result = -9999999999; //가장 작은수를 max로 설정
int min_result = 9999999999; //가장 큰수를 max로 설정
int arr[11]; // 개수는 2~11개
int cal_arr[4]; // 차례대로 +,-,*,/ 개수가 들어감

void dfs(int plus, int minus, int multi, int div, int sum, int cnt) { // sum은 연산되는 값의 결과
	if (cnt==n) { // cnt가 수의 개수(n)과 같아지면, 즉 수들이 다 연산되면 max,min을 구함
		max_result = max(max_result, sum);
		min_result = min(min_result, sum);
	}
	if (plus > 0) { dfs(plus - 1, minus, multi, div, sum + arr[cnt], cnt + 1); } // sum + arr[cnt]로 '+'해주고 plus개수는 -1해줌, 그리고 cnt는 +1해서 arr의 다음 수로 가도록!
	if (minus > 0) { dfs(plus, minus - 1, multi, div, sum - arr[cnt], cnt + 1); }
	if (multi > 0) { dfs(plus, minus, multi-1 , div, sum * arr[cnt], cnt + 1); }
	if (div > 0) { dfs(plus, minus, multi, div-1, sum / arr[cnt], cnt + 1); }
}

int main() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	for (int j = 0; j < 4; j++) {
		cin >> cal_arr[j];
	}
	dfs(cal_arr[0], cal_arr[1], cal_arr[2], cal_arr[3], arr[0], 1);
	cout << max_result << endl;
	cout << min_result << endl;
}
