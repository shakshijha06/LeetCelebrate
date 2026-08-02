from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Prefix sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        dq = deque()      # Stores indices of prefix sums
        ans = n + 1

        for i in range(n + 1):
            # Check if we have a valid subarray
            while dq and prefix[i] - prefix[dq[0]] >= k:
                ans = min(ans, i - dq.popleft())

            # Maintain increasing prefix sums
            while dq and prefix[i] <= prefix[dq[-1]]:
                dq.pop()

            dq.append(i)

        return ans if ans <= n else -1