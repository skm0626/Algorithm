#include <iostream>
#include <algorithm>
using namespace std;

bool desc(int a,int b){
    return a>b;
}
int main() {
   int n;
    int maximum=0;
   cin >> n;
   int rope[100000]; // 로프의 최대 입력 수 10,000
   for (int i = 0; i < n; i++) {
      cin >> rope[i];
   }
   sort(rope, rope + n,desc); // 내림차순으로 정렬
    for (int i=0;i<n;i++){
        maximum = max(maximum, rope[i]*(i+1));
        // 예) 40, 16, 10이 있다면 40짜리는 최대 40을 버틸 수 있고 나머지 줄은 못 버팀 -> 답:40
        // 16은 40,16짜리가 버틸 수 있음 -> 답 : 16*2 = 32
        // 10은 40,16,10이 모두 버틸 수 있음 -> 답 : 10*3 = 30
    }
   cout << maximum << endl;
}
