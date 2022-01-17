# Created February 17th, 2020
# Last edited: February 20th, 2020
# Team Identifier: T082
# Authors:
   # Nicholai Ponomarev (Student #: 101182048)
   # Sibyl Chang (Student #: 101181655)
   
# Imports all functions from the 'Cimpl' module:
from Cimpl import *

# Imports all filter function from the 'T082_image_filters' module:
from T082_image_filters import three_tone, posterize, extreme_contrast, \
     sepia, detect_edges, flip_horizontal, flip_vertical, draw_curve

# The approved list of commands which the user can choose from:
listOfApprovedCommands = ['L',  'S', '3', 'X', 'T', 'P', \
                          'E', 'D', 'V', 'H', 'Q']   
                                                         
print("\nProgram Initialiazing!") # Welcome message.

inputCommand = "" # Initializes the inputCommand as an empty string.
image = None # Initializes the image as type None.

# This loop will run as long as inputCommand is not 'Q' or 'q'.
while inputCommand != "Q": 
   inputCommand = input("\nL)oad image  S)ave-as  \n3)-tone  X)treme contrast"\
                        "  T)int sepia  P)osterize  \nE)dge detect  D)raw curve"\
                        "  V)ertical flip  H)orizontal flip \nQ)uit\n\n: ").upper()
   # The .upper() command changes any inputted lowercase to its uppercase letter. 
   # This gives the user the flexibility to input either lower or upper case letters when prompted.
               
   if inputCommand not in listOfApprovedCommands: # Verifies that the input is one of the approved commands.
      print("\nNo such command")   
      
   elif inputCommand == "L": # Executes the load_image function if the input is 'L' or 'l'.
      image = load_image(choose_file()) # Allows the user to choose an image.
      show(image) # Displays the chosen image.
      
   elif type(image) != Image: # Checks if an image has been loaded. 
      print("\nNo image loaded") 
      
   elif inputCommand == "S": # Executes the save_as function if the input is 'S' or 's'.
      filename = input("\nWhat would you like to save your image as: ") # User designates the filename and type.
      save_as(image, filename) # Opens the file directory to save the image.
      
   elif inputCommand == "3": # Executes the three_tone function if the input is '3'.
      image = three_tone(image, "blood", "cyan", "gray") # Hardcodes the applied colours.
      show(image) # Displays the filtered image.
      
   elif inputCommand == "X": # Executes the extreme_contrast function if the input is 'X' or 'x'.
      image = extreme_contrast(image) # Applies the extreme contrast filter.
      show(image) 
      
   elif inputCommand == "T": # Executes the sepia function if the input is 'T' or 't'.
      image = sepia(image) # Applies the sepia filter.
      show(image) 
      
   elif inputCommand == "P": # Executes the posterize function if the input is 'P' or 'p'.
      image = posterize(image) # Applies the posterize filter.
      show(image) 
      
   elif inputCommand == "E": # Executes the detect_edges function if the input is 'E' or 'e'.
      thresholdInput = int(input("\nWhat threshold would you like: ")) # User inputs a desired threshold for the filter.
      image = detect_edges(image, thresholdInput) # Applies the edge detection filter.
      show(image) 
      
      #The following code is commented out to not impeded the script because the curve drawing #filter does not work correctly.
      """
   elif inputCommand == "D": # Executes the draw_curve function if the input is 'D' or 'd'.
      curveImage = draw_curve(image, "cyan") # Hardcodes the color 'cyan' as curve colour.
      image = curveImage[0]
      show(image) 
      
      """
      
   elif inputCommand == "V": # Executes the flip_vertical function if the input is 'V' or 'v'.
      image = flip_vertical(image) # Flips the image vertically.
      show(image)
      
   elif inputCommand == "H": # Executes the flip_horizontal function if the input is 'H' or 'h'.
      image = flip_horizontal(image) # Flips the image horizontally.
      show(image)
      
print("\nProgram now Terminated!") # Final message at the end of the program.

