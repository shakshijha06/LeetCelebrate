import java.util.*;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        // Sort the array
        Arrays.sort(nums);
        List<List<Integer>> ans = new ArrayList<>();
        
        for (int i = 0; i < nums.length - 2; i++) {
            // Early break: if the smallest element is positive, no triplet can sum to 0
            if (nums[i] > 0) {
                break;
            }
            
            // Skip duplicate first elements
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            
            int left = i + 1;
            int right = nums.length - 1;
            
            while (left < right) {
                int total = nums[i] + nums[left] + nums[right];
                
                if (total == 0) {
                    // Found a valid triplet
                    ans.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    
                    left++;
                    right--;
                    
                    // Skip duplicate left values
                    while (left < right && nums[left] == nums[left - 1]) {
                        left++;
                    }
                    
                    // Skip duplicate right values
                    while (left < right && nums[right] == nums[right + 1]) {
                        right--;
                    }
                    
                } else if (total < 0) {
                    left++; // Need a larger sum
                } else {
                    right--; // Need a smaller sum
                }
            }
        }
        
        return ans;
    }
}