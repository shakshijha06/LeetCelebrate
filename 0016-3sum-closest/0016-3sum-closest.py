class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        closest = nums[0] + nums[1] + nums[2]

        for k in range(len(nums) - 2):
            if k > 0 and nums[k] == nums[k - 1]:
                continue

            i = k + 1
            j = len(nums) - 1

            while i < j:
                curr_sum = nums[k] + nums[i] + nums[j]

                if abs(curr_sum - target) < abs(closest - target):
                    closest = curr_sum

                if curr_sum == target:
                    return target
                elif curr_sum > target:
                    j -= 1
                else:
                    i += 1

        return closest