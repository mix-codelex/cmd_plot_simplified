import math
import random
import numpy as np


colorMap256 = {
    # Basic colors (16 standard colors)
    "black": 0,
    "maroon": 1,
    "green": 2,
    "olive": 3,
    "navy": 4,
    "purple": 5,
    "teal": 6,
    "silver": 7,
    "grey": 8,
    "gray": 8,  # Alternative spelling
    "red": 9,
    "lime": 10,
    "yellow": 11,
    "blue": 12,
    "fuchsia": 13,
    "magenta": 13,  # Alias for fuchsia
    "aqua": 14,
    "cyan": 14,  # Alias for aqua
    "white": 15,
    # Extended basic colors
    "dark_red": 88,
    "dark_green": 22,
    "dark_blue": 18,
    "dark_yellow": 58,
    "dark_cyan": 30,
    "dark_magenta": 90,
    # Bright variations
    "bright_black": 8,
    "bright_red": 196,
    "bright_green": 46,
    "bright_yellow": 226,
    "bright_blue": 21,
    "bright_magenta": 201,
    "bright_cyan": 51,
    "bright_white": 231,
    # Reds
    "crimson": 160,
    "scarlet": 196,
    "cherry": 161,
    "rose": 203,
    "coral": 203,
    "salmon": 209,
    "pink": 205,
    "hot_pink": 198,
    "deep_pink": 197,
    "light_pink": 217,
    "indian_red": 167,
    "fire_brick": 124,
    "dark_salmon": 173,
    "light_salmon": 216,
    "tomato": 203,
    # Oranges
    "orange": 208,
    "dark_orange": 166,
    "orange_red": 202,
    "peach": 216,
    "papaya": 215,
    "tangerine": 214,
    "burnt_orange": 166,
    "rust": 130,
    "amber": 214,
    # Yellows
    "gold": 220,
    "lemon": 227,
    "light_yellow": 230,
    "pale_yellow": 229,
    "khaki": 185,
    "beige": 223,
    "cream": 230,
    "ivory": 230,
    "wheat": 223,
    "corn": 227,
    "banana": 226,
    "canary": 227,
    # Greens
    "forest_green": 28,
    "dark_green": 22,
    "sea_green": 29,
    "medium_sea_green": 71,
    "light_sea_green": 37,
    "pale_green": 120,
    "light_green": 119,
    "lawn_green": 118,
    "chartreuse": 118,
    "spring_green": 48,
    "medium_spring_green": 49,
    "green_yellow": 154,
    "lime_green": 77,
    "yellow_green": 113,
    "mint": 121,
    "mint_cream": 194,
    "honeydew": 194,
    "jade": 35,
    "emerald": 46,
    "malachite": 47,
    "olive_drab": 64,
    # Blues
    "navy_blue": 17,
    "midnight_blue": 17,
    "royal_blue": 63,
    "steel_blue": 67,
    "cornflower_blue": 69,
    "deep_sky_blue": 39,
    "sky_blue": 117,
    "light_sky_blue": 117,
    "powder_blue": 152,
    "light_blue": 153,
    "alice_blue": 231,
    "azure": 231,
    "ice_blue": 159,
    "periwinkle": 104,
    "indigo": 54,
    "slate_blue": 62,
    "medium_slate_blue": 99,
    "cadet_blue": 73,
    "teal_blue": 31,
    "cerulean": 33,
    # Purples/Violets
    "violet": 129,
    "dark_violet": 92,
    "blue_violet": 92,
    "medium_violet_red": 162,
    "orchid": 170,
    "plum": 176,
    "thistle": 182,
    "lavender": 183,
    "medium_orchid": 134,
    "dark_orchid": 128,
    "purple_rain": 93,
    "royal_purple": 55,
    "amethyst": 133,
    "grape": 97,
    "eggplant": 91,
    "mulberry": 126,
    # Browns
    "brown": 94,
    "saddle_brown": 94,
    "chocolate": 130,
    "sienna": 131,
    "peru": 173,
    "tan": 180,
    "sandy_brown": 215,
    "rosy_brown": 138,
    "goldenrod": 178,
    "dark_goldenrod": 136,
    "coffee": 94,
    "mocha": 95,
    "caramel": 179,
    "cinnamon": 173,
    "bronze": 136,
    "copper": 166,
    # Grays
    "dim_gray": 242,
    "dark_gray": 248,
    "light_gray": 252,
    "gainsboro": 253,
    "whitesmoke": 255,
    "charcoal": 235,
    "slate_gray": 66,
    "light_slate_gray": 103,
    "dark_slate_gray": 239,
    "ash": 245,
    "pewter": 247,
    "stone": 250,
    # Pastels
    "pastel_pink": 218,
    "pastel_blue": 153,
    "pastel_green": 157,
    "pastel_yellow": 229,
    "pastel_orange": 216,
    "pastel_purple": 183,
    # Neons
    "neon_pink": 199,
    "neon_green": 46,
    "neon_blue": 45,
    "neon_yellow": 226,
    "neon_orange": 202,
    "neon_purple": 129,
    # Metallics
    "silver_metallic": 250,
    "gold_metallic": 220,
    "platinum": 254,
    "steel": 240,
    "iron": 239,
    "titanium": 250,
    # Nature colors
    "grass": 34,
    "moss": 64,
    "sage": 108,
    "pine": 22,
    "ocean": 24,
    "sand": 223,
    "dirt": 94,
    "clay": 131,
    "mud": 58,
    "stone_gray": 244,
    "sky": 117,
    "sunset": 202,
    "sunrise": 214,
    # Gem colors
    "ruby": 160,
    "sapphire": 21,
    "diamond": 231,
    "topaz": 214,
    "opal": 194,
    "pearl": 255,
    "turquoise": 44,
    "garnet": 88,
    "onyx": 16,
    "citrine": 226,
}




