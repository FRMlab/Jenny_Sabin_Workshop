import rhinoscriptsyntax as rs

#recursive functions are functions that call themselves

def RecursiveSquare(plane, u_dir, v_dir):
    
    if u_dir == 0: # an equality check
        return 1
        
        
    if v_dir == 0:
        return 1
    
    else:
        rs.AddPlaneSurface(plane, u_dir, v_dir)
        
        return RecursiveSquare(plane, u_dir, v_dir)
        
        
        
plane = rs.

RecursiveSquare(plane, 15, 15)