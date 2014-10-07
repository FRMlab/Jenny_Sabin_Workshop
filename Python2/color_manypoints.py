import rhinoscriptsyntax as rs

def manypoints():
    pt=[]
    imax = rs.GetInteger("number of spheres in X-axis",5,1,10)
    jmax = rs.GetInteger("number of spheres in Y-axis",5,1,10)
    kmax = rs.GetInteger("number of spheres in Z-axis",5,1,10)

    for i in rs.frange(0,imax,1):
        for j in rs.frange(0,jmax,1):
            for k in rs.frange(0,kmax,1):
                #set up coordinate
                arrPointCoord = rs.AddPoint([i,j,k])
                pt.append(arrPointCoord)
                r = 0+(255-0)/(imax)*i
                g = 255-(0+(255-0)/(jmax)*j)
                b = (255/kmax*k)
                rs.ObjectColor(pt,[r,g,b])
    

manypoints()
