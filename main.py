class Color:
    def __init__(self, red=0, green=0, blue=0):
        self.red = red
        self.green = green
        self.blue = blue
    def print_color(self):
        print("Self Color:", self.red, self.green, self.blue)

def print_color(color):
    print("Color:", color.red, color.blue, color.green)

color = Color()
color.red = 255
color.green = 123
color.blue = 8

color2 = Color(244, 100, 50)  # This will create a new Color object with the specified RGB values
color.print_color()  # This will call the print_color method of the Color class 
print_color(color2)
