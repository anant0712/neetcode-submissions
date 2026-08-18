class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        left = 0
        right = len(heights)-1

        while left < right:
            width = right - left
            ht = min(heights[left],heights[right])
            area = width*ht

            max_water = max(max_water,area)

            if heights[left] < heights[right]:
                left +=1
            else:
                right -=1
        return max_water