class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create an adjacency list to map each course to its prerequisites
        preMap = { i : [] for i in range(numCourses) }
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visiting = set()  # Set to keep track of nodes in the current DFS path (detect cycles)
        
        # DFS function to check if a course can be finished (no cycle in its prerequisites)
        def dfs(crs):
            # If we see the course in the current DFS stack, we found a cycle!
            if crs in visiting:
                return False
            # If this course has no prerequisites left, it's already processed
            if preMap[crs] == []:
                return True
            
            # Mark the course as being visited in this path
            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):      # If a cycle is detected downstream, return False
                    return False
            visiting.remove(crs)      # Done with this node in this path

            # Memoization: No cycles, mark as completed (no prereqs left)
            preMap[crs] = []
            return True
        
        # Try to process every course. If any cycle detected, return False
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

# ---------------------------------------------------------
# IMPLEMENTATION STEPS (in comments for your notes):

# 1. Build the graph:
#    - Use a hashmap to store each course and its prerequisites.

# 2. For each course, run DFS to detect cycles:
#    - If you see the same course twice in the current path, it's a cycle (return False).
#    - If you reach a course with no prereqs, it's safe (return True).
#    - Mark courses as "visited" for the current path using a set.
#    - Once a course and all its dependencies are processed, empty its prereq list for memoization.

# 3. Try to process all courses:
#    - If you can process all without a cycle, return True. If you ever find a cycle, return False immediately.

# ---------------------------------------------------------
# DRY RUN:
# Input: numCourses = 2, prerequisites = [[1,0]]
# - preMap = {0: [], 1: [0]}
# - Run dfs(0): preMap[0] is [], so return True.
# - Run dfs(1): 1 is not in visiting, preMap[1] = [0]
#   - visiting = {1}
#   - dfs(0): return True (no prereqs for 0)
#   - Remove 1 from visiting, set preMap[1] = []
# - Both processed successfully, so return True.

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# - preMap = {0: [1], 1: [0]}
# - dfs(0): visiting={0}, dfs(1): visiting={0,1}, dfs(0) again --> cycle detected, return False.

# ---------------------------------------------------------
# TIME COMPLEXITY:
# - Building the graph: O(P), where P = len(prerequisites)
# - DFS may visit each course and each edge at most once: O(N + P), where N = numCourses
# - Overall: **O(N + P)**

# SPACE COMPLEXITY:
# - Graph/hashmap storage: O(N + P)
# - Recursion stack & visiting set: O(N)
# - Overall: **O(N + P)**

# ---------------------------------------------------------
