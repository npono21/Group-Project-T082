#batch_interface

from Cimpl import *
from T046_image_filters import *
from filter_function import filter_selection

file_name = input("Enter the batch file name: ")

read_file = open(file_name)

for line in read_file:
    current_test = line.split()
    num_function = len(current_test) - 2
    image = load_image(current_test[0])
    destination = current_test[1]
    for i in range(num_function):
        index = i + 2
        command = str.upper(current_test[index])
        image = filter_selection(command,image)
    save_as(image,destination)

#batch_interface_file.txt