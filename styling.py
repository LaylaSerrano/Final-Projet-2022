import turtle as tr

def writing(data):
    ''' Creates the writing and font style
        created by Layla Serrano (lserrano03@tamu.edu)
    '''
    tr.write(data, move=False, align= 'left', font=('Arial', 8, 'bold'),)
    
def exitcode():
    tr.write('OH NOOOOO :( Sorry can map out try again', move=False, align= 'left', font=('Arial', 8, 'bold'))
