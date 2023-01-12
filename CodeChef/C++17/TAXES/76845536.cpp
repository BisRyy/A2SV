#include <iostream>
using namespace std;

int main() {
	// your code goes here
int x,y;
cin >> x;
for(int i=0;i<x;i++){
    cin >> y;
    if(y>100)
    y-=10;
    cout << y << endl;
    
}
	return 0;
}
