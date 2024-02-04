'''made by Layla (lserrano03@tamu.edu) and Zach (zachyb@tamu.edu)'''
import turtle as tr
import card_direct3 as cd
import styling as sty

tr.pensize(width=7)  # line width
tr.pencolor('#3F60E1')  # light blue color

img = tr.Turtle()

tr.register_shape('caraut.gif')
tr.shape('caraut.gif')

instruct = []

with open("Easterwood2Coulter.txt", 'r') as directions:  # opening the file
    counter = 0
    lines = directions.readlines()  # making list of lines in file
    del(lines[22])
    del(lines[28])
    del(lines[31])
    del(lines[37])


    while counter < len(lines):
        data = lines[counter]  # getting the str in list of lines at index of counter
        instruct = data
        data = data.strip('\n').split()  # splitting the str of directions into list
        distance = lines[counter + 1].split()  # splitting the str of distance into list
        if "min" in distance or "s" in distance:  # checking if min or s in distance to execute actual dist a diff way
            improved_dist = []
            for i in distance:  # iterates through list of distance
                new_str = i  # making sure if ( or ) not in str, it still gets appended onto improved list
                if "(" in i:  # checking if ( in str
                    new_str = i.translate({ord('('): None})  # deleting ( from str
                elif ")" in i:  # checking if ) in str
                    new_str = i.translate({ord(')'): None}) # deleting ) from str
                improved_dist.append(new_str)  # appending new str without ( or ) into new list
            amount = cd.dist3(improved_dist)  # getting the actual distance turtle should go
        else:  # if min or s not in it, then execute normal
            amount = cd.dist3(distance)  # getting the actual distance turtle should go
        cd.directs3(data, amount)  # function call from card_direct3 for directs3
        tr.pencolor('black')  # pen to black
        sty.writing(instruct) # writes out directions
        tr.pencolor('#3F60E1')  # pen back to light blue color
        tr.screensize(canvwidth=200000, canvheight=200000) # screen size width
        tr.speed(speed='fast')  # increases speed since it has a very long part toward the end
        tr.bgcolor('grey')
        counter += 3  # skipping to next set of directions

tr.done()