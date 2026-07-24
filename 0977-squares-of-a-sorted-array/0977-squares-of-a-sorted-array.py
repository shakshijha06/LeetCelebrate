class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left=0
        right=len(nums)-1
        ans=[0]*len(nums)
        idx=len(nums)-1
        while left<=right:
            if abs(nums[left])>abs(nums[right]):
                ans[idx]=nums[left]*nums[left]
                left+=1
            else:
                ans[idx]=nums[right]*nums[right]
                right-=1
            idx-=1
        return ans
