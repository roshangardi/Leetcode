from typing import List


class Solution:
    def numDecodings(self, s):
        if not s:
            return 0
        print(s)
        n = len(s)
        dp_array = [0] * (n + 1)
        dp_array[0] = 1
        dp_array[1] = 1 if s[0] != '0' else 0
        print(dp_array)
        for i in range(2, n+1):
            first = int(s[i - 1:i])
            second = int(s[i - 2:i])
            print(first, second)
            if 1 <= first <= 9:
                dp_array[i] += dp_array[i - 1]
            if 10 <= second <= 26:
                dp_array[i] += dp_array[i - 2]
            print(dp_array)

        return dp_array[n]


sol = Solution()
print(sol.numDecodings("1204"))
