class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        k%=nums.size();
        vector<int> temp = nums;
        if(nums.size()>k){
            for(int i=0; i<k;++i){
                temp[i] = nums[nums.size()-k+i];
            }
            for(int i=0; i<nums.size()-k;++i){
                temp[k+i] = nums[i];
            }
            nums = temp;
        }
    }
};