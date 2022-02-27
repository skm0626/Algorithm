#include <iostream>
#include <string>
using namespace std;

int main() {
	string n,m;
	int ans = 0;
	getline(cin,n); //예시가 'a a a'가 있는데 cin으로만 하면 공백으로 처리되어서 다음m입력으로 받아버림
	getline(cin,m);
	for (int i = 0; i < n.length(); i++) {
		bool flag = true;
		for (int j = 0; j < m.length(); j++) {
			if (n[i+j] != m[j]) { //여기가 중요!!!
				flag = false;
				break;
			}
		}
		if (flag == true) {
			ans += 1;
			i += m.length() - 1; //m의 길이만큼 더해서 다시 탐색
		}
	}
	cout << ans;
}
