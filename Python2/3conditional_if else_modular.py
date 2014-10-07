import rhinoscriptsyntax as rs
from math import*

rs.EnableRedraw(False)

for i in range(0,40):
    
    if (i%5==0): #i modular 2 (checks for remainder; what if we divide i by 2, is there a remainder? if there is not, it adds a point(2 fits perfectly into i));checks for even numbers and adds a point; easy way of doing sequences
        rs.AddPoint([i,0,0])
    
    
    else:
        rs.AddSphere([i,0,0],0.3)
        
    
    