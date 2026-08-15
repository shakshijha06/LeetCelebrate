#include <stdlib.h>
#include <string.h>

void backtrack(char **ans, int *returnSize, char *str,
               int pos, int open, int close, int n) {

    // Complete valid string
    if (pos == 2 * n) {
        str[pos] = '\0';
        ans[*returnSize] = malloc((2 * n + 1) * sizeof(char));
        strcpy(ans[*returnSize], str);
        (*returnSize)++;
        return;
    }

    // Add '('
    if (open < n) {
        str[pos] = '(';
        backtrack(ans, returnSize, str,
                  pos + 1, open + 1, close, n);
    }

    // Add ')'
    if (close < open) {
        str[pos] = ')';
        backtrack(ans, returnSize, str,
                  pos + 1, open, close + 1, n);
    }
}

char** generateParenthesis(int n, int* returnSize) {

    *returnSize = 0;

    // Maximum possible number of valid combinations for n <= 8
    char **ans = malloc(1430 * sizeof(char *));

    char *str = malloc((2 * n + 1) * sizeof(char));

    backtrack(ans, returnSize, str, 0, 0, 0, n);

    free(str);

    return ans;
}