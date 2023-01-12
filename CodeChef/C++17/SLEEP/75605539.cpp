#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int n,x;
	cin >> n;
	for(int i=0; i<n; i++){
	    cin >> x;
	    if(x >= 7)
	        cout << "NO" << endl;
	   else
	     cout << "YES" << endl;
	}
	
	
	return 0;
}
