# Text-based Interactive User Interface

from Cimpl import *
from T046_image_filters import *

command_list = ["L", "S", "3", "X", "T", "P", "E", "D", "V", "H", "Q"]
def filter_selection(action,pic):
    if action == "L":
        result = load_image(choose_file())
        return result
    elif action == "S" and type(pic) == Image:
        save_as(pic)
        print("Image saved to selected directory")
    elif action == "3" and type(pic) == Image:
        print("Choose 3 of the following colours: black, white, blood, green, blue, lemon, cyan, magenta, gray")
        color_list = ["black","white","blood","green","blue","lemon","cyan","magenta","gray"]
        choice_list = []
        for i in range(3):
            c = input("Please enter Colour " + str(i + 1) + ": ")
            while c not in color_list:
                print("Not a valid colour, please try again\n")
                c = input("Please enter Colour " + str(i + 1) + ": ")    
            choice_list.append(c)
        result = three_tone(pic,choice_list[0],choice_list[1],choice_list[2])
        print("Three tone filter has been applied to the image")
        return result
    elif action == "X" and type(pic) == Image:
        result = extreme_contrast(pic)
        print("Extreme contract filter has been applied to the image")
        return result
    elif action == "T" and type(pic) == Image:
        result = sepia(pic)
        print("Sepia tint filter has been applied to the image")
        return result
    elif action == "P" and type(pic) == Image:
        result = posterize(pic)
        print("Posterize filter has been applied to the image")
        return result
    elif action == "E" and type(pic) == Image:
        threshold = int(input("Enter a contrast threshold: "))
        result = detect_edges(pic,threshold)
        print("Edge detection filter has been applied to the image")
        return result
    elif action == "D" and type(pic) == Image:
        print("Choose a line colour from the following options: black, white, blood, green, blue, lemon, cyan, magenta, gray")
        color_list = ["black","white","blood","green","blue","lemon","cyan","magenta","gray"]
        line_color = input("Please enter desired line colour: ")
        while line_color not in color_list:
                print("Not a valid colour, please try again\n")
                line_color = input("Please enter desired line colour: ")
        mod_image = draw_curve(pic,line_color)
        result = mod_image[0]
        print("A curve going through the specified points has been drawn on the image")
        return result
    elif action == "V" and type(pic) == Image:
        result = flip_vertical(pic)
        print("Vertical flip filter has been applied to the image")
        return result
    elif action == "H" and type(pic) == Image:
        result = flip_horizontal(pic)
        print("Horizontal flip filter has been applied to the image")
        return result
    else:
        if action == "Q":
            print("Program finished")
        elif action not in command_list:
            print("No such command")
        else:
            print("No image loaded")
            print("An image must be loaded before a filter is applied. When prompted, enter 'L' or 'l' to load an image.")