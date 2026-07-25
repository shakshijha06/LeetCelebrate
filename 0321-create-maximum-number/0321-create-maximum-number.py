from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        # Pick the maximum subsequence of length k
        def maxSubsequence(nums, k):
            stack = []
            drop = len(nums) - k

            for num in nums:
                while stack and drop > 0 and stack[-1] < num:
                    stack.pop()
                    drop -= 1

                if len(stack) < k:
                    stack.append(num)
                else:
                    drop -= 1

            return stack

        # Merge two subsequences into the largest possible number
        def merge(a, b):
            ans = []

            while a or b:
                if a > b:
                    ans.append(a.pop(0))
                else:
                    ans.append(b.pop(0))

            return ans

        best = []

        start = max(0, k - len(nums2))
        end = min(k, len(nums1))

        for i in range(start, end + 1):

            part1 = maxSubsequence(nums1, i)
            part2 = maxSubsequence(nums2, k - i)

            candidate = merge(part1[:], part2[:])

            if candidate > best:
                best = candidate

        return best