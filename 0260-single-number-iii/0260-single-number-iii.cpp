class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
    multiset<int> x;
    vector<int> y;
    for(int i=0; i<nums.size(); i++){
        x.insert(nums[i]);
    }
    for(int i=0; i<nums.size(); i++){
        if(x.count(nums[i])==1)
            y.push_back(nums[i]);
        }      
   return y;
    }
};