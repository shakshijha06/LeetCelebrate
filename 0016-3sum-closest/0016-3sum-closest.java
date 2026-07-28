class Solution {
    public int threeSumClosest(int[] nums, int target) {

        Arrays.sort(nums);

        int closest = nums[0] + nums[1] + nums[2];

        for (int k = 0; k < nums.length - 2; k++) {

            if (k > 0 && nums[k] == nums[k - 1])
                continue;

            int i = k + 1;
            int j = nums.length - 1;

            while (i < j) {

                int sum = nums[k] + nums[i] + nums[j];

                if (Math.abs(sum - target) < Math.abs(closest - target)) {
                    closest = sum;
                }

                if (sum == target) {
                    return target;
                } else if (sum > target) {
                    j--;
                } else {
                    i++;
                }
            }
        }

        return closest;
    }
}