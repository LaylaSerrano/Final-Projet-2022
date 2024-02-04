#  direcrions modual for map 1

import turtle as tr

def direct(data, length):
    #all
    ''' gives the turtle fucntion based on the directional lines for map 1

        made by Layla (lserrano03@tamu.edu) and Zach (zachyb@tamu.edu)

    '''
    if "north" in data:
        tr.setheading(90)
        dist(length)
        
    elif "south" in data:
        tr.setheading(270)
        dist(length)
        
    elif "west" in data:
        tr.setheading(180)
        dist(length)
        
    elif "east" in data:
        tr.setheading(0)
        dist(length)
        
    elif "northeast" in data:
        tr.setheading(45)
        dist(length)
        
    elif "northwest" in data:
        tr.setheading(135)
        dist(length)
        
    elif "southeast" in data:
        tr.setheading(315)
        dist(length)
        
    elif "southwest" in data:
        tr.setheading(225)
        dist(length)
        
    elif "right" in data:
        tr.right(angle=90)
        dist(length)
        
    elif "left" in data:
        tr.left(angle=90)
        dist(length)
        


def dist(amt):

    ''' Determains the length and put it to the correct scale for the turtle drawing

        made by Layla (lserrano03@tamu.edu) and Zach (zachyb@tamu.edu)

    '''
    
    amount = float(amt[0])  # getting the actual distance
    return tr.forward(amount*200)  # converting distance into noticable amount and making go forward





