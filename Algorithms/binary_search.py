"""
Question:
Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""

def binary_search(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        Time: O(log(n))
        """
        L = 0
        R = len(nums) - 1

        while R >= L:
                mid = (L + R)//2  # this devides 'down' (6.5 -> 6)
                if nums[mid] == target:
                        return mid
                elif nums[mid] > target:
                        R = mid - 1
                else:  # nums[mid] < target
                        L = mid + 1
        return -1

# notice: in order to prevent overflow in large lists (L+R too long) 
# we can calculate the mid as mid = L + ((R - L) // 2)

nums = [-1,0,3,5,9,12] 
target = 9
x = binary_search(nums=nums, target=target)
print(f"the output of binary_search of the input: nums={nums}, target={target} is: {x} ")

nums = [-1,0,3,5,9,12] 
target = 2
x = binary_search(nums=nums, target=target)
print(f"the output of binary_search of the input: nums={nums}, target={target} is: {x} ")
