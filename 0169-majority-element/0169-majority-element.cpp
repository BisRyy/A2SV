class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> s; int ans = 0;
        for(int i : nums){
           s[i]++;
        }
        for(auto x: nums){
            if(s[x] > nums.size()/2)
                return x;
        }
        return ans;
    }
};