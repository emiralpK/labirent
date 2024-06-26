import numpy as np

def generate_maze(size):
    maze = np.random.randint(2, size=(size, size)).tolist()
    maze[0][0] = 0
    maze[size-1][size-1] = 0
    return maze

def solve_maze(maze):
    size = len(maze)
    solution = [[0] * size for _ in range(size)]
    def dfs(x, y):
        if x < 0 or x >= size or y < 0 or y >= size or maze[y][x] == 1 or solution[y][x] == 1:
            return False
        solution[y][x] = 1
        if (x, y) == (size - 1, size - 1):
            return True
        if dfs(x + 1, y) or dfs(x - 1, y) or dfs(x, y + 1) or dfs(x, y - 1):
            return True
        solution[y][x] = 0
        return False
    dfs(0, 0)
    return solution

def generate_and_solve(size=32):
    maze = generate_maze(size)
    solution = solve_maze(maze)
    return maze, solution
