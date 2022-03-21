#include <iostream>
#include <string>
#include <queue>

using namespace std;

int main() {
	string arr[101]; // 미로
	int dist[101][101]; // 이동 거리
	bool chk[101][101]; // 방문 체크

	queue<pair<int, int> > Q;
	int n, m;

	cin >> n >> m;

	int dx[4] = { 0,0,1,-1 };
	int dy[4] = { 1,-1,0,0 };

	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}

	dist[0][0] = 1;
	Q.push({ 0,0 });
	chk[0][0] = 1;

	while (!Q.empty()) {

		pair<int, int> cur = Q.front();
		Q.pop();

		for (int i = 0; i < 4; i++) {
			int nx = cur.first + dx[i];
			int ny = cur.second + dy[i];

			if (0 <= nx && nx < n && 0 <= ny && ny < m && arr[nx][ny] == '1' && chk[nx][ny] == 0){
                dist[nx][ny] = dist[cur.first][cur.second] + 1;
                Q.push({ nx,ny });
                chk[nx][ny] = 1;
            }
		}
	}
	cout << dist[n - 1][m - 1];
	return 0;
}
