import rhinoscriptsyntax as rs

idSurface = rs.GetObject("Surface to frame", 8, True, True)
faces = []

intCount = rs.GetInteger("Number of iterations per direction", 20, 2)

uDomain = rs.SurfaceDomain(idSurface, 0)
vDomain = rs.SurfaceDomain(idSurface, 1)
uStep = int((uDomain[1] - uDomain[0]) / intCount)
vStep = int((vDomain[1] - vDomain[0]) / intCount)

rs.EnableRedraw(False)
for u in range(int(uDomain[0]),int(uDomain[1]), int(uStep)):
    for v in range(int(vDomain[0]),int(vDomain[1]), int(vStep)):
        pt = rs.EvaluateSurface(idSurface, u, v)
        srfFrame = rs.SurfaceFrame(idSurface, [u, v])
        rs.AddPlaneSurface(srfFrame, 2.0, 2.0)
        #rs.AddEllipse(srfFrame, 1.0, 3.0)
        component = rs.GetObject("component to populate",rs.filter.mesh)
        faces = rs.MeshFaces(component, False)
        rs.AddMesh(faces, srfFrame)

rs.EnableRedraw(True)