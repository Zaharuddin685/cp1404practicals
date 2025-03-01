# Dictionary of color names and their hex codes
COLOR_CODES = {
    "aliceblue": "#F0F8FF",
    "antiquewhite": "#FAEBD7",
    "aquamarine": "#7FFFD4",
    "azure": "#F0FFFF",
    "beige": "#F5F5DC",
    "black": "#000000",
    "blueviolet": "#8A2BE2",
    "brown": "#A52A2A",
    "burlywood": "#DEB887",
    "cadetblue": "#5F9EA0"
}

# User input loop
color_name = input("Enter a color name: ").lower()
while color_name:
    if color_name in COLOR_CODES:
        print(f"{color_name.title()} has hex code {COLOR_CODES[color_name]}")
    else:
        print("Invalid color name.")
    color_name = input("Enter a color name: ").lower()  # Ask again

print("Goodbye!")
