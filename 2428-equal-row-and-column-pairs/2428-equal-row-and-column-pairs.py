class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        convert_grid = list(zip(*grid))

        for i in range(len(grid[0])):
            if list(convert_grid[i]) in grid:
                count += grid.count(list(convert_grid[i]))
        return count

        