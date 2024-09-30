class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
         if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(r, c):
            # Boundary check and stop if it's water or already visited
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 'W':
                return
            # Mark the current land as visited
            grid[r][c] = 'W'
            # Recursively visit neighboring cells (up, down, left, right)
            dfs(r - 1, c)  # up
            dfs(r + 1, c)  # down
            dfs(r, c - 1)  # left
            dfs(r, c + 1)  # right

        # Iterate through every cell in the grid
        for r in range(rows):
            for c in range(cols):
                # When land is found, start DFS to mark the entire island
                if grid[r][c] == 'L':
                    islands += 1  # Increment the island count
                    dfs(r, c)  # Start exploring the island

        return islands