class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        officer=0
        for CM in range(1,len(nums)):
            if nums[CM]!=nums[CM-1]:
                officer+=1
                nums[officer]=nums[CM]
        return officer +1
            
        