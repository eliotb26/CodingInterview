"""
We define a k-subsequence of an array as follows:

It is a subsequence of contiguous elements in the array, i.e. a subarray.
The sum of the subsequence's elements, s, is evenlt divisible by k (i.i: s % k = 0).
Given an array of integers, determine the number of k-subsequences it contains.
For example k = 5 and the array nums = [5, 10, 11, 9, 5].
The 10 k-subsequences are: {5}, {5, 10}, {5, 10, 11, 9}, {5, 10, 11, 9, 5}, {10}, {10, 11, 9}, {10, 11, 9, 5}, {11, 9}, {11, 9, 5}, {5}.

Function Description: Complete the function kSub in the editor below.
The function must return an long integer that represents the number of k-subsequences.

kSub has following parameter(s):

k: an integer that the sum of the subsequence must be divisible by
nums[nums[0], ..., nums[n-1]]: an array of integers
Constraints:

1 <= n <= 3 x 10^5
1 <= k <= 100
1 <= nums[i] <= 10^4
Input Format for Custom Testing

The first line contains an integer k, the number the sum of the subsequence must be divisible by.
The next line contains an integer n, that denotes the number of elements in nums.
Each line i of the n subsequent lines (where 0 <= i < n) contains an integer that describes nums[i].
Input

Sample Input 0:
3
5
1
2
3
4
1

Sample Output 0:
4

Explanation 0:
The 4 contiguous subsequences of nums having sums that are evenly divisible be k = 3 are:
{3}, {1, 2}, {1, 2, 3}, {2, 3, 4}

"""

