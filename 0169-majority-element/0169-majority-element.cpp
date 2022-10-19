class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> s; int ans = 0;
        for(int i : nums){
             if(++s[i] > nums.size()/2)
                return i;
        }
        return ans;
    }
};