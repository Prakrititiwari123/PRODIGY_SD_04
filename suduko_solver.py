def print_grid(grid):
    """Prints the Sudoku grid in a readable format."""
    for row in grid:
        print(" ".join(str(num) if num != 0 else "." for num in row))
    print("\n")

def is_safe(grid, row, col, num):
    """Checks if placing num at grid[row][col] is valid."""
    for x in range(9):
        if grid[row][x] == num or grid[x][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(grid):
    """Solves the Sudoku puzzle using backtracking."""
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_safe(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

# Input Sudoku Grid (0 represents empty cells)
sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("\n🔢 Unsolved Sudoku:")
print_grid(sudoku_grid)

if solve_sudoku(sudoku_grid):
    print("\n✅ Solved Sudoku:")
    print_grid(sudoku_grid)
else:
    print("\n❌ No solution exists!")
