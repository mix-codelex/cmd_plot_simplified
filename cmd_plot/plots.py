import math
import numpy as np
from cmd_plot.utils import (
    get_color_block,
    get_centered_title,
    get_random_color_block,
    get_color_letter_256code,
    get_color_palette_for_pie_chart,
)


def get_canvas_string(canvas):
    n, m = np.shape(canvas)
    print(n, m)
    r = ""
    for i in range(n + 2):
        for j in range(m):
            if i < n:
                r += canvas[i][j]
        if i == n or i < n:
            r += "\n"
    return r


def plot_scatter(x, y, height, width):
    # min-max scaling
    x_min, x_max = min(x), max(x)
    y_min, y_max = min(y), max(y)

    x_range = x_max - x_min or 1
    y_range = y_max - y_min or 1

    scaled_x = [(x_i - x_min) / x_range * (width - 1) for x_i in x]
    scaled_y = [(y_i - y_min) / y_range * (height - 1) for y_i in y]

    # Reverse y-axis as we start from the top to the bottom
    scaled_y = [(height - 1) - y_i for y_i in scaled_y]

    # Create matrix canvas
    mat_canvas = [
        [get_color_block(254, width=1) for _ in range(width)] for _ in range(height)
    ]

    # Mark intersetion points
    for x_i, y_i in zip(scaled_x, scaled_y):
        x_pos, y_pos = round(x_i), round(y_i)
        # Check validity range of x,y
        if 0 <= x_pos <= width and 0 <= y_pos <= height:
            mat_canvas[y_pos][x_pos] = get_color_letter_256code(
                text="\u25cf", fg_color="red", bg_color=254
            )

    print(get_canvas_string(mat_canvas))


def plot_line(x, y, height, width):
    # min-max scaling
    x_min, x_max = min(x), max(x)
    y_min, y_max = min(y), max(y)

    x_range = x_max - x_min or 1
    y_range = y_max - y_min or 1

    scaled_x = [(x_i - x_min) / x_range * (width - 1) for x_i in x]
    scaled_y = [(y_i - y_min) / y_range * (height - 1) for y_i in y]

    # Reverse y-axis as we start from the top to the bottom
    scaled_y = [(height - 1) - y_i for y_i in scaled_y]

    # Create matrix canvas
    mat_canvas = [
        [get_color_block(254, width=1) for _ in range(width)] for _ in range(height)
    ]

    # Implement the line algorithm
    for i in range(1, len(scaled_x)):
        x0, y0 = round(scaled_x[i - 1]), round(scaled_y[i - 1])
        x1, y1 = round(scaled_x[i]), round(scaled_y[i])
        dx, dy = abs(x1 - x0), abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx - dy

        while True:
            if 0 <= x0 < width and 0 <= y0 < height:
                mat_canvas[y0][x0] = get_color_letter_256code(
                    text="\u25cf", fg_color="red", bg_color=254
                )
            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x0 += sx
            if e2 < dx:
                err += dx
                y0 += sy

    # Mark intersetion points
    for x_i, y_i in zip(scaled_x, scaled_y):
        x_pos, y_pos = round(x_i), round(y_i)
        # Check validity range of x,y
        if 0 <= x_pos <= width and 0 <= y_pos <= height:
            mat_canvas[y_pos][x_pos] = get_color_letter_256code(
                text="\u25cf", fg_color="red", bg_color=254
            )

    print(get_canvas_string(mat_canvas))


def plot_bar(data, labels, width):
    max_value = max(data)
    # This is used to understand what the value represent in term of width length
    scaling_factor = width / max_value

    # Get colors and values
    # Each bar data values get an randomly assigned color value
    color_blocs = [get_random_color_block(width=3) for _ in data]
    bg_block = get_color_block(254, width=3)  # to use where there is no data
    # ex.1 A=60,B=40,   for A 60 is color_blocs and 40 is bg_block and vice versa for B
    # value_labels return the ansi color text version of the data value for visuzaliztion purpose
    value_labels = [
        get_centered_title(str(val), total_width=len(str(max_value)) + 2)
        for val in data
    ]

    canvas = []
    for i, val in enumerate(data):
        bar_len = int(
            val * scaling_factor
        )  # How much width to use for this value see ex. 1
        row = []
        for j in range(width + 1):
            if j < bar_len:
                row.append(color_blocs[i])
            elif j == bar_len:
                # Set value text
                row.append(value_labels[i])
            else:
                row.append(bg_block)
        canvas.append(row)

    print(get_canvas_string(canvas))



def plot_pie(data, labels, size, use_colors=True):
    total = sum(data)
    if total == 0:
        print("All values are zero.")
        return
    
    # get #len(data) colors for each pie slices
    colors = get_color_palette_for_pie_chart(len(data))
    
    if use_colors:
        symbols = [ get_color_letter_256code('░', bg_color=col, fg_color=col) for col in colors]
    else:
        symbols = ["█", "▓", "▒", "░", "▄", "▀", "◆", "●", "◇", "○"]
    
    
    # Create matrix canvas
    # Ansi character are taller than they are wide, there 2*size
    circle_canvas = [ [" " for _ in range(size * 2)] for _ in range(size) ]
    center_x, center_y = size, size // 2
    radius = size // 2
    
    current_angle = 0
    for i, val in enumerate(data):
        # Angle percentage for each pie slices
        angle = 360 * (val / total)
        end_angle = current_angle + angle 
        symbol = symbols[i % len(symbols)] # slice color
        
        for y in range(size):
            for x in range(size * 2):
                # Convert x,y to polor coordinates
                dx = x - center_x
                dy = y - center_y
                
                dx_scaled = dx / 2.0
                dist = math.hypot(dx_scaled, dy)
                
                if dist > radius:
                    # point not part of the circle
                    continue
                
                # Polor angle
                theta = (math.degrees(math.atan2(dy, dx_scaled)) + 360) %  360
                if current_angle <= theta <= end_angle:
                    circle_canvas[y][x] = symbol
        current_angle = end_angle
    
    
    print(get_canvas_string(circle_canvas))
    
    print("\nLegend:")
    for i, (label, val) in enumerate(zip(labels, data)):
        print(f"{symbols[i % len(symbols)]} {label} ({val / total:.1%})")