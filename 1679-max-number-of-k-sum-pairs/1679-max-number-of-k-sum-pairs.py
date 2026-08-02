from collections import defaultdict

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        ans = 0

        for num in nums:
            if freq[k - num] > 0:
                ans += 1
                freq[k - num] -= 1
            else:
                freq[num] += 1

        return ans