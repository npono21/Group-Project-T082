#Created February 18th, 2021
#Last edited: February 20th, 2021
#Team Identifier: T082
#Authors:
   #Igbinosa Uhunmwagho (Student #: 101187781)
   #Hamson Olotu (Student #: 101204718)
   
#Import Statement:
#Import all functions from the 'Cimpl' module:
from Cimpl import *
   
#Import all filter function from 'T082_image_filters' module:
from T082_image_filters import three_tone, posterize, extreme_contrast, \
        sepia, detect_edges, flip_horizontal, flip_vertical, draw_curve

print("\nProgram Initializing!\n")
                                                     
filename = input("What is the name of the batchfile?\n :") #User inputs batchfile name.
batch_file = open(filename)  #Opens batchfile corresponding to user input.
image = load_image(choose_file())   #choose image to apply filters too.
for line in batch_file:
   
   items = line.split(" ")
   components = items[0], items[1]
   
   image_copy = copy(image)  # Using a copy of the image to avoid making changes to the original image
   list_of_filters = []
   
   for i in range(2, len(items)):    #add filters to be applied to a list
      list_of_filters += items[i]
         
   
   for operation in list_of_filters:   
   
      if operation == '3':
         image_copy = three_tone(image_copy, "blood", "cyan", "gray") #Hardcoded applied colours.
         show(image_copy) #Shows resulting filtered image.
         
      if operation == 'X':    
         image_copy = extreme_contrast(image_copy) #Calls on imported
         show(image_copy)                          #func to apply filter.
         
      if operation == 'P':
         image_copy = posterize(image_copy) #Calls on imported
         show(image_copy)                   #func to apply filter.
         
      if operation == 'V':
         image_copy = flip_vertical(image_copy) #Calls on imported
         show(image_copy)                       #func to apply filter.
         
      if operation == 'H':
         image_copy = flip_horizontal(image_copy) #Calls on imported
         show(image_copy)                         #func to apply filter.
      
      if operation == 'T':
         image_copy = sepia(image_copy) #Calls on imported
         show(image_copy)               #func to apply filter.
         
      if operation == 'E':
         thresholdvalue = int(15)
         image_copy = detect_edges(image_copy, thresholdvalue) #Calls on imported
         show(image_copy)                                      #func to apply filter.
   


   save_as(image_copy, items[1]) #save image changes to file specified

print("\nProgram Terminating!")

batch_file.close()  #Closes the batch file. 