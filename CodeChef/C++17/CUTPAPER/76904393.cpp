#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int x,y,z;
	cin >> x;
	for(int i=0; i<x; i++){
	    cin >> y >> z;
	    cout << abs(y/z) * abs(y/z) << endl;
	    
	}
	return 0;
}
