class Solution {
public:
    int search(vector<int>& nums, int t) {
        int x = 0, y = nums.size()-1;
        while(x<=y){
        int m = (x+y)/2;
        if(nums[m]==t)
            return m;
        if(nums[m]>t)
            y = m-1;
        else
            x = m+1;
        }
     return -1;   
    }
};