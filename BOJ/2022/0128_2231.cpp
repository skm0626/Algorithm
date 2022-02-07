#include <iostream>
using namespace std;

int main() {
	int n;
	int a, b,result;
	cin >> n;
	for (int i = 1; i < n+1; i++) { // 자연수 1부터
		a = i;
		b = i;
		while (a > 0) { // 0이 되기 전까지 각 자리수 합 구하기
			b += a % 10;
			a = a / 10;
		}
		if (b == n) { // 해당 수(i)와 각 자리수 합이 입력값과 같으면 해당 수(i)가 입력값의 생성자!
			cout << i<< endl;
			break;
		}
	}
	if (b != n) { // 생성자 없음
		cout << "0" << endl;
	}

}
