grid = [[1,2],[3,4]]

def surfaceArea(grid):

    for i, j in grid:
        print(f"i: {i}, j: {j}")

# You are given an n x n grid where you have placed some 1 x 1 x 1 cubes. 
# Each value v = grid[i][j] represents a tower of v cubes placed on top of cell (i, j).

# After placing these cubes, you have decided to glue any directly adjacent cubes to each other, forming several irregular 3D shapes.

# Return the total surface area of the resulting shapes.

# Note: The bottom face of each shape counts toward its surface area
surfaceArea(grid)