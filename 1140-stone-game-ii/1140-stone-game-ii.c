#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int n;
int **dp;
int *suffix;

int max(int a, int b) {
    return a > b ? a : b;
}

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

        int newM = max(M, X);

        // My stones = remaining - opponent's stones
        int current = suffix[i] - solve(i + X, newM);

        best = max(best, current);
    }

    dp[i][M] = best;

    return best;
}

int stoneGameII(int* piles, int pilesSize) {

    n = pilesSize;

    // Create suffix array
    suffix = (int*)calloc(n + 1, sizeof(int));

    for (int i = n - 1; i >= 0; i--) {
        suffix[i] = suffix[i + 1] + piles[i];
    }

    // Create DP table
    dp = (int**)malloc(n * sizeof(int*));

    for (int i = 0; i < n; i++) {

        dp[i] = (int*)malloc((n + 1) * sizeof(int));

        for (int j = 0; j <= n; j++) {
            dp[i][j] = -1;
        }
    }

    int answer = solve(0, 1);

    // Free memory
    for (int i = 0; i < n; i++) {
        free(dp[i]);
    }

    free(dp);
    free(suffix);

    return answer;
}