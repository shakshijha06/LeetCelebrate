import java.util.*;

class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> set = new HashSet<>(nums.length * 2);

        for (int num : nums) {
            set.add(num);
        }

        int longest = 0;

        for (int num : set) {
            if (!set.contains(num - 1)) {
                int curr = num;

                while (set.contains(curr)) {
                    curr++;
                }

                longest = Math.max(longest, curr - num);
            }
        }

        return longest;
    }
}