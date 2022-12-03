class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string ans = "";
        for (int i=0; i< strs[0].size(); i++){
            char x = strs[0][i];
            for(int j=1; j< strs.size(); j++){
                if(x != strs[j][i]){
                    return ans;
                }
            }
            ans+=x;
        }
    return ans;
    }
};