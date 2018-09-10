#Import other python files
import filehandler as fh
import dataManipulation as dm
#Import needed libraries
import matplotlib.pyplot as py

highlight = [30,38,56,74,75,82] #Z values to be highlighted (Can be any numbers between 1 and 92)

#Load all files
wind1 = fh.file('wind_expand.001.dat')
wind3 = fh.file('wind_expand.003.dat')
wind5 = fh.file('wind_expand.005.dat')

#Calculate the elemental abundances in mass fraction for each file(two lists ['z'] and ['x'])
abundance1 = dm.getAbundance(wind1)
abundance3 = dm.getAbundance(wind3)
abundance5 = dm.getAbundance(wind5)

response = input("Show data on graph? (Y/N)") #Gets the input from user whether to show graph or not
if(response == "y" or response == "Y"):
    print("Loading graph")
    print("Close graph to continue...")
    py.figure(figsize=(16,8)) #Set the size of the figure
    py.title('Abundances of each elemental mass fraction', color='b', y=1.04) #Write the title (slightly raised in y dir_n)

    #Plot each of the dataset abundances on the graph with the semilog plot
    py.semilogy(abundance1['z'],abundance1['x'], marker = "*")
    py.semilogy(abundance3['z'],abundance3['x'], marker = "o")
    py.semilogy(abundance5['z'],abundance5['x'], marker = "x")
    #Display the legend for the plot
    py.legend(['wind_expand.001','wind_expand.003','wind_expand.005'])
    #Set the x and y axis lables
    py.xlabel('Atomic number, Z')
    py.ylabel('Elemental Abundance')
    #Limit the graph from 10^8 to 1.5 on the y axis
    py.ylim(1E-8, 1.5)
    #Limit the graph from 25 to 83 on the x axis
    py.xlim(25,83)
    elementF = fh.file('elements.dat') #Load elements file
    elements = elementF.contents #Get contents from elements files    
    for i in range(len(highlight)): #Draws a vertical line at each of the points in the highlight list   
        py.axvline(highlight[i], color='y')
        try: #Try statement to ensure program does not fail when i=len(highlight)
            if(highlight[i+1]-highlight[i] < 2): #If the difference between adjacent highlight points is smaller than 2 then..
                #Offset it by one point to avoid the numbers being written over each other
                py.annotate(elements[highlight[i]-1], xy=(highlight[i]-1, 1.5))  
            else:
                py.annotate(elements[highlight[i]-1], xy=(highlight[i], 1.0)) #Writes the annotation by the vertical highlight line
        except:
            py.annotate(elements[highlight[i]-1], xy=(highlight[i], 1.5))#Writes the annotation by the vertical highlight line  
    py.show() #Shows the plot
response = input("Write data to file? (Y/N)")  #Gets the input from user whether to write to file or not
if(response == "y" or response == "Y"):
    #Writes the data to the file specified
    dm.writeToFile("rprocess_data.txt",abundance1['z'],abundance1['x'],abundance3['x'],abundance5['x'],["Z", "Wind_expand.001 abundance", "Wind_expand.003 abundance","Wind_expand.005 abundance"] )
    print("File successfully created...")