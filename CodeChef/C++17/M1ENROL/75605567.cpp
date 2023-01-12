#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int n,x,y,z;
	cin >> n;
	for( int i=0; i<n;i++){
	    cin >> x;
	    cin >> y;
	    z = y - x;
	    y>x ?cout<<z:cout<<0;
	    cout << endl;
	    
	}
	return 0;
}
