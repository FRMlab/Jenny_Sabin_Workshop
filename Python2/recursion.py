import rhinoscriptsyntax as rs

#This one uses a really cool trick in python to manipulate all values in a list by a number.
 
def RecursiveScale(objID,scalePt,scaleFact, scaleVect, num):
    if num == 0:
        return 0
    else:
        sc = (1.0 / scaleFact)
        scaleVect = [x - sc for x in scaleVect] #this is the meat of the script (subtract each element of a list by a number)
        rs.ScaleObject(objID, scalePt, scaleVect, True)
        return RecursiveScale(objID, scalePt, scaleFact, scaleVect, num-1)
 
 
objID = rs.GetObject()
scalePt = rs.GetPoint("Pick Scale Center")
scaleFact = rs.GetReal("Enter a scale Factor", 10, 0)
scaleVect = [1.0, 1.0, 1.0]
num = rs.GetInteger("Enter a the number of iterations", 10, 1)
 
RecursiveScale(objID, scalePt, scaleFact, scaleVect, num)