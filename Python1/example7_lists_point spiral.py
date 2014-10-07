import rhinoscriptsyntax as rs
import math

#Call rs.EnableRedraw(False)
for t in rs.frange(-50,50,1.25):
    arrPoint = [t*math.sin(5*t), t*math.cos(5*t), t]
    
    print(arrPoint)
    rs.AddPoint(arrPoint)
    #Call rs.EnableRedraw(True)