def visibility(grid, x, y, coords, horizontal):
    size = len(grid)
    if x in (0, size - 1) or y in (0, size - 1):
        return True, 0 # at the edge the scenic score is 0
    visible = True
    score = 0
    for coord in coords:
        score += 1
        if (grid[y][coord] if horizontal else grid[coord][x]) >= grid[y][x]:
            visible = False
            break
    return visible, score


with open("puzzle_input.txt") as file:
    grid = [[int(tree) for tree in row.strip()] for row in file]
    size = len(grid) # assume the grid is a squre
    visibilities = {}
    scenic_scores = {}
    for y in range(size):
        for x in range(size):
            coords = range(x - 1, -1, -1), range(x + 1, size), range(y - 1, -1, -1), range(y + 1, size)
            directions = True, True, False, False
            for coords, dir in zip(coords, directions):
                visible, score = visibility(grid, x, y, coords, dir)
                if not visibilities.get((x, y), False): # if True already found, don't change
                    visibilities[x, y] = visible
                scenic_scores[x, y] = scenic_scores.get((x, y), 1) * score
    print(sum(visibilities.values()))
    print(max(scenic_scores.values()))