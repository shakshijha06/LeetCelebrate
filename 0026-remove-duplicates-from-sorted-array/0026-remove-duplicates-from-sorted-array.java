class Solution {
    public int removeDuplicates(int[] nums) {

        int officer = 0;
        int CM = 1;

        while (CM < nums.length) {

            if (nums[CM] != nums[CM - 1]) {
                officer++;
                nums[officer] = nums[CM];
            }

            CM++;
        }

        return officer + 1;
    }
}