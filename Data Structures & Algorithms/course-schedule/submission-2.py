class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pres_dict = {i:[] for i in range(numCourses)}

        for course, prerequisite in prerequisites:
            pres_dict[course].append(prerequisite)

        # print(pres_dict)
        visited = set()
        
        def dfs(crs):
            if crs in visited:
                return False
            if pres_dict[crs] == []:
                return True
            visited.add(crs)
            for cr in pres_dict[crs]:
                if dfs(cr) == False:
                    return False
            visited.remove(crs)
            pres_dict[crs] = []
            return True
        
        for crs in pres_dict:
            if dfs(crs) == False:
                return False
        
        return True
        
            



        