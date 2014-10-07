import rhinoscriptsyntax as rs
from math import*

rs.EnableRedraw(False)

for i in range(0,40):
    
    if (i%5==0): #i modular 5; every 5th element will be a point
        rs.AddPoint([i,0,0])
    
    
    else:
        rs.AddSphere([i,0,0],0.3)
        
rs.EnableRedraw(True)    
    