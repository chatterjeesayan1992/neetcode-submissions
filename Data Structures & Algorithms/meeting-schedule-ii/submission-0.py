"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_times = sorted([i.start for i in intervals])
        end_times = sorted([i.end for i in intervals])

        # print(len(start_times), len(end_times),len(intervals))

        
        i=j=0
        count = 0
        res = 0
        while i < len(intervals):
            if start_times[i] < end_times[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            res = max(res, count)
        return res
        

        