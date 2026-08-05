class Solution:
    def threeSum(self, nums):
        # Sort the array to use the two-pointer approach
        nums.sort()

        n = len(nums)
        result = []

        # Store append() in a variable (slightly faster than repeated lookup)
        append = result.append

        # Fix one element at a time
        for i in range(n - 2):

            # If the current number is positive,
            # all remaining numbers will also be positive (array is sorted),
            # so no triplet can sum to 0.
            if nums[i] > 0:
                break

            # Skip duplicate first elements to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Smallest possible sum with the current number
            # If it's already greater than 0, no need to continue.
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break

            # Largest possible sum with the current number
            # If it's still less than 0, this number can't form a valid triplet.
            if nums[i] + nums[n - 2] + nums[n - 1] < 0:
                continue

            # Initialize two pointers
            left = i + 1
            right = n - 1

            # Store the current fixed element
            first = nums[i]

            # Find the other two numbers
            while left < right:

                total = first + nums[left] + nums[right]

                # Triplet found
                if total == 0:

                    append([first, nums[left], nums[right]])

                    # Move both pointers inward
                    left += 1
                    right -= 1

                    # Skip duplicate values on the left
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate values on the right
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                # Sum is too small → move left pointer to increase the sum
                elif total < 0:
                    left += 1

                # Sum is too large → move right pointer to decrease the sum
                else:
                    right -= 1

        # Return all unique triplets
        return result