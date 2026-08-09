class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        # suffix[i] = sum of piles from i to end
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        # dp[i][M]
        dp = [[-1] * (n + 1) for _ in range(n)]

        def solve(i, M):

            # No piles left
            if i == n:
                return 0

            # Already calculated
            if dp[i][M] != -1:
                return dp[i][M]

            best = 0

            # Try taking X piles
            for X in range(1, 2 * M + 1):

                if i + X > n:
                    break

                newM = max(M, X)

                # My stones = remaining - opponent's stones
                current = suffix[i] - solve(i + X, newM)

                best = max(best, current)

            dp[i][M] = best
            return best

        return solve(0, 1)