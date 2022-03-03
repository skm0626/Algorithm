#include <iostream>
using namespace std;

int main() {
	int n;
	cin >> n;
	if (n % 2 == 0) { //가져가는 돌의 개수가 1,3개로 홀수임 -> 돌의 개수가 홀수면 '상근', 짝수이면 '창영'이가 게임을 이김
		cout << "CY";
	}
	else {
		cout << "SK";
	}
	return 0;
}
