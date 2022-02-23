#include <iostream>
#include <algorithm>
#include <stack>
using namespace std;

int main() {
	int n, m;
	cin >> n >> m;
	int set[50];
	int single[50];
	int answer = 0;
	for (int i = 0; i < m; i++) {
		cin >> set[i] >> single[i];
	}
	sort(set, set + m);
	sort(single, single + m);

	if (n <= 6) {
		cout << min(set[0], single[0] * n);
	}
	else {
		cout << min(min((n / 6)*set[0] + (n % 6)*single[0], ((n / 6) + 1)*set[0]),n*single[0]);
	}
}
