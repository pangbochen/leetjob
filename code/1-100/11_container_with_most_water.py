class Solution:
    def maxArea1(self, height: List[int]) -> int:
        # the most naive method
        # the O(n^2) solution
        # brouse all possible methods
        max_area = 0
        len_height = len(height)
        for i in range(len_height):
            for j in range(i+1, len_height):
                max_area = max(max_area, min(height[i], height[j])*(j-i))
        return max_area

    def maxArea(self, height: List[int]) -> int:
        # to update the two pointers method
        # the solurion 
        max_area = 0
        len_height = len(height)
        left, right = 0, len_height-1
        while left<right:
            area = min(height[left], height[right])*(right-left)
            max_area = max(area, max_area)
            # update two pointers
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
