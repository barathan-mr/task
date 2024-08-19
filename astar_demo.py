from queue import PriorityQueue
def hvalue(cell,dest):
    x1,y1=cell
    x2,y2=dest
    return abs(x1-x2)+abs(y1-y2)
def is_valid(cell, grid):
    x, y = cell
    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y]==0:
        return False
    return grid[x][y] == 1
def neighbours(grid,cell):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    neighbor = []
    x, y = cell
    for dx, dy in directions:
        neighbour = (x + dx, y + dy)
        if is_valid(neighbour, grid):
            neighbor.append(neighbour)
    return neighbor

def astar_search(grid,start,dest):
    open=PriorityQueue()
    g_score = { (i, j): float('inf') for i in range(len(grid)) for j in range(len(grid[0])) }
    f_score = { (i, j): float('inf') for i in range(len(grid)) for j in range(len(grid[0])) }
    g_score[start]=0
    f_score[start]=g_score[start]+hvalue(start,dest)
    open.put((f_score[start],start))

    while not open.empty():
        _,curr_cell=open.get()
        if curr_cell==dest:
            print("path getted")
        for neighbour in neighbours(grid,curr_cell):
            temp_gscore=g_score[curr_cell]+1

            if temp_gscore < g_score[neighbour]:
                g_score[neighbour] = temp_gscore
                f_score[neighbour] = temp_gscore + hvalue(neighbour, dest)
                open.put((f_score[neighbour], neighbour))



def main():
    grid=[
        [1,0,1,1,1],
        [1,1,1,0,1],
        [1,1,1,0,1],
        [0,0,1,0,1],
        [1,1,1,0,1],
    ]
    print(len(grid[0]))
    start=(4,0)
    dest=(0,4)
    astar_search(grid,start,dest)
if __name__=="__main__":
    main()