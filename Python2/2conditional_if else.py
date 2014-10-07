import rhinoscriptsyntax as rs
from math import*

for i in range(0,20):
    
    if (i%2==0): #i modular 2 (checks for remainder; what if we divide i by 2, is there a remainder
        rs.AddPoint([i,0,0])
    
    
    else:
        rs.AddSphere([i,0,0],0.3)
        
    
    