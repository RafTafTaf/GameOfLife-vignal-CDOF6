import os
import time
import numpy as np
import random

def clear_console():
    """Clear the console based on the operating system."""
    command = "cls" if os.name == "nt" else "clear"
    os.system(command)

def generate_grid(rows, cols):
    """Generate a grid filled with random 0s and 1s using numpy."""
    return np.random.randint(0, 2, size=(rows, cols)).tolist()

def display_grid(grid, generation):
    """Display the grid and indicate the generation number."""
    clear_console()
    print(f"Generation {generation} - Press Ctrl+C to quit.")
    for row in grid:
        print("".join("# " if cell else ". " for cell in row))
    print()

def count_neighbors(grid, row, col):
    """Count live neighbors of a cell."""
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1)
    ]
    rows, cols = len(grid), len(grid[0])
    return sum(grid[(row + dr) % rows][(col + dc) % cols] for dr, dc in directions)

def next_generation(grid):
    """Compute the next generation grid."""
    rows, cols = len(grid), len(grid[0])
    new_grid = []

    for r in range(rows):
        new_row = []
        for c in range(cols):
            live_neighbors = count_neighbors(grid, r, c)
            if grid[r][c] == 1 and live_neighbors in (2, 3):
                new_row.append(1)
            elif grid[r][c] == 0 and live_neighbors == 3:
                new_row.append(1)
            else:
                new_row.append(0)
        new_grid.append(new_row)

    return new_grid

def prompt_user(prompt, min_val, max_val):
    """Get and validate user input within a range."""
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"Value must be between {min_val} and {max_val}.")
        except ValueError:
            print("Please enter a valid integer.")

def game_of_life():
    """Main function to run Conway's Game of Life."""
    clear_console()
    
    rows = prompt_user("Enter the number of rows (10-50): ", 10, 50)
    cols = prompt_user("Enter the number of columns (10-50): ", 10, 50)
    generations = prompt_user("Enter the number of generations (10-400): ", 10, 400)

    grid = generate_grid(rows, cols)

    for gen in range(1, generations + 1):
        display_grid(grid, gen)
        new_grid = next_generation(grid)

        if new_grid == grid:
            print("The grid has stabilized. Simulation ended.")
            break

        grid = new_grid
        time.sleep(0.2)

if __name__ == "__main__":
    try:
        while True:
            game_of_life()
            restart = input("Press 'r' to restart or any other key to exit: ").strip().lower()
            if restart != 'r':
                break
    except KeyboardInterrupt:
        print("\nSimulation interrupted by user.")
