#include <iostream>
using namespace std;

int main() {
	int a, b;
	int re, answer=0;
	cin >> a >> b;
	int li[100];
	for (int i = 0; i < a; i++) {
		cin >> li[i];
	}
	for (int i = 0; i < a - 2; i++) {
		for (int j = i+1; j < a-1; j++) {
			for (int k = j+1; k < a; k++) {
				re = li[i] + li[j] + li[k];
				if (re == b) {
					answer = b;
					break;
				}
				else if (re < b && re >answer) {
					answer = re;
				}
				else {
					continue;
				}
			}
		}
	}
	cout << answer;
}
