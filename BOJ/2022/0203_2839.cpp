#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int n;
	int ans=0;
	cin >> n;
	while (n >= 0) {
		if (n % 5 == 0) { // n이 5의 배수이면 몫이 정답이고 while문 끝냄
			ans += n/5;
			break;
		}
		else {
			n = n - 3; //5의 배수가 아니면 3을 빼줌
			if (n >= 0) { // 3을 뺐을 때 n이 0 이상이면 아직 설탕봉지가 있는 거니까 일단 3봉지짜리 +1
				ans += 1; 
			}
			else { // n이 0보다 작아지면 3,5봉지로 나눠떨어지지 않은거라서 -1
				ans = -1;
			}
		}
	}
	cout << ans << endl;
}
