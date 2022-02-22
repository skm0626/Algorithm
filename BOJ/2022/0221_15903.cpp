#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int n, m;
	long long arr[1000]; // long long으로 안해서 계속 틀렸음!
	long long result=0;
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	while (m--) {
		sort(arr, arr + n);
		long long val = arr[0] + arr[1];
		arr[0] = val;
		arr[1] = val;
	}
	for (int j = 0; j < n; j++) {
		result += arr[j];
	}
	cout << result;
}
