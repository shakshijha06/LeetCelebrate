class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique=1
        officer=0
        CM=1
        while(CM<len(nums)):
            if (nums[CM]==nums[CM-1]):
                CM+=1
            else:
                
                officer+=1
                nums[officer]=nums[CM]
                unique+=1
                CM+=1
        return unique


        