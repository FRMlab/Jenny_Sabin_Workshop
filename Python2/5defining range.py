import rhinoscriptsyntax as rs
from math import*


#for i in range(0,100):
    #rs.AddPoint([sin(i),i,0])#make 100 points where x coord. changes; 1 unit apart


i  = 0
while i<100: #while loop allows us to iterate while a condition is true
    rs.AddPoint([sin(i),i,0])
    i+=1 #whatever i is, add 1 to it