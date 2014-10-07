import Rhino
import System.Drawing

#implement some custom drawing while a user is picking a point with the following script. 
#This script draws a Red and Blue line connected to the point under the mouse cursor while the user is picking a point.
 
def GetPointDynamicDrawFunc( sender, args ):
  pt1 = Rhino.Geometry.Point3d(0,0,0)
  pt2 = Rhino.Geometry.Point3d(10,10,0)
  args.Display.DrawLine(pt1, args.CurrentPoint, System.Drawing.Color.Red, 2)
  args.Display.DrawLine(pt2, args.CurrentPoint, System.Drawing.Color.Blue, 2)
 
# Create an instance of a GetPoint class and add a delegate for the DynamicDraw event
gp = Rhino.Input.Custom.GetPoint()
gp.DynamicDraw += GetPointDynamicDrawFunc
gp.Get()