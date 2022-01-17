# Created February 17th, 2020
# Last edited: February 20th, 2020
# Team Identifier: T082
# Authors:
   # Nicholai Ponomarev (Student #: 101182048)
   
# Imports all functions from the 'Cimpl' module:
from Cimpl import *

# Imports all filter function from the 'T082_image_filters' module:
from T082_image_filters import three_tone, posterize, extreme_contrast, \
     sepia, detect_edges, flip_horizontal, flip_vertical, draw_curve

# The approved list of commands which the user can choose from:
listOfApprovedCommands = ['L', 'S', '3', 'X', 'T', 'P', \
                          'E', 'D', 'V', 'H', 'Q']      
def userInputCode(): 
   if inputCommand not in listOfApprovedCommands: # Verifies that the input is one of the approved commands.
      print("\nNo such command")   

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
      
   elif inputCommand == "D": # Executes the draw_curve function if the input is 'D' or 'd'.
      curveImage = draw_curve(image, "cyan") # Hardcodes the color 'cyan' as curve colour.
      image = curveImage[0]
      show(image) 
      
   elif inputCommand == "V": # Executes the flip_vertical function if the input is 'V' or 'v'.
      image = flip_vertical(image) # Flips the image vertically.
      show(image)
      
   elif inputCommand == "H": # Executes the flip_horizontal function if the input is 'H' or 'h'.
      image = flip_horizontal(image) # Flips the image horizontally.
      show(image)