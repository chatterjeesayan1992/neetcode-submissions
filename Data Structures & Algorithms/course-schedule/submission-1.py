class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        pres = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            pres[crs].append(pre)
        
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if pres[crs] == []:
                return True
            visited.add(crs)
            for pr in pres[crs]:
                if dfs(pr) == False:
                    return False

            visited.remove(crs)
            pres[crs] = []
            return True 
        
        for crs in pres:
            if dfs(crs) == False:
                return False
        
        return True

        