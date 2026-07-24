class Solution {
    public int removeDuplicates(int[] nums) {

        int officer = 0;
        for(int CM=1;CM<nums.length;CM++)
        {
            if (nums[CM]!=nums[CM-1])
            {
                officer++;
                nums[officer]=nums[CM];
            }
        }
        return officer+1;
    }
}