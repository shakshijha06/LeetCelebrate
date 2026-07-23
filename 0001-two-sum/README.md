<h2><a href="https://leetcode.com/problems/two-sum">1. Two Sum</a></h2><h3>Easy</h3><hr><p>Given an array of integers <code>nums</code>&nbsp;and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.</p>

<p>You may assume that each input would have <strong><em>exactly</em> one solution</strong>, and you may not use the <em>same</em> element twice.</p>

<p>You can return the answer in any order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,7,11,15], target = 9
<strong>Output:</strong> [0,1]
<strong>Explanation:</strong> Because nums[0] + nums[1] == 9, we return [0, 1].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,4], target = 6
<strong>Output:</strong> [1,2]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,3], target = 6
<strong>Output:</strong> [0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>

<h1>Two Sum | Brute Force → Two Pointer → One-Pass Hash Map</h1>

<h2>Intuition</h2>

<p>There are multiple ways to solve this problem, with each approach improving upon the previous one.</p>

<ul>
    <li><b>Brute Force:</b> Check every possible pair of elements and return the indices whose sum equals the target.</li>
    <li><b>Two Pointer:</b> Sort the array while preserving the original indices, then use two pointers to efficiently search for the target sum.</li>
    <li><b>One-Pass Hash Map:</b> Store each visited element in a hash map. For every element, check whether its complement (<code>target - current</code>) has already been seen. This achieves the optimal time complexity.</li>
</ul>

<hr>

<h2>Approach</h2>

<h2>Solution 1: Brute Force</h2>

<p>
The simplest approach is to iterate through every pair of elements using two nested loops.
If the sum of a pair equals the target, return their indices.
</p>

<h3>Java</h3>

```java
class Solution {
    public int[] twoSum(int[] nums, int target) {

        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {

                if (nums[i] + nums[j] == target) {
                    return new int[]{i, j};
                }
            }
        }

        return new int[]{};
    }
}
```
<h3>Python</h3>

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):

                if nums[i] + nums[j] == target:
                    return [i, j]

        return []
```

<h4>Complexity</h4>

<ul>
<li><b>Time Complexity:</b> O(n²)</li>
<li><b>Space Complexity:</b> O(1)</li>
</ul>

<h4>Advantages</h4>

<ul>
<li>Very simple and easy to implement.</li>
<li>Does not require any extra data structures.</li>
<li>Preserves the original array without modification.</li>
</ul>

<h4>Disadvantages</h4>

<ul>
<li>Inefficient for large input sizes due to quadratic time complexity.</li>
<li>Performs many unnecessary comparisons.</li>
</ul>

<hr>

<h2>Solution 2: Two Pointer</h2>

<p>
Sort the array while storing each element's original index.
Then use two pointers to find the required sum.
If the current sum is smaller than the target, move the left pointer; otherwise, move the right pointer.
</p>

<h3>Java</h3>

```java
import java.util.*;

class Solution {
    public int[] twoSum(int[] nums, int target) {

        int n = nums.length;
        int[][] arr = new int[n][2];

        for (int i = 0; i < n; i++) {
            arr[i][0] = nums[i];
            arr[i][1] = i;
        }

        Arrays.sort(arr, Comparator.comparingInt(a -> a[0]));

        int left = 0;
        int right = n - 1;

        while (left < right) {

            int sum = arr[left][0] + arr[right][0];

            if (sum == target) {
                return new int[]{arr[left][1], arr[right][1]};
            }

            if (sum < target) {
                left++;
            } else {
                right--;
            }
        }

        return new int[]{};
    }
}
```

<h3>Python</h3>

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        arr = [(num, idx) for idx, num in enumerate(nums)]
        arr.sort()

        left = 0
        right = len(arr) - 1

        while left < right:

            curr_sum = arr[left][0] + arr[right][0]

            if curr_sum == target:
                return [arr[left][1], arr[right][1]]

            elif curr_sum < target:
                left += 1

            else:
                right -= 1

        return []
```

<h4>Complexity</h4>

<ul>
<li><b>Time Complexity:</b> O(n log n)</li>
<li><b>Space Complexity:</b> O(n)</li>
</ul>

<h4>Advantages</h4>

<ul>
<li>More efficient than the brute force approach.</li>
<li>The two-pointer technique reduces the search to a single pass after sorting.</li>
</ul>

<h4>Disadvantages</h4>

<ul>
<li>Sorting changes the original order, so original indices must be stored separately.</li>
<li>Higher space usage compared to brute force.</li>
<li>Slower than the hash map approach because of the sorting step.</li>
</ul>

<hr>

<h2>Solution 3: One-Pass Hash Map (Optimal)</h2>

<p>
Use a hash map to store each number and its index while traversing the array.
For every element, compute its complement (<code>target - current</code>).
If the complement already exists in the hash map, return both indices.
Otherwise, store the current element and continue.
</p>

<h3>Java</h3>

```java
class Solution {
    public int[] twoSum(int[] nums, int target) {

        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {

            int complement = target - nums[i];

            if (map.containsKey(complement)) {
                return new int[]{map.get(complement), i};
            }

            map.put(nums[i], i);
        }

        return new int[]{};
    }
}
```

<h3>Python</h3>

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i, num in enumerate(nums):

            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i

        return []
```

<h4>Complexity</h4>

<ul>
<li><b>Time Complexity:</b> O(n)</li>
<li><b>Space Complexity:</b> O(n)</li>
</ul>

<h4>Advantages</h4>

<ul>
<li>Optimal time complexity with a single traversal.</li>
<li>Constant-time average lookup using a hash map.</li>
<li>Preserves the original order of the array.</li>
<li>Simple and efficient for large inputs.</li>
</ul>

<h4>Disadvantages</h4>

<ul>
<li>Requires additional memory to store the hash map.</li>
<li>Performance depends on the efficiency of the hash table implementation (average O(1) lookups).</li>
</ul>

<hr>

<h2>Comparison</h2>

<table>
<thead>
<tr>
<th>Approach</th>
<th>Time Complexity</th>
<th>Space Complexity</th>
<th>Advantages</th>
<th>Disadvantages</th>
</tr>
</thead>

<tbody>

<tr>
<td><b>Brute Force</b></td>
<td>O(n²)</td>
<td>O(1)</td>
<td>Simple to understand and requires no extra space.</td>
<td>Quadratic time complexity makes it inefficient for large inputs.</td>
</tr>

<tr>
<td><b>Two Pointer</b></td>
<td>O(n log n)</td>
<td>O(n)</td>
<td>Faster than brute force after sorting.</td>
<td>Requires sorting and additional storage for original indices.</td>
</tr>

<tr>
<td><b>One-Pass Hash Map</b></td>
<td>O(n)</td>
<td>O(n)</td>
<td>Optimal solution with constant-time lookups.</td>
<td>Uses additional O(n) space.</td>
</tr>

</tbody>
</table>

<hr>

<h2>Conclusion</h2>

<p>
Among the three approaches, the <b>One-Pass Hash Map</b> provides the best balance of simplicity and efficiency.
It solves the problem in linear time while maintaining clean and readable code, making it the preferred solution for the Two Sum problem.
</p>
	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
	<li><strong>Only one valid answer exists.</strong></li>
</ul>

<p>&nbsp;</p>
<strong>Follow-up:&nbsp;</strong>Can you come up with an algorithm that is less than <code>O(n<sup>2</sup>)</code><font face="monospace">&nbsp;</font>time complexity?
