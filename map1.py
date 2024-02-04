#map 1
'''

made by Layla (lserrano03@tamu.edu) and Zach (zachyb@tamu.edu)

'''

import turtle as tr

import card_directs1 as cd

import styling as sty

tr.pensize(width=7)    # line sizing
tr.pencolor('#3F60E1')  # light blue color

img = tr.Turtle()  # gif used for the curser

tr.register_shape('caraut.gif')   # shape regestration
tr.shape('caraut.gif')   # shape assignment

with open("Kyle2VetPk.txt", 'r') as directions:  # opening the file
    counter = 3  # setting counter to 3 to skip the first lines of file
    lines = directions.readlines()  # making a list of all lines in file
    while counter < (len(lines)-2):  # while loop until the last 2 lines of code
        data = lines[counter]  # getting string at index of counter from list of lines
        instruct = data  # lists out the instructions so they'll be exicutes at the correct time
        
        data = data.strip('\n').split()  # splitting the individual line into list
        
        length = lines[counter+1].split()  # getting the direction line from code and splitting
        tr.screensize(canvwidth=10000, canvheight=2000)
        cd.direct(data, length)  # fuction call from car_direct1 using direct
        tr.pencolor('black')  # changes pen color to black
        sty.writing(instruct)  # prints out directions
        tr.pencolor('#3F60E1')  # changes pin back to a light blue color that way ou can see the directions
        tr.bgcolor('grey')

        counter += 3  # skipping the next set of directions
        
tr.done()







