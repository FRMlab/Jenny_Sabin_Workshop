import rhinoscriptsyntax as rs

#recursive functions are functions that call themselves
 
def RecursiveCircle(pt, r):
    if r == 0: #value of r is 0; an equality check
        return 1
    else:
        rs.AddCircle(pt, r)
        return RecursiveCircle(pt, r-1)
 
 
pt = rs.GetPoint("Pick starting point")
 
RecursiveCircle(pt, 10)