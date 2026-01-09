class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        
        n = len(text2)
        dp = [0] * (n+1)

        for i in range(1, len(text1)+1):
            cur = [0] * (n+1)
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    cur[j] = dp[j - 1]+1
                else:
                    cur[j] = max(dp[j], cur[j-1])
            dp = cur
        
        return dp[n]


        
