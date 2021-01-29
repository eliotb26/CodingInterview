"""
In this challenge, you will be given an array of integers and a target value.
Determine the number of distinct pairs of elements in the array that sum up to the target value.
Two pairs (a, b) and (c, d) are considered to be distinct if and only if the values in sorted order do not match i.e. (1, 9) and (9, 1) are indistinct but (1, 9) and (9, 2) are distinct.

For Example, given the array [1, 2, 3, 6, 7, 8, 9, 1] and a target value of 10, the seven pairs (1, 9), (2, 8), (3, 7), (8, 2), (9, 1), (9, 1) and (1, 9) all sum to 10 and there are only three distinct pairs: (1, 9), (2, 8), and (3, 7).

Function Description: Complete the function numberOfPairs in the editor below.
The function must return an integer, the total number of distinct pairs of elements in the array that sum to the target value.

numberOfPairs has the following parameter(s):

a[a[0], ..., a[n-1]]: an array of integers to select the pairs from.
Constraints:

1 <= n <= 5 x 10^5
0 <= a[i] <= 10^9
0 <= k <= 5 x 10^9
Input Format for Custom Testing

The first line contains an integer n, the size of the array a.
The next n lines each contain an element a[i] where 0 <= i < n.
The next line contains an integer k, the target value.
Input Sample Input 0: 6 1 3 46 1 3 9 47

Sample Output 0:
1

Explanation 0:
a = [1, 3, 46, 1, 3, 9]
There are 4 pairs of unique elements where a[i]+a[j] = k:

1. (a[0] = 1, a[2] = 46)
2. (a[2] = 46, a[0] = 1)
3. (a[2] = 46, a[3] = 1)
4. (a[3] = 1, a[2] = 46)
In the list above, all four pairs contain the same values.  
We only have 1 distinct pair (1, 46).

"""


def distinctPairs(nums, target):
    if len(nums) == 0: 
        return 0 
    dist_pairs = set([])     # by rule, duplicates are not allowed in sets 
    for ind in range(len(nums)): 
        search_result = binary_search(nums, ind, len(nums)-1, target - nums[ind])
        if search_result != -1: 
            dist_pairs.add(tuple(sorted([nums[ind], search_result])))
    return len(dist_pairs)
    
def binary_search(arr, left, right, target): 
    index = left 
    while right >= left: 
        mid = (left+right) //2

        if arr[mid] == target: 
            if mid != index:
                return arr[mid]
            else: 
                if arr[mid-1] == target or arr[mid+1] == target: 
                    return arr[mid-1]
                else: 
                    return -1
        elif arr[mid] > target: 
            right = mid -1 
        else: 
            left = mid+1
        
    return -1 

def main(): 
    print(distinctPairs([1, 3, 46, 1, 3, 9], 47))

main() 