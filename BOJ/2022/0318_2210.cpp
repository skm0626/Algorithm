#include <iostream>
using namespace std;

int n;
int MAP[5][5];
bool check[1000000]; // 만들어지는 5자리 숫자가 중복되는 것을 막기 위해 결과값 중복체크
int ans = 0; //최종 정답

int dx[] = { 0,0,1,-1 }; //좌우 이동
int dy[] = { 1,-1,0,0 }; //상하 이동

void DFS(int x, int y, int sum, int cnt) {
	if (cnt == 5) { // 5번 이동 완료
		if (check[sum] == false) { //증복되는 값이 아니라면
			check[sum] = true; // true로 체크
			ans += 1;
		}
		return;
	}

	for (int i = 0; i < 4; i++) { //nx, ny의 길이가 4니까 0~3까지
		// 상하좌우를 통해 새로운 곳으로 좌표 이동
		int nx = x + dx[i]; 
		int ny = y + dy[i];
		if (nx >= 0 && ny >= 0 && nx < 5 && ny < 5)
		{
			DFS(nx, ny, sum * 10 + MAP[nx][ny], cnt + 1);
		}
	}
}

int main() {
	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < 5; j++) {
			cin >> MAP[i][j];
		}
	}
	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < 5; j++) {
			DFS(i, j, MAP[i][j], 0);
		}
	}
	cout << ans;
	return 0;
}
