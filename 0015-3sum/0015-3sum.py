class Solution:
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        result = []
        append = result.append

        for i in range(n - 2):

            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break

            if nums[i] + nums[n - 2] + nums[n - 1] < 0:
                continue

            left = i + 1
            right = n - 1
            first = nums[i]

            while left < right:
                total = first + nums[left] + nums[right]

                if total == 0:
                    append([first, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result