from agent import Agent
import random as r


def initialize_grid(n: int = 30, red_blue_split: float = 0.5, pct_empty: float = 0.15) -> list:
    # Initialize grid of agents
    grid = [[None for _ in range(n)] for _ in range(n)]

    # Fill grid
    for i in range(n):
        for j in range(n):
            # Determine if empty cell
            if r.random() > pct_empty:
                # Place agent
                if r.random() < red_blue_split:
                    grid[i][j] = Agent("Red")
                else:
                    grid[i][j] = Agent("Blue")
            # Empty location
            else:
                grid[i][j] = Agent("White")

    return grid


# Generate a list of neighbors around an agent
def generate_neighborhood(grid: list, i: int, j: int) -> list:
    neighborhood = []

    for k in range(i-1, i+2):
        for l in range(j-1, j+2):
            if 0 <= k < len(grid) and 0 <= l < len(grid):
                if i != k or j != l:
                    if not grid[k][l].empty:
                        neighborhood.append(grid[k][l])

    # IDK why I have to manually remove these but my above if statement does not handle it
    for n in neighborhood:
        if n.empty:
            neighborhood.remove(n)

    return neighborhood


if __name__ == '__main__':
    # Create random grid (parameters hardcoded in header)
    grid = initialize_grid()

    # Check satisfaction and move accordingly
    t = 0.4
    max_iter = 0
    satisfied = False

    for i in range(len(grid)):
        print()
        for j in range(len(grid)):
            if grid[i][j].color.__eq__("Red"):
                print("X ", end="")
            elif grid[i][j].color.__eq__("Blue"):
                print("* ", end="")
            else:
                print("  ", end="")
    print()

    while max_iter < 1000 and not satisfied:
        unsatisfied = []
        empty_cells = []

        # Generate agent satisfaction
        for j in range(len(grid)):
            for k in range(len(grid)):
                if not grid[j][k].empty:
                    neighborhood = generate_neighborhood(grid, j, k)
                    if not len(neighborhood) == 0:
                        grid[j][k].is_content(neighborhood, t)
                    else:
                        grid[j][k].content = False

                else:
                    empty_cells.append((j, k))

                if not grid[j][k].content and not grid[j][k].empty:
                    unsatisfied.append((j, k))

        if len(unsatisfied) == 0:
            satisfied = True

        # print("Unsat: " + str(len(unsatisfied)))
        # print("Rest: " + str(50*50 - (len(unsatisfied) + len(empty_cells))))

        # Move all unsatisfied agents to random empty location
        while len(unsatisfied) != 0 and len(empty_cells) != 0:
            move = r.choice(unsatisfied)
            unsatisfied.remove(move)

            empty = r.choice(empty_cells)
            empty_cells.remove(empty)

            grid[empty[0]][empty[1]] = grid[move[0]][move[1]]
            grid[move[0]][move[1]] = Agent("White")

        max_iter += 1

    print(satisfied)

    for i in range(len(grid)):
        print()
        for j in range(len(grid)):
            if grid[i][j].color.__eq__("Red"):
                print("X ", end="")
            elif grid[i][j].color.__eq__("Blue"):
                print("* ", end="")
            else:
                print("  ", end="")
    print()