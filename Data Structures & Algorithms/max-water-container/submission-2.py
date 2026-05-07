class Solution:
    def maxArea(self, heights: List[int]) -> int:

        low, high = 0, len(heights) - 1

        max_water_contained = -sys.maxsize - 1
        while low < high:
            water_contained = min(heights[high], heights[low])*(high - low)
            max_water_contained = max(max_water_contained, water_contained)

            if heights[high] < heights[low]:
                high -= 1
            
            else:
                low += 1
        
        return max_water_contained

