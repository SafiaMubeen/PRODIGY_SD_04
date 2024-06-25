def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) for num in row))


def find_empty_location(grid, l):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                l[0], l[1] = i, j
                return True
    return False


def used_in_row(grid, row, num):
    return num in grid[row]


def used_in_col(grid, col, num):
    return num in [grid[row][col] for row in range(9)]


def used_in_box(grid, row, col, num):
    box_start_row, box_start_col = row - row % 3, col - col % 3
    return num in [grid[i][j] for i in range(box_start_row, box_start_row + 3) for j in
                   range(box_start_col, box_start_col + 3)]


def check_location_is_safe(grid, row, col, num):
    return not used_in_row(grid, row, num) and not used_in_col(grid, col, num) and not used_in_box(grid, row, col, num)


def solve_sudoku(grid):
    l = [0, 0]

    if not find_empty_location(grid, l):
        return True

    row, col = l[0], l[1]

    for num in range(1, 10):
        if check_location_is_safe(grid, row, col, num):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True

            grid[row][col] = 0

    return False


def main():
    grid = []
    print(
        "Enter the Sudoku grid row by row, using 0 for empty cells (each row should have 9 space-separated integers):")
    for _ in range(9):
        while True:
            row = input().strip().split()
            if len(row) == 9 and all(r.isdigit() for r in row):
                row = list(map(int, row))
                grid.append(row)
                break
            else:
                print("Invalid input. Please enter exactly 9 space-separated integers for the row.")

    print("\nInput Sudoku grid:")
    print_grid(grid)

    if solve_sudoku(grid):
        print("\nSudoku grid solved successfully:")
        print_grid(grid)
    else:
        print("No solution exists")


# Call the main function
main()
