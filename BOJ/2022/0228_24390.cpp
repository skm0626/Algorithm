#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main() {
	string n;
	int second, answer;
	cin >> n;
	second = stoi(n.substr(0, 2)) * 60 + stoi(n.substr(3, 2));

	if (second == 0) { cout << 0; return 0; }
	if (0 < second && second < 30) { 
		answer = second / 10; 
		answer += 1;//조리시작(0초) 버튼 
	}
	else if (second < 60) {
		answer = (second - 30) / 10 + 1; //조리시작(0초) 버튼 
	}
	else { 
		if (stoi(n.substr(3, 2)) < 30) { // 30초 보다 작으면 조리시작(30초 역할)을 쓸 필요가 없음
			answer = second / 600 + (second % 600) / 60 + ((second % 600) % 60) / 10;
			answer += 1; //조리시작(0초) 버튼
		}
		else { //조리시작 버튼이 30초 역할을 해야할 때 -> 즉, 초단위가 30초보다 크면 30초를 써야 이득
			answer = second / 600 + (second % 600) / 60 + ((second % 600) % 60) / 30 + (((second % 600) % 60) % 30) / 10;
		}
	}
	cout << answer;
}
