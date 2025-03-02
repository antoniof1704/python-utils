# Create a function that produces specified text to appear in the log in one of the avialable colour options

def log_message(text, colour):
    # ANSI escape codes for text colors
    Black = "\033[30m"
    Red = "\033[31m"
    Green = "\033[32m"
    Yellow = "\033[33m"
    Blue = "\033[34m"
    Magenta = "\033[35m"
    Cyan = "\033[36m"
    White = "\033[37m"
    RESET = "\033[0m"  # Reset to default color

    # Mapping the input colour to the corresponding escape code
    colour_dict = {
        "black": Black,
        "red": Red,
        "green": Green,
        "yellow": Yellow,
        "blue": Blue,
        "magenta": Magenta,
        "cyan": Cyan,
        "white": White
    }

    # Check if the provided color is valid and print the text with color
    if colour.lower() in colour_dict:
        print(f"{colour_dict[colour.lower()]}{text}{RESET}")
    else:
        print(f"{Red}Invalid color. Available options: black, red, green, yellow, blue, magenta, cyan, white.{RESET}")