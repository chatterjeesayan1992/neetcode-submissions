class Solution:
    def maxArea(self, heights: List[int]) -> int:

        if len(heights) < 2:
            return 0
        
        low, high = 0, len(heights) -1
        max_water = -sys.maxsize - 1 
        while low < high:
            water_contained = (high - low)* min(heights[low], heights[high])
            max_water = max(max_water, water_contained)

            if heights[high] > heights[low]:
                low += 1
            else:
                high -= 1
        
        return max_water

        