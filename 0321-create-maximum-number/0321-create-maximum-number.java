class Solution {

    public int[] maxNumber(int[] nums1, int[] nums2, int k) {

        int m = nums1.length;
        int n = nums2.length;

        int[] best = new int[k];

        int start = Math.max(0, k - n);
        int end = Math.min(k, m);

        for (int i = start; i <= end; i++) {

            int[] part1 = maxSubsequence(nums1, i);
            int[] part2 = maxSubsequence(nums2, k - i);

            int[] candidate = merge(part1, part2);

            if (greater(candidate, 0, best, 0)) {
                best = candidate;
            }
        }

        return best;
    }

    // Pick maximum subsequence of length k
    private int[] maxSubsequence(int[] nums, int k) {

        int[] stack = new int[k];
        int top = 0;

        int drop = nums.length - k;

        for (int num : nums) {

            while (top > 0 && drop > 0 && stack[top - 1] < num) {
                top--;
                drop--;
            }

            if (top < k) {
                stack[top++] = num;
            } else {
                drop--;
            }
        }

        return stack;
    }

    // Merge two arrays into largest possible number
    private int[] merge(int[] a, int[] b) {

        int[] ans = new int[a.length + b.length];

        int i = 0;
        int j = 0;
        int idx = 0;

        while (i < a.length || j < b.length) {

            if (greater(a, i, b, j)) {
                ans[idx++] = a[i++];
            } else {
                ans[idx++] = b[j++];
            }
        }

        return ans;
    }

    // Compare remaining suffixes
    private boolean greater(int[] a, int i, int[] b, int j) {

        while (i < a.length && j < b.length && a[i] == b[j]) {
            i++;
            j++;
        }

        if (j == b.length) return true;
        if (i == a.length) return false;

        return a[i] > b[j];
    }
}