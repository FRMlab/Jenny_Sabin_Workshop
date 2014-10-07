import rhinoscriptsyntax as rs
import math
from System.Drawing import Color


#define a mobius strip surface
xy =(10,10)


o=-0.5
p=0.5
op=1/(xy[0])


vp =2*math.pi
vpstep=vp/(xy[1])


points = []
a=2


for i in rs.frange(-0.5,0.5,op):
    for j in rs.frange(0,vp,vpstep):
        b=j/2
        x=math.cos(j)*(a+i*math.cos(b))
        y=math.sin(j)*(a+i*math.cos(b))
        z=i*math.sin(b)
        pt = x,y,z
        points.append(pt)


xy=(xy[0]+1,xy[1]+1)


rs.AddLayer('surface',Color.Black)
srf=rs.AddSrfPtGrid(xy, points)
rs.ObjectLayer(srf,'surface')


rs.EnableRedraw(False)


