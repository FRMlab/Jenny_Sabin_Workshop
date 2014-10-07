import rhinoscriptsyntax as rs
#This script will compute a bunch of cross-product vector based on a pointcloud

def AddVector(vecdir, base_point=[0,0,0]):
    tip_point = rs.PointAdd(base_point, vecdir)
    line = rs.AddLine(base_point, tip_point)
    if line: return rs.CurveArrows(line,2)


def vectorfield():
    cloud_id = rs.GetObject("Input pointcloud", 2, True, True)
    if cloud_id is None: return
    
    listpoints = rs.PointCloudPoints(cloud_id)
    base_point = rs.GetPoint("Vector field base point")
    if base_point is None: return
    
    for point in listpoints:
        vecbase = rs.VectorCreate(point, base_point)
        vecdir = rs.VectorCrossProduct(vecbase, (0,0,1))
        if vecdir:
            vecdir = rs.VectorUnitize(vecdir)
            vecdir = rs.VectorScale(vecdir,2.0)
            AddVector(vecdir, point)
vectorfield()