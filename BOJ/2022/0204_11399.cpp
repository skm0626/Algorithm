#include <iostream>
#include <algorithm>
using namespace std;

int main() {
   int n;
    int sum=0;
   cin >> n;
   int num[1000];
   for (int i = 0; i < n; i++) {
      cin >> num[i];
   }
   sort(num, num + n); //1,2,3,3,4
    for (int i=0;i<n;i++){
        sum += (num[i] *(n-i));
    }
    cout << sum <<endl;
}
