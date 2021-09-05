#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start

from itertools import combinations

class Solution:
    def combine(self, n, k):
        return list(combinations(range(1, n+1), k))

        # 1        1+1          k
        #                       n        
        # 
        #          n-(k-1)+1    
        #                 
        # n-(k-1)

        # @lc code=end
