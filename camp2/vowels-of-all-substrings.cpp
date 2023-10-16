class Solution {
    bool v[26] = {1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0};
    
public:
    long long countVowels(string w) {
        long long ans = 0, size = w.size();
        for (int i = 0; i < w.size(); ++i)
            ans += v[w[i] - 'a'] * (i + 1) * (size - i);
        return ans;
    }
};