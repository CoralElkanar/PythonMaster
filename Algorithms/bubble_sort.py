"""
Question: 
sort the list in an ascending order
"""

def bubble_sort(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        max Time: O(n^2)
        min Time: O(n) if already sorted
        """
        # i represents the number of elements that are already sorted - in the correct position
        for i in range(len(nums)):
                # we subject the number of elements sorted (i), and subject 1 to avoid running for the last element, 
                # which will be already sorted by the time we get to it.
                for j in range(len(nums)-i-1):
                        # compare the current element with the element that comes after it
                        if nums[j] > nums[j+1]:
                                # swap
                                nums[j], nums[j+1] = nums[j+1], nums[j]
                
"""
swap:
temp = nums[j]
nums[j] = nums[j+1]
nums[j+1] = temp
"""


nums = [1,17,8,2,5,0,9,25]
print(f"nums = {nums}")
bubble_sort(nums=nums)
print(f"after bubble_sort: nums = {nums}")
