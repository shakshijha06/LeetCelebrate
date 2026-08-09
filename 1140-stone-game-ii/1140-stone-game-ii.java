class Solution {

    int n;
    int[][] dp;
    int[] suffix;

    int solve(int i, int M) {

        // No piles left
        if (i == n) {
            return 0;
        }

        // Already calculated
        if (dp[i][M] != -1) {
            return dp[i][M];
        }

        int best = 0;

        // Try taking X piles
        for (int X = 1; X <= 2 * M && i + X <= n; X++) {

            int newM = Math.max(M, X);

            // My stones = remaining - opponent's stones
            int current = suffix[i] - solve(i + X, newM);

            best = Math.max(best, current);
        }

        dp[i][M] = best;

        return best;
    }

    public int stoneGameII(int[] piles) {

        n = piles.length;

        suffix = new int[n + 1];

        // Calculate suffix sums
        for (int i = n - 1; i >= 0; i--) {
            suffix[i] = suffix[i + 1] + piles[i];
        }

        dp = new int[n][n + 1];

        // -1 means not calculated
        for (int i = 0; i < n; i++) {
            java.util.Arrays.fill(dp[i], -1);
        }

        return solve(0, 1);
    }
}