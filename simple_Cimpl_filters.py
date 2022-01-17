""" ECOR 1051 Fall 2019

Some simple Cimpl image processing filters.
Last edited: Nov. 12, 2019
"""

from Cimpl import choose_file, load_image, copy, create_color, set_color,\
                  show, Image, get_color, save_as

def grayscale(image: Image) -> Image:
    """Return a grayscale copy of image.
   
    >>> image = load_image(choose_file())
    >>> gray_image = grayscale(image)
    >>> show(gray_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:

        # Use the pixel's brightness as the value of RGB components for the 
        # shade of gray. These means that the pixel's original colour and the
        # corresponding gray shade will have approximately the same brightness.
        
        brightness = (r + g + b) // 3
        
        # or, brightness = (r + g + b) / 3
        # create_color will convert an argument of type float to an int
        
        gray = create_color(brightness, brightness, brightness)
        set_color(new_image, x, y, gray)      
    return new_image

