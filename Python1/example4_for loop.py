import rhinoscriptsyntax as rs
import math

rs.EnableRedraw(False)
#Sin curve
numPoints = 30
freq = 6
scale = 4
pi = math.pi
radius = 5
points = []


for i in rs.frange(0,numPoints,.2):
    rads = (i/numPoints)*((2*pi)*freq)
    x = i*scale
    y = radius*math.sin(rads)
    z = 0
    
    n = rs.AddPoint([x,y,z])
    points.append(n)
    
    
rs.AddInterpCurve(points)
rs.EnableRedraw(True)

