#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int n;
	cin >> n;
	int a = 300;
	int b = 60;
	int c = 10;
	int numa = 0;
	int numb = 0;
	int numc = 0;

	numa = n / a;
	n = n % a;
	numb = n / b;
	n = n % b;
	numc = n / c;
	n = n % c;

	if (n != 0) {
		cout << -1 << endl;
	}
	else {
		cout << numa << " " << numb << " " << numc;
	}
}
