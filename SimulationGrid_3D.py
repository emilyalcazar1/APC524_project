class SimulationGrid_3D:
    """
    This class acts as a parent class to all simulation work that involves points
    inside a 3D grid. It explicitly defines the size of the simulation box and the
    number of points in each grid. 
    
    
    Arguments:
    x, y, z: (int) grid size along each direction
    points: (dict) name and location (array of length 3) of each point
    
    
    
    Functions:
    GridPlot: Uses matplotlib to plot all the points; not recommended for large grids. 
    
    """
    def __init__(self, x_length: int, y_length: int, z_length: int, points: dict):
        self.x = x_length
        self.y = y_length
        self.z = z_length
        self.points = points
        
        # The data type of points needs to be a list
        if not isinstance(points, dict):
            raise TypeError()
        
        # Ensures that no points exist outside the grid size
        set_coords = points.values()
        
        x_coords = [list(set_coords)[i][0] for i in range(len(points.keys()))]
        y_coords = [list(set_coords)[i][1] for i in range(len(points.keys()))]
        z_coords = [list(set_coords)[i][2] for i in range(len(points.keys()))]

        
        if max(x_coords) > x_length or min(x_coords) > x_length or max(x_coords) < 0 or min(x_coords) < 0:
            raise TypeError("Points exist out of bounds of x")
            
        if max(y_coords) > y_length or min(y_coords) > z_length or max(y_coords) < 0 or min(y_coords) < 0:
            raise TypeError("Points exist out of bounds of y")
            
        if max(z_coords) > y_length or min(z_coords) > z_length or max(z_coords) < 0 or min(z_coords) < 0:
            raise TypeError("Points exist out of bounds of z")
