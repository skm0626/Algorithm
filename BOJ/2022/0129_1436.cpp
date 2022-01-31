#include <iostream>
#include <string>
using namespace std;

int main() {
	int n;
	int num = 0;
	cin >> n;
	for (int i = 1; i <= 10000000; i++) { //1부터 최소 입력값이 10,000이기 때문에 적어도 10000666까지라고 가정하고 10000000까지 for문 돌림
		if ((to_string(i).find("666")) != string::npos) { //'666'으로 하면 6이 하나만 들어가도 num값이 올라감!
			num += 1;
		}
		if (num == n) {
			cout << i << endl;
			break;
		}
	}
}
