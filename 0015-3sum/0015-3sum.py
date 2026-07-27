class Solution:
    def threeSum(self, nums):
        nums.sort()#sort the array
        n = len(nums)
        result = []
        

        for i in range(n - 2):#fixing one element 

            if i > 0 and nums[i] == nums[i - 1]:#skipping duplicate element
                continue
          

            left = i + 1
            right = n - 1
#finifng two elemnt whose sum with num[i] is 0
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                

                if total == 0:   #Found a valid triplet

                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Skip duplicate values on the left
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Skip duplicate values on the right

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                # Sum is too small, increase it
                elif total < 0:
                    left += 1
                  # Sum is too large, decrease it
                else:
                    right -= 1

        return result