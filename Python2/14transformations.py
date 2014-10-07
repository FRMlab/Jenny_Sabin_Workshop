#Transformations

#we take a look at vectors and how to create simple object transformations using them.
#Specifically, we creat some vectors to translate the position of a point and copy it to a new location using the CopyObject() method.
#We thing create a polyline though the list of translated and copied points. 
 
import rhinoscriptsyntax as rs
import random
 
#ask user to create a point
userPt = rs.GetPoint("create a point")
pt = rs.AddPoint(userPt)
 
#create a list of points and append pt to the list
pts = []
pts.append(pt)
 
for i in range(0,100):
    xDir = random.uniform(-10.0, 10.0)
    yDir = random.uniform(-10.0, 10.0)
    zDir = 0.0
    vect = (xDir, yDir, zDir)
    newPt = rs.CopyObject(pts[-1],vect) #last created point (will always grab the last one in the list; transformed by our vector
    pts.append(newPt)
 
myPolyline = rs.AddPolyline(pts)