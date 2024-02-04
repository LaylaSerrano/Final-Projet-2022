# map 2  cardinal directions

import turtle as tr

def directions(data, amount):
    ''' gives the turtle fucntion based on the directional lines for map 1

            made by Layla (lserrano03@tamu.edu) and Zach (zachyb@tamu.edu)

        '''
    if ("north" in data) or ("N/S" in data):
        tr.setheading(90)
        tr.forward(amount)
    elif "south" in data:
        tr.setheading(270)
        tr.forward(amount)
    elif "west" in data:
        tr.setheading(180)
        tr.forward(amount)
    elif ("east" in data) or ("E" in data):
        tr.setheading(0)
        tr.forward(amount)
    elif "northeast" in data:
        tr.setheading(45)
        tr.forward(amount)
    elif "northwest" in data:
        tr.setheading(135)
        tr.forward(amount)
    elif "southeast" in data:
        tr.setheading(315)
        tr.forward(amount)
    elif "southwest" in data:
        tr.setheading(225)
        tr.forward(amount)
    elif "right" in data:
        tr.right(angle=90)
        tr.forward(amount)
    elif "left" in data:
        tr.left(angle=90)
        tr.forward(amount)
    elif "Continue" in data:
        tr.right(angle=90)
        tr.forward(amount)


def dist2(line):
    ''' Finds the distance that the marker should travel and converts miles
        and feet proportional

        made by Zach (zachyb@tamu.edu)

    '''

    amount = float(line[2])  # getting miles or feet the turtle should go into float
    if "mi" in line:  # if miles
        return amount * 500  # making the distance traveled noticable in pop up
    elif "ft" in line:  # if ft
        return (amount / 5280) * 500  # convert ft to miles, then makes the distance noticable in pop up





