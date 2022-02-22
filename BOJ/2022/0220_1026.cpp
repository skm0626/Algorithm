#include <iostream>
#include <algorithm>
using namespace std;

bool desc(int a, int b) {
	return a > b;
}

int main() {
	int n;
	int arr_a[50];
	int arr_b[50];
	int result=0;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> arr_a[i];
	}
	for (int j = 0; j < n; j++) {
		cin >> arr_b[j];
	}
	sort(arr_a, arr_a + n);
	sort(arr_b, arr_b + n, desc);

	for (int k = 0; k < n; k++) {
		result += arr_a[k] * arr_b[k];
	}
	cout << result;
}
