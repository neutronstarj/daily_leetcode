/*
 * @lc app=leetcode id=77 lang=cpp
 *
 * [77] Combinations
 */

// @lc code=start

class Solution {
private:
    vector<vector<int>> result; // save the real result
    vector<int> path; // tempaorary save the result
    void backtracking(int n, int k, int startIndex) {
        if (path.size() == k) {
            result.push_back(path);
            return; // when path[1,2] two element which is k element
        }
        for (int i = startIndex; i <= n; i++) {
            path.push_back(i); 
            backtracking(n, k, i + 1); // next layer
            path.pop_back(); // backtracking, remove the changes
        }
    }
public:
    vector<vector<int>> combine(int n, int k) {
        result.clear(); // 可以不写
        path.clear();   // 可以不写
        backtracking(n, k, 1);
        return result;
    }
};


// @lc code=end


