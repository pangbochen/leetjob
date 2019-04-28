'''
15. 3Sum
Medium

3582

389

Favorite

Share
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []
        nums.sort()
        length = len(nums)
        for i in range(length-2):
            # to avoid the duplicate triplets
            if i == 0 or nums[i] > nums[i-1]:
                cur_num = nums[i]

                # keep two pointers to scan result
                left = i+1
                right = length-1
                while left<right:
                    if nums[left]+nums[right]+cur_num<0:
                        left += 1
                    elif nums[left]+nums[right]+cur_num>0:
                        right -= 1
                    else:
                        solution.append([cur_num, nums[left], nums[right]])
                        left += 1
                        right -= 1
                        # to avoid the duplicate solution
                        while left < right and nums[left]==nums[left-1]:
                            left += 1
                        while left < right and nums[right]==nums[right+1]:
                            right -= 1
                return solution