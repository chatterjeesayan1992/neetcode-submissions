class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l,r = 0, len(heights)-1

        max_water = -sys.maxsize - 1

        while l < r:
            water_contained = min(heights[l],heights[r]) * (r-l)
            max_water = max(max_water, water_contained)

            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        return max_water

