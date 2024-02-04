'''made by Layla (lserrano03@tamu.edu) and Zach (zachyb@tamu.edu)'''

import turtle as tr

import car_direct2 as cd

import styling as sty


tr.pensize(width=7)     # line sizing
tr.pencolor('#3F60E1')  # light blue color

img = tr.Turtle()

tr.register_shape('caraut.gif')
tr.shape('caraut.gif')

instruct = []

with open("Zach2StJo.txt", 'r') as directions:  # opening the file
    counter = 3  # setting counter to 3 to skip the first lines of file
    lines = directions.readlines()
    while counter < (len(lines) - 2):  # while loop until the last 2 lines of code
        data = lines[counter]  # getting string at index of counter from list of lines
        instruct = data
        data = data.strip('\n').split() # splitting the individual line into list
        distance = lines[counter + 1].split()  # getting the direction line from code and splitting
        improved_dist = []  # making a list of lines without ( or )
        for i in distance:  # iterating through the list
            new_str = i  # making sure if ( or ) are not in str, then it still gets appended to list
            if "(" in i:  # checking if ( in i
                new_str = i.translate({ord('('): None})  # deleting ( from str
            elif ")" in i:  # checking if ) in i
                new_str = i.translate({ord(')'): None})  # deleting ) from str

            improved_dist.append(new_str)  # appending new str without ( or ) improved_dist
        amount = cd.dist2(improved_dist)  # finding the distance the turtle should go

        tr.screensize(canvwidth=10000, canvheight=2000) # screen sizing to fit the graph
        cd.directions(data, amount)   # fuction call from car_direct2 using directions
        tr.pencolor('black')  # pen to black
        sty.writing(instruct) # prints directions
        tr.pencolor('#3F60E1')  # pen back to light blue color
        tr.bgcolor('grey')
        counter += 3  # skipping to next set of directions

tr.done()