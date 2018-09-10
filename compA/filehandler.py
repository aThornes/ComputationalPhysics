#! C:\Program Files (x86)\Python\

'''FileHandler class (Attributes: contents)'''
class file(object):    
    #Initialises the class and reads from the file specified (filename)
    def __init__(self, filename):
        self.contents = [] # Initialises the list                
        f = open(filename) # Opens the file with the specified name
        lines = f.readlines() # Reads all lines from the file and adds them to a list
        self.contents = lines # Sets the contents attribute of the object to the previously defined list  
        self.rows = len(lines)
        f.close()
    
    #Returns a list of all values in the specified column within the file
    def getColumn(self, columnLine):        
        column = [] #Initialises a new list
        for i in range(self.rows): #A for loop for each of the rows found in the file
            if(self.contents[i][0] != '#'): #Ignores any row that starts with a '#'
                value = self.contents[i].split()[columnLine]
                try:
                    #Adds the section of the row within the column specified to the array
                    value = float(value)
                    column.append(value) 
                except:
                    None
                    #Will not add strings to the list (only float values can be added)
                
        return column #Returns a list with all the values found in that column
