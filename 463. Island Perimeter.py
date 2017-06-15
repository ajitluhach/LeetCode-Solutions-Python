"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
"""


class Solution(object):
    def islandPerimeter(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        neighbours = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    islands += 1
                    if c < cols - 1 and grid[r][c+1] == 1: neighbours += 1  # Do not check this case if col index is last_index - 1 
                    if r < rows - 1 and grid[r+1][c] == 1: neighbours += 1  # Do not check this case if row index is last_index - 1
        return 4*islands - 2*neighbours
