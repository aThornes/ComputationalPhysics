from numpy import *
f=open('wind_expand.001.dat')
line=f.readline()
file=f.readlines()
f.close()
column_z=[]
column_x=[]
for m in range(len(file)):
    column_z.append(int(file[m].split()[1]))
    column_x.append(file[m].split()[3])
x=[]
x1=[]
x2=[]
x3=[]
#column_Z=array(column_z)
#j=[]
for i in range(len(column_z)):
	if(column_z[i] == column_z[i-1]):
		##Is the same so add to current list position, don't append
		print("Same")
	else:
		##not the same, append to list
		print("Not the same")
'''
    print(i,column_z[i])
    #why is column z[i] just wrong??
    if i == i[+1]:
        x1.append('Yo, Yo')
    if i != column_z[1:]:
        x2.append('Mo, Mo')
    else:
        x.append('this is a failure')

print('should be 92 x1s, 196 x2s and no xs')
len(x1)
'''