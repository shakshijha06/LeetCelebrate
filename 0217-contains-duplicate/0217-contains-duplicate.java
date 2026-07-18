import java.util.HashSet;

class Solution {
    public boolean containsDuplicate(int[] nums) {

        HashSet<Integer> seen = new HashSet<>();

        for (int x : nums) {
            if (seen.contains(x)) {
                return true;
            }

            seen.add(x);
        }

        return false;
    }
}