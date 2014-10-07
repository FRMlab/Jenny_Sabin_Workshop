import rhinoscriptsyntax as rs
import math

#Sub waveGrid
rowSpace = 3
colSpace = 3
limit = 20
arrPoints = [limit, limit] #array to hold points
pi = math.pi
amp = 3
startTheta = 0
freq = 6

rs.EnableRedraw(False)

for rows in rs.frange(0,limit,1):
    for cols in rs.frange(0,limit,1):
    
        #equate cols loop to angle slices around a circle ( angles in radians )
        #+ starting point on the circle
            rad = ((cols/limit)*(2*math.pi)) + startTheta
            x = cols*colSpace
            y = rows*rowSpace
            z = (math.sin(rad * freq)*amp)
            n = rs.AddPoint([x,y,z])


    #iterate between rows
    startTheta = startTheta + ((2*math.pi)*(cols/limit))
rs.EnableRedraw(True)



