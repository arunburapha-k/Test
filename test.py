import math

def draw_star(size=15):
    # Create a grid with a width adjustment for terminal characters (usually taller than wide)
    width = int(size * 2.5)
    height = size
    grid = [[' ' for _ in range(width)] for _ in range(height)]
    
    # Center of the star
    cx, cy = width // 2, height // 2
    
    # Outer and inner radii
    R = height // 2
    r = R * 0.382  # Golden ratio related for a perfect 5-pointed star
    
    points = []
    # Calculate the 10 points of the star (5 outer, 5 inner)
    for i in range(10):
        angle = math.radians(i * 36 - 90)  # Start from top
        radius = R if i % 2 == 0 else r
        # Adjust px for terminal aspect ratio (characters are taller than wide)
        px = cx + radius * math.cos(angle) * 2.2
        py = cy + radius * math.sin(angle)
        points.append((px, py))
    
    # Function to check if a point (x, y) is inside the star polygon
    def is_inside(x, y, poly):
        n = len(poly)
        inside = False
        p1x, p1y = poly[0]
        for i in range(n + 1):
            p2x, p2y = poly[i % n]
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xints = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xints:
                            inside = not inside
            p1x, p1y = p2x, p2y
        return inside

    # Fill the grid
    for y in range(height):
        for x in range(width):
            if is_inside(x, y, points):
                grid[y][x] = '*'

    # Print the grid
    for row in grid:
        print("".join(row))

draw_star(15)