def get_random_color_block(width=2):
    # Use indices 16-231 for bright and distinct colors
    bright_colors = range(16, 232)
    index = random.choice(bright_colors)
    return f"\u001b[48;5;{index}m{str('').center(width, ' ')}\u001b[0m"


def get_color_block(index, width=2):
    blocks = [
        f"\u001b[48;5;{i - 1}m{str('').center(width, ' ')}\u001b[0m"
        for i in range(1, 256)
    ]
    return blocks[index]


def get_color_letter_256code(text, fg_color=None, bg_color="white"):
    """
    Convert a string to 256-color ANSI codes, supporting named colors with extensive palette.

    Parameters:
        text (str): The text to colorize.
        fg_color (str | int): The foreground color (name or 0-255).
        bg_color (str | int): The background color (name or 0-255).

    Returns:
        str: The ANSI-colored string.
    """
    # Convert named colors to 256-color equivalents if provided
    if isinstance(fg_color, str):
        fg_color = colorMap256.get(fg_color.lower(), fg_color)
        # If still a string after lookup, try to convert to int
        if isinstance(fg_color, str):
            try:
                fg_color = int(fg_color)
            except ValueError:
                fg_color = None

    if isinstance(bg_color, str):
        bg_color = colorMap256.get(bg_color.lower(), bg_color)
        # If still a string after lookup, try to convert to int
        if isinstance(bg_color, str):
            try:
                bg_color = int(bg_color)
            except ValueError:
                bg_color = 231  # Default to white if invalid

    # Validate color ranges (0-255 for 256-color mode)
    if fg_color is not None and (fg_color < 0 or fg_color > 255):
        fg_color = None
    if bg_color is not None and (bg_color < 0 or bg_color > 255):
        bg_color = 231  # Default to white

    # Base ANSI code format
    fg_code = f"\033[38;5;{fg_color}m" if fg_color is not None else ""
    bg_code = f"\033[48;5;{bg_color}m" if bg_color is not None else ""
    reset_code = "\033[0m"

    # Return the formatted text with ANSI codes
    return f"{fg_code}{bg_code}{text}{reset_code}"


def get_centered_title(
    title, counts=0, g_width=0, space_width=0, total_width=None, color="black"
):
    if not total_width:
        total_width = g_width * len(counts) + (space_width * len(counts)) + space_width
    title_len = len(title)
    row_array = [get_color_block(254, width=1)] * total_width
    title_array = [get_color_letter_256code(text=t, fg_color=color) for t in title]

    row_array_midpoint = math.ceil(total_width / 2)
    title_array_midpoint = math.ceil(title_len / 2)
    start_index = (row_array_midpoint - 1) - (title_array_midpoint - 1)
    row_array[start_index : start_index + title_len] = title_array

    title_text_colors = "".join(row_array)
    return title_text_colors


def get_color_palette_for_pie_chart(num_segments):
    """
    Generate a visually distinct color palette for pie charts.

    Parameters:
        num_segments (int): Number of segments needed

    Returns:
        list: List of 256-color codes optimized for visibility
    """
    # Predefined high-contrast color palette for pie charts
    pie_colors = [
        196,  # bright_red
        46,  # bright_green
        21,  # bright_blue
        226,  # bright_yellow
        201,  # bright_magenta
        51,  # bright_cyan
        208,  # orange
        129,  # violet
        28,  # forest_green
        160,  # crimson
        39,  # deep_sky_blue
        220,  # gold
        128,  # dark_orchid
        166,  # dark_orange
        34,  # grass
        198,  # hot_pink
        63,  # royal_blue
        178,  # goldenrod
        92,  # blue_violet
        173,  # peru
        118,  # chartreuse
        162,  # medium_violet_red
        67,  # steel_blue
        214,  # tangerine
        77,  # lime_green
        133,  # amethyst
        130,  # chocolate
        44,  # turquoise
        203,  # coral
        113,  # yellow_green
    ]

    # If we need more colors than predefined, generate them using a pattern
    if num_segments > len(pie_colors):
        # Use mathematical distribution for additional colors
        for i in range(len(pie_colors), num_segments):
            # Generate colors in HSV-like distribution
            hue_step = 360 // num_segments
            color_index = 16 + ((i * hue_step) % 216)  # Use 216-color cube
            pie_colors.append(color_index)

    return pie_colors[:num_segments]


def parse_numbers(seq):
    return np.array([float(val) if "." in val else int(val) for val in seq.split(",")])


def sort_points_by_x(x, y):
    # Pair x and y, sort by x
    sorted_pairs = sorted(zip(x, y), key=lambda pair: pair[0])

    # Unzip back to sorted x and y
    sorted_x, sorted_y = zip(*sorted_pairs)

    return list(sorted_x), list(sorted_y)


def plot_block_colors():
    for i in range(1, 256):
        print(f"\u001b[48;5;{i - 1}m{str(i).center(5, ' ')}\u001b[0m", end="")
        if i % 15 == 0:
            print(
                "\u001b[0m"
            )  # resets the text color back to the terminal's default and add \n
