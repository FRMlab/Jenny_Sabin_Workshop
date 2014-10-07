import rhinoscriptsyntax as rs

def myFunction(object,translation):
    rs.MoveObject(object,translation)
    print("translation successful")
    
strObject = rs.GetObject("pick an object",4) 
#pick geometry from screen, hit F1 to check arguments/inputs, filter specifies object

print(strObject) #specific identifier

myFunction(strObject, [20,0,0])


