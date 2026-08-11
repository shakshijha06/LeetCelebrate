#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* maxSlidingWindow(int* nums, int numsSize, int k, int* returnSize) {
    
    *returnSize = numsSize - k + 1;
    
    int* result = (int*)malloc((*returnSize) * sizeof(int));
    
    // Deque stores indices
    int* deque = (int*)malloc(numsSize * sizeof(int));
    
    int front = 0;
    int back = 0;
    int resultIndex = 0;
    
    for (int i = 0; i < numsSize; i++) {
        
        // 1. Remove indices outside the window
        if (front < back && deque[front] <= i - k) {
            front++;
        }
        
        // 2. Remove smaller elements from the back
        while (front < back && nums[deque[back - 1]] <= nums[i]) {
            back--;
        }
        
        // 3. Add current index
        deque[back++] = i;
        
        // 4. Window is ready
        if (i >= k - 1) {
            result[resultIndex++] = nums[deque[front]];
        }
    }
    
    free(deque);
    
    return result;
}