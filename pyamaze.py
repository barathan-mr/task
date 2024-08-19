from queue import PriorityQueue

def hvalue(cell, dest):
    x1, y1 = cell
    x2, y2 = dest
    return abs(x1 - x2) + abs(y1 - y2)

def is_valid(cell, grid):
    x, y = cell
    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
        return False
    return grid[x][y] == 1

def neighbours(cell, grid):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    neighbor = []
    x, y = cell
    for dx, dy in directions:
        neighbour = (x + dx, y + dy)
        if is_valid(neighbour, grid):
            neighbor.append(neighbour)
    return neighbor

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    total_path.reverse()
    return total_path

def astar_search(grid, start, dest):
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}

    g_score = { (i, j): float('inf') for i in range(len(grid)) for j in range(len(grid[0])) }
    g_score[start] = 0

    f_score = { (i, j): float('inf') for i in range(len(grid)) for j in range(len(grid[0])) }
    f_score[start] = hvalue(start, dest)

    while not open_set.empty():
        _, current = open_set.get()

        if current == dest:
            path = reconstruct_path(came_from, current)
            print("Path found:", path)
            return path

        for neighbour in neighbours(current, grid):
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbour]:
                came_from[neighbour] = current
                g_score[neighbour] = temp_g_score
                f_score[neighbour] = temp_g_score + hvalue(neighbour, dest)
                open_set.put((f_score[neighbour], neighbour))

    print("No path found")
    return None

def main():
    grid = [
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [1, 1, 1, 0, 1],
        [0, 0, 1, 0, 1],
        [1, 1, 1, 0, 1],
    ]
    start = (4, 0)
    dest = (0, 4)
    astar_search(grid, start, dest)

if __name__ == "__main__":
    main()
