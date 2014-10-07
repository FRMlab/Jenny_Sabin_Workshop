import rhinoscriptsyntax as rs

num = rs.GetReal("line length x-dir")
line = rs.AddLine([9,7,2],[num,0,0])
print "curve inserted with id", line