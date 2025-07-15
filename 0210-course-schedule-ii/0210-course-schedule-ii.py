class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Step 1: Build adjacency list (prereq map) for each course
        prereq = {c: [] for c in range(numCourses)}  # course -> list of prerequisites
        for crs, pre in prerequisites:
            prereq[crs].append(pre)  # add prerequisite for each course

        output = []        # stores the valid course order (post-order)
        visit = set()      # keeps track of courses already checked (safe, no cycle)
        cycle = set()      # keeps track of nodes in the current DFS path (to detect cycles)

        def dfs(crs):
            # If we're revisiting a node in the current path, a cycle is found
            if crs in cycle:
                return False
            # If we've already checked this course, it's safe to use
            if crs in visit:
                return True

            cycle.add(crs)  # add to current DFS path
            for pre in prereq[crs]:  # recursively check all prerequisites
                if not dfs(pre):
                    return False     # If cycle detected downstream, return False
            cycle.remove(crs)        # backtrack: remove from current DFS path
            visit.add(crs)           # mark this course as completed/safe
            output.append(crs)       # add course to ordering (post-order)
            return True

        # Step 2: Try to process every course (handles disconnected graphs)
        for c in range(numCourses):
            if not dfs(c):
                return []  # Cycle found; no valid order

        return output      # Return the order (reverse post-order DFS)

        # --------------------------
        # Implementation Steps:
        # 1. Build a graph using an adjacency list to track prerequisites.
        # 2. For each course, run DFS to visit all prerequisites.
        # 3. Use a set (cycle) to detect cycles in the DFS path.
        # 4. If you ever revisit a node in the current DFS path, a cycle exists → impossible schedule.
        # 5. If no cycle, append course to output after visiting its prerequisites (post-order).
        # 6. At the end, output contains a valid topological order of courses.

        # --------------------------
        # Dry Run Example:
        # numCourses = 4
        # prerequisites = [[1,0],[2,0],[3,1],[3,2]]
        # prereq = {0:[], 1:[0], 2:[0], 3:[1,2]}
        # DFS will build order: 0, 1, 2, 3 (or 0, 2, 1, 3)

        # --------------------------
        # Time Complexity: O(V + E)
        # - V: number of courses
        # - E: number of prerequisite pairs
        # Each course and prerequisite edge is visited once.

        # Space Complexity: O(V + E)
        # - The adjacency list stores up to E edges
        # - The recursion stack and sets can use up to V space
