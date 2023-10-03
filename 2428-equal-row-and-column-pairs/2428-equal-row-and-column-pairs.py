class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        count = 0

        length = range(1,len(grid[0])+1)

        row_dict = dict(zip(length,grid))

        column_dict = dict(zip(length,list(zip(*grid))))

        for i in length:
            for j in length:
                if row_dict[i] == list(column_dict[j]):
                    count += 1

        return count

        