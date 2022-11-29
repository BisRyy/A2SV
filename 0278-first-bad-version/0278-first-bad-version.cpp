// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int f = 1, l =n, m;
        while(f<l){
            m = f + (l-f)/2;
            if(!(isBadVersion(m))){
                f=m+1;
            }
            else
                l = m;
        }
        return f;
    }
};