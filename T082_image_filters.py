#Created February 8th, 2020
#Team Identifier: T082
#Authors:
   #Nicholai Ponomarev (Student #: 101182048)
   #Hamson Olotu (Student #:101204718)
   #Igbinosa MatthewUhunmwagho (Student #: 101187781)
   #Sibyl Chang (Student #: 101181655)
   
#Import Statement:
#Import all functions from the 'Cimpl' module.
from Cimpl import *

from simple_Cimpl_filters import grayscale

#Colour Filter Function Definition:
#red_channel function definition written by Nicholai Ponomarev (#101182048):
def red_channel(image: Image) -> Image:
 
 """
 Team Identifier: T082
 Author: Nicholai Ponomarev (Student #: 101182048)
 Returns a copy of the original image with
 the blue and green colours filtered out only leaving
 the red channel. This copy is then saved under the 
 name "redImage" as a JPEG file in the same folder
 containing this code and the 'Cimpl' module source 
 code.
 >>> original_image = load_image(choose_file())
 >>> redFilter = red_channel(original_image)
 >>> show(redFilter)
 """

 redFilterImage = copy(image)
  
 #Filter out the green and blue channel to only leave 
 #the red channel.
 for pixel in redFilterImage:
  x, y, (r, g, b) = pixel
  redColour = create_color(r, g*0, b*0)
  set_color(redFilterImage, x, y, redColour)
  #print(x, y, ":", r, g, b)
 return redFilterImage

#green_channel function definition written by Igbinosa MatthewUhunmwagho (Student #: 101187781):
def green_channel(image: Image)->Image:
    """
    Team Identifier: T082
    Author: Igbinosa MatthewUhunmwagho (Student #: 101187781)
    Returns a green filtered copy of image.
    >>> original_image = load_image(choose_file())
    >>> greenFilter = green_channel(original_image)
    >>> show(greenFilter)
    """
    green_image = copy(image)
    
    for pixel in green_image:
        x,y, (r, g, b) = pixel
        
        green = create_color(r*0, g, b*0)
        set_color(green_image, x, y, green)
    return green_image
   
#blue_channel function definition written by Sibyl Chang (Student #: 101181655):
def blue_channel(image: Image) -> Image:
    """
    Team Identifier: T082
    Author: Sibyl Chang (Student #: 101181655)
    Returns a copy of an image with only the blue channel present
    >>> img = load_image(choose_file()) 
    >>> blue_img = blue_filter(img)
    >>> show(blue_img)
    
    """
    new_img = copy(image) # Copies the image
    
    # Filters out the red and green channel
    for pixels in new_img:
        x, y, (r, g, b) = pixels
        blue_color = create_color( r * 0, g * 0, b )
        set_color(new_img, x, y, blue_color)
    return new_img
   
#combine function definition written by Hamson Olotu (Student #:101204718):
def combine(image1: Image, image2: Image, image3: Image) -> Image:
    """
    Team Identifier: T082
    Author: Hamson Olotu (Student #: 101204718)
    Returns the combined image of the three images and reverses the effects 
    of the red, green and blue filters applied to the images. Assumptions: The 
    images are the same but are just different in color. The images in the 
    parameters are in the order: red, green, and blue.
    >>> image1 = load_image(choose_file())
    >>> image2 = load_image(choose_file())
    >>> image3 = load_image(choose_file())
    >>> greenFilter = green_channel(image1, image2, image3)
    >>> show(combinedImage)
    """
    
    combined_image = copy(image1)
    for pixel in image1:
        x, y, (r, g, b) = pixel
        red, green1, blue1 = get_color(image1, x, y)
        red2, green, blue2 = get_color(image2, x, y)
        red3, green3, blue = get_color(image3, x, y)
        new_color = create_color(red, green, blue)
        set_color(combined_image, x, y, new_color)
    
    return combined_image
   
#Main Filter Function Definitions:
#P3 Three_tone filter function definition written by Nicholai Ponomarev (#101182048):
def three_tone(image: Image, col1: str, col2: str, col3: str) -> Image:
    """
    Author: Nicholai Ponomarev (Student #: 101182048)
    Team Designation: T082
    This filter takes the brightness of each pixel in the image
    and according to that brightess, it will change the color of 
    the respective pixel to either color 1, 2 or 3 to 
    make the image only have three tones. If the 
    brightness is between 0 and 84, the pixel is changed to color 1, 
    if the brightness is between 85 and 170, the pixel is changed 
    to color 2 and if the brightness is between 171 and 255, the pixel 
    is changed to colour. The colors are selected from the initialized 
    list of colors above.
    >>> original_image = load_image(choose_file())
    >>> Above line can be replace with hardcoded 'original_image = load_image("XXX")
        where 'XXX' represents the file name of the respective image.
    >>> threeTonedFilter = three_tone(original_image, "cyan", "blood", "green")
    >>> show(threeTonedFilter)
    """

    threeTonedImage = copy(image)
    colors = [col1, col2, col3] #Initialize list called colors that takes three inputs.
    newColors = [] #Initialize a new empty list that will take color choices.
    
    for choice in colors:
        if choice == "black".lower(): #added '.lower()' for future use when user input will be required.
            newColors.append((0, 0, 0)) #Adds black to newColors list if choice.
        elif choice == "white".lower():
            newColors.append((255, 255, 255))#Adds white to newColors list if choice.
        elif choice == "blood".lower():
            newColors.append((255, 0, 0)) #Adds blood to newColors list if choice.
        elif choice == "green".lower():
            newColors.append((0, 255, 0)) #Adds green to newColors list if choice.
        elif choice  == "blue".lower():
            newColors.append((0, 0, 255)) #Adds blue to newColors list if choice.
        elif choice == "lemon".lower():
            newColors.append((255, 255, 0)) #Adds lemon to newColors list if choice.
        elif choice == "cyan".lower():
            newColors.append((0, 255, 255)) #Adds cyan to newColors list if choice.
        elif choice == "magenta".lower():
            newColors.append((255, 0, 255)) #Adds magenta to newColors list if choice.
        elif choice == "gray".lower():
            newColors.append((128, 128, 128)) #Adds gray to newColors list if choice.
            
    
    for pixel in threeTonedImage:
        x, y, (r, g, b) = pixel
        brightness = (r + g + b)//3 #Calculate the brightness of each individual pixel.
        if brightness >= 0 and brightness <= 84:
            (R, G, B) = newColors[0] #Initializes it in the first index of the newColors list.
            newColor = create_color(R, G, B) #Creates a new color according to the brightness and the col2 str.
        elif brightness >= 85 and brightness <= 170:
            (R, G, B) = newColors[1]            
            newColor = create_color(R, G, B)
        elif brightness >= 171 and brightness <= 255:
            (R, G, B) = newColors[2]            
            newColor = create_color(R, G, B)
        set_color(threeTonedImage, x, y, newColor) #Sets every pixel to one of the three colors according
                                                   #to its brigthness.
    return threeTonedImage #Returns the new filtered image. 

#P3 Posterize filter function definition written by Igbinosa MatthewUhunmwagho (Student #: 101187781):
def posterize(image: Image) -> Image:
    """
    Team Identifier: T082
    Author: Igbinosa MatthewUhunmwagho (Student #: 101187781)
    Returns the posterized copy of an image.
    
    >>>original_image = load_image(choose_file())
    >>>posterizeImage = posterize(original_image)
    >>>show(posterizeImage)
    """
    posterize_image = copy(image)
    for pixel in posterize_image:
        x,y, (r, g, b) = pixel 
        r=_adjust_component(r)
        g=_adjust_component(g)
        b=_adjust_component(b)
        
        posterized = create_color(r,g,b)
        set_color(posterize_image, x, y, posterized)        
    
    return posterize_image
        

def _adjust_component(rgb_value:int )-> int:
    """
    Returns the midpoint of the pixels's red, green, or blue component by 
    range-checking.
    
    >>>_adjust_component(25)
    31
    >>>_adjust_component(136)
    159
    >>>_adjust_component(192)
    223
    """ 
    if rgb_value >=0 and rgb_value<=63:
        return 31
    if rgb_value>=64 and rgb_value<=127:
        return 95
    if rgb_value>=128 and rgb_value<=191:
        return 159
    if rgb_value>= 192 and rgb_value<=255:
        return 223  
    
#P3 Extreme_contrast filter unction definition written by Sibyl Chang (Student #: 101181655):
def extreme_contrast(img: Image) -> Image:
    """
    Author: Sibyl Chang | 101181655
    Team: T082
    
    Returns a copy of an image which maximizes or minimizes the
    contrast between the pixels depending on the component's value. For instance, 
    if the component's value is between 0 and 127, the value is changed to
    0 and if it is between 128 to 255, the value os changed to 255.
    >>> img = load_image(choose_file())
    >>> extreme_img = extreme_contrast(img)
    >>> show(extreme_img)
    """
    
    new_img = copy(img) # Copies the original image
    
    for pixels in img:
        x, y, (r, g, b) = pixels
        color = get_color(img, x, y) 
        
        # Gets the color of the pixels in the original image
        red = get_color(img, x, y) [0]
        green = get_color(img, x, y) [1]
        blue = get_color(img, x, y) [2]
        
        # Sets the RGB values depending on the conditions below
        if 0 <= red <= 127:
            red = 0
        if 128 <= red <= 255:
            red = 255
        if 0 <= green <= 127:
            green = 0
        if 128 <= green <= 255:
            green = 255
        if 0 <= blue <= 127:
            blue = 0
        if 128 <= b <= 255:
            blue = 255  
            
        set_color(new_img, x, y, Color(red,green,blue))
    return new_img

#P3 Sepia filter function definition written by Hamson Olotu (Student #:101204718):
def sepia(image: Image) -> Image:
    """
    Team Identifier: T082
    Author: Hamson Olotu (Student #: 101204718)
    Returns the image with a sepia tint applied to it.
    
    >>> image = load_image(choose_file())
    >>> filtered_image = sepia_filter(image)
    >>> show(image)
    """
    
    new_image = copy(image)
    grayscale_image = grayscale(image)
    
    for x, y, (r, g, b) in grayscale_image:
        if r < 63:
            set_color(new_image, x, y, create_color(r * 1.1, g, b * 0.9))
        elif 63 <= r <= 191:
            set_color(new_image, x, y, create_color(r * 1.15, g, b * 0.85))
        elif r > 191:
            set_color(new_image, x, y, create_color(r * 1.08, g, b * 0.93))
    return new_image

#P4 Edge_detection filter function definition written by Nicholai Ponomarev (#101182048):
def detect_edges(image: Image, threshold: int) -> Image:
    """
    Author: Nicholai Ponomarev (Student #: 101182048)
    Team Designation: T082
    This filter compares the contrast between a pixel
    and the pixel directly below it. If the contrast is 
    above a designated threshold, which is a positive integer,
    it will turn the top pixel to black and if the contrast is
    below a designatedthreshold, it will turn the top pixel to white. 
    The filter automatically turns the bottom row of pixels to white.
    The goal of this filter is to produce an image that 
    resembles a pencil drawing.
    >>> original_image = load_image(choose_file())
    >>> finalProduct = detect_edges(original_image, 21)
    >>> show(finalProduct)
    """
    
    filteredImage = copy(image) #Creates a copy of image. 
    
    imageWidth = get_width(filteredImage) #Gets width of image in pixels.
    imageHeight = get_height(filteredImage) #Gets height of image in pixels.
    
    white = create_color(255, 255, 255)
    black = create_color(0, 0, 0)
    
    for x in range(imageWidth):
        for y in range(imageHeight-1):
            
            r, g, b = get_color(filteredImage, x, y) #Gets the color of each top pixel.
            R, G, B = get_color(filteredImage, x, (y+1)) #Gets the color of each bottom pixel.
            
            brightnessTopPixel = (r + g + b) // 3 #Determine the brightness of each top pixel.
            brightnessBottomPixel = (R + G + B) // 3 #Determine the brightness of each bottom pixel.
            
            contrast = abs(brightnessTopPixel - brightnessBottomPixel) #Formula for determining contrast.
            
            if contrast > threshold: #If the contrast is larger than the threshold, the pixel changes to black.
                set_color(filteredImage, x, y, black)
            else: #If the contrast is smaller than the threshold, the pixel changed to white.
                set_color(filteredImage, x, y, white)
                
    #Following code makes the bottom line white.
    for x in range(imageWidth):
        set_color(filteredImage, x, imageHeight-1, white)
        
    return filteredImage #Returns the image. 


#P4 Horizontal Flipping filter function definition written by Igbinosa MatthewUhunmwagho (Student #: 101187781):
def flip_horizontal(image: Image) -> Image:
    """
    Team Identifier: T082
    Author: Igbinosa Matthew Uhunmwagho (Student #: 101187781)
    Returns the copy of an image flipped along the vertical line. That is, 
    flipped left to right.
    
   >>>original_image = load_image(choose_file())
   >>>flipped_image = flip_horizontal(original_image)
   >>>show(flipped_image)
    
    """
    
    flipped_image = copy(image)
    
    width = get_width(flipped_image)
    height = get_height(flipped_image)
    
    
    for x in range(width):
        for y in range(height):
            rgb = get_color(image, x, y)
            flipped_image.set_color((width - 1) - x, y, rgb)
        
    return flipped_image

#P4 Vertical Flipping filter function definition written by Sibyl Chang (Student #: 101181655):
def flip_vertical(img: Image) -> Image:
    """
    Author: Sibyl Chang | 101181655
    Team: T082
    
    Returns a copy of an image that is flipped along a horizontal line.
    
    >>> img = load_image(choose_file())
    >>> flipped_img = flip_vertical(img)
    >>> show(flipped_img) 
    
    """
    new_img = copy(img) # Copies the original image
    
    # Gets the height and the width of the copied image
    width = get_width(new_img)
    height = get_height(new_img)    
    
    for y in range(height):
        for x in range(width):
            pixel = get_color(img, x, y) # Gets the color of the pixel
            new_img.set_color(x, (height - 1) - y, pixel) # Flips the pixels along a horizontal line
    return new_img # Returns the flipped image of the original image

#P4 Draw_curve function definition written by Hamson Olotu (Student #:101204718):
#Updated version from previous submission but still does not meet correct 
#requirements

black = (0, 0, 0)
white = (255, 255, 255)
blood = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
lemon = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
grey = (128, 128, 128)

def _exhaustive_search(max_x: int, polycoeff: list, val: int):
    """Returns
    """
    if len(polycoeff) == 3:
        a, b, c = polycoeff
        d = b ** 2 - 4 * a * (c - val)
        ans = ""
        x1 = 0
        x2 = 0
        if d < 0:
            ans = "None"
        elif d >= 0:
            x1 = (b + math.sqrt(d)) / (2 * a)
            x2 = (b - math.sqrt(d)) / (2 * a)
        if 0 <= x1 <= max_x:
            if 0 <= x2 <= max_x:
                return x2
            else:
                return x1 
        elif ans == "None":
            return None
        else:
            return None
    else:
        m, b = polycoeff
        x = (val - b) / m
        if 0 <= x <= max_x:
            return x
        else:
            return None
        
    
    
    
def _image_border_findings(image_size: list, polynom: list):
    """Returns
    """
    pixel_x = image_size[0] - 1
    pixel_y = image_size[1] - 1
    
    horizontal1 = _exhaustive_search(pixel_x, polynom, 0)
    horizontal2 = _exhaustive_search(pixel_x, polynom, pixel_y)
    vertical1 = np.polyval(polynom, 0)
    vertical2 = np.polyval(polynom, pixel_x)
    if 0 <= vertical1 <= pixel_y:
        vertical1 = vertical1
    else:
        vertical1 = "None"
    if 0 <= vertical2 <= pixel_y:
        vertical2 = vertical2
    else:
        vertical2 = "None"
        
    borders = [horizontal1, horizontal2, vertical1, vertical2]
    
    count = 0
    coordinates = []
    
    for i in range(len(borders)):
        if type(borders[i]) == int:
            count += 1
            if i == 0:
                coordinates.append((borders[i], 0))
            elif i == 1:
                coordinates.append((borders[i], pixel_y))
            elif i == 2:
                coordinates.append((0, borders[i]))
            elif i == 3:
                coordinates.append((pixel_x, borders[i]))
        else:
            count += 0
            
    coordinates.sort()
    return coordinates
    
    
def _interpolation(list_of_points: list) -> list:
    """
    """
    x = []
    y = [] 
    
    for i in range(len(list_of_points)):
        x.append(list_of_points[i][0])
        y.append(list_of_points[i][1])
        
    if len(list_of_points) == 2:
        z = np.polyfit(x, y, 1)
    else:
        z = np.polyfit(x, y, 2)
        
    return z
        

def draw_curve(image: Image, color: str,  pointlist: list = None) -> tuple:
    """
    Team Identifier: T082
    Author: Hamson Olotu (Student #: 101204718)
    Returns an image with a curve drawn on it.
    >>> draw_curve(image[0])
    """
    image_copy = copy(image)
    image_width = get_width(image)
    image_height = get_height(image)
    size_of_image = [image_width, image_height]
    line_color = color.lower()
    if pointlist == None:
        print("The image size is " + str(image_width) + " pixels wide "\
        + "and " + str(image_height) + " pixels high!")
        points = int(input("How many data points would you like to use?\n :"))
        points_list = []
        points_list.sort()
        if 2 <= points <= 3:
            count = 1
            while count <= int(points):
                list1 = [int(input("x" + str(count) + ":")), int(input("y" + str(count) + ":"))]
                points_list.append(tuple(list1))
                count += 1
            curve = _interpolation(points_list)
        elif points > 3:
            count = 1
            while count <= int(points):
                list1 = [int(input("x" + str(count) + ":")), int(input("y" + str(count) + ":"))]
                points_list.append(tuple(list1))
                count += 1
            curve = _interpolation(points_list)
        else:
            print("Please enter 2 or more points")
    else:
        curve = _interpolation(pointlist)
    
    border_findings = _image_border_findings(size_of_image, curve)
    lspace = np.linspace(0, image_width, 20)
    x_points = lspace
    y_points = np.polyval(curve, x_points)
    
    
    save_as(image_copy, "img.jpg")
    image_new = plt.imread("img.jpg")
    plt.xlim([0, image_width])
    plt.ylim([0, image_height])    
    plt.plot(x_points, y_points, color= line_color, linewidth= 5)
    plt.imshow(image_new, extent=[0, image_width, 0, image_height])
    plt.axis('off')
    plt.savefig('final.jpg')
    final_image = load_image('final.jpg')
    
    
    return (final_image, border_findings)
    







