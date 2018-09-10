import filehandler as fh

#Get elemental abundance
def getAbundance(file):
    #Define lists
    z_elementNum = []
    x_element = []
    zVal = file.getColumn(1) #Get file column 2
    xVal = file.getColumn(3) #Get file column 4
    '''
    prevVal is used to check the current col1 value with the last thereby
    informing the program whether to start a new z value or not, note this depends on the
    z values being in order in the file as they currently are.
    '''
    prevVal = -1    
    for i in range(file.rows-1):
        if(zVal[i] != prevVal): #Only adds to the list if the z value is a new value
            z_elementNum.append(zVal[i]) #Adds a new z value to the element,Z, number list
            x_element.append(xVal[i]) #Adds a new x value to the element list
        else:
            #Adds the new value to the existing x value if the z value is the same as previous
            x_element[len(x_element)-1] += xVal[i] 
        prevVal = zVal[i] #Sets the previous z value to the current ready for the next loop pass
    return {'z':z_elementNum, 'x':x_element} #Returns the two lists which are callable by the names 'z' and 'x'
    
    #Write data to a file
def writeToFile(filename, col1, col2, col3, col4, header):    
    file = open(filename, 'w+') #Opens the file (will create the file if it does not exist)
    for i in range(4):
        bigSpace = False
        if(i==1 or i==2): 
            bigSpace = True        
        writeLine(file, header[i], bigSpace)
    file.write('\n') #Start a new line
    for i in range(len(col1)): #Repeats for all rows
        a = writeLine(file, str(int(col1[i])), False) #Write col1 to file
        b = writeLine(file, str(col2[i]), True) #Write file 1 abundances (converting numbers to string)
        c = writeLine(file, str(col3[i]), True) #Write file 2 abundances (converting numbers to string)
        d = writeLine(file, str(col4[i]), False) #Write file 3 abundances (converting numbers to string)
        if(i != len(col1) - 1):
            file.write('\n') #Start a new line if not on last line
    file.close() #Close the file
    
def writeLine(file, inp, large): #Writes the line to the file with the correct spacing(same for all string lengths)
    #file = The file to write to
    #inp = the string to write
    #large = boolean value whether to add a large space
    space = 4 - len(inp)
    if(large): #If large space then use 30 spaces between start of string and the next string
        space = 30 - len(inp)   
    file.write(inp) #Writes the line to file    
    for i in range(space):
        file.write(" ") #Write x number of spaces to the file as defined before