#include <iostream>
using namespace std;

int main() {
	// your code goes here
float x,y,z;
cin >>x;
for(int i=0;i<x;i++){
    cin >> y >> z;
    if(z>=y/2)
    cout << "YES\n";
    else
cout << "NO\n";
}
	return 0;
}
