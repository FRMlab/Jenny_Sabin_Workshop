import rhinoscriptsyntax as rs
import math

def flange(typeofFlange):

    #variables
    points = [] #collection
    nP = 100
    nSin = 10


    #conditional assignment

    if (typeofFlange == "floppy"):
        t = 3
        r = 15
        amp = 10
        
    if (typeofFlange == "extrafloppy"):
        t = 3
        r = 30
        amp = 20

#iteration to calculate points
    for i in rs.frange(0, nP, 1):
        x = r * math.sin(i*360/(nP-1))
        y = r * math.cos(i*360/(nP-1))
        z = amp*math.sin(i*nSin*360/(nP-1))
#Feature
        point = rs.AddPoint([x,y,z])
        points.append(point)


    
flange("floppy")



