import turtle as tr

def directs3(data, amount):
    ''' gives the turtle fucntion based on the directional lines for map 1

                made by Layla (lserrano03@tamu.edu) and Zach (zachyb@tamu.edu)

    '''

    if "right" in data:
        tr.right(angle=90)
        tr.forward(amount)
    elif "left" in data:
        tr.left(angle=90)
        tr.forward(amount)
    elif "south" in data:
        tr.setheading(270)
        tr.forward(amount)
    elif "west" in data:
        tr.setheading(180)
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
    elif ("east" in data) or ("E" in data):
        tr.setheading(0)
        tr.forward(amount)
    elif ("north" in data) or ("N/S" in data):
        tr.setheading(90)
        tr.forward(amount)
    elif "Continue" in data and 'Frontage' in data:
        tr.forward(amount)
    elif "Continue" in data and 'Turkey' in data:
        tr.forward(amount)
    elif "Continue" in data and 'F' in data:
        tr.right(angle=90)
        tr.forward(amount)

def dist3(line):
    ''' Finds the distance that the marker should travel and converts miles
            and feet proportional

            made by Zach (zachyb@tamu.edu)

    '''

    if "min" in line or "s" in line:  # checking if nim or s in to see which index the true distance should be
        amount = float(line[2])  # getting the true distance
        if "mi" in line:  # checking if mi
            return amount * 750  # making the distance traveled noticable in pop up
        elif "ft" in line: # checking if ft
            return (amount / 5280) * 750  # converting ft to miles, making the distance traveled noticable in pop up
    else:  # as long as min or s not in line
        amount = float(line[0])  # execute as normal indexing
        if "mi" in line:  # doing the same conversions as above
            return amount * 750
        elif "ft" in line:
            return (amount / 5280) * 750