#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int n,x,y,z;
	cin >> n;
	for(int i=0; i<n; i++){
	    cin >> x ;
	    cin >> y ;
	    cin >> z;
	    int a = x*y*z;
	    cout << a << endl;
	}
	return 0;
}
