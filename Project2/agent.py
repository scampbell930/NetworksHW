class Agent:
    content = False
    color = "None"
    empty = True

    def __init__(self, color):
        self.color = color

        if not color.__eq__("White"):
            self.empty = False

    def is_content(self, neighborhood, t):
        same_neighbors = 0

        # Count all neighbors of same color
        for neighbor in neighborhood:
            if neighbor.color == self.color:
                same_neighbors += 1

        # Check if content
        if (same_neighbors / len(neighborhood)) >= t:
            self.content = True
        else:
            self.content = False
