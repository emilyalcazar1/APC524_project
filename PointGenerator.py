def PointGenerator(npoints: int, init_condition, xlim = 100, ylim = 100, zlim = 100):
    """
    This function generates the dictionary contaning the points and its associated coordinates
    can be passed on to the class SimulationGrid_3D, among others. Each of the npoints can either 
    be explicitly defined in the init_condition, or it can be situated using some of the defined 
    arrangements. 

    Arguments:
    npoints: (int) total number of points
    init_condition: the coordinate of each point,
                    OR a string which defines some possible arrangements

    """
    err_flag = 0;
    valid_param = ["random", "line","square"]
    grid = {}
        
    # checks that the argument passed into init_condition are valid
    if not isinstance(init_condition,list):
        err_flag = 1
    
    if isinstance(init_condition, str):
        err_flag = 2
        for i in range(len(valid_param)):
            if init_condition == valid_param[i]:
                err_flag = 0
    
    if err_flag != 0:
        if err_flag == 1:
            raise TypeError("Input argument for initial condition is not a nested list of coordinates or a string.")
        
        if err_flag == 2:
            raise TypeError("Input argument string for initial condition does not exist.")
    
    # if a list is passed, then its coordinates are matched with points
    if isinstance(init_condition,list):
        coord_dim = len(init_condition[0])
        
        # checks that the points passed all live in the same dimension of space
        for i in range(len(init_condition) - 1):
            if len(init_condition[i+1]) != coord_dim:
                raise TypeError("The points must be defined in the same dimensional space.")
            
        for i in range(len(init_condition)):
            grid[str(i)] = init_condition[i]
        return grid
    
    # randomly positioned points in 3D space
    if init_condition == "random":
        for i in range(npoints):
            x = random.randrange(0,xlim)
            y = random.randrange(0,ylim)
            z = random.randrange(0,zlim)
            grid[str(i)] = [x,y,z]
        return grid
    
    # points are all aligned along a line in the z-direction 
    if init_condition == "line":
        for i in range(npoints):
            grid[str(i)] = [0,0,i]
        return grid
    
    # points are all fitted onto a square in the xy-plane. 
    if init_condition == "square":
        maxlen = int(npoints**0.5)
        excess = npoints-maxlen**2
        
        for i in range(maxlen):
            for j in range(maxlen):
                grid[str(i*maxlen+j)] = [i,j,0]
        
        # if the number of points cannot exactly match a square, then the
        # extra points are fitting along the perimeter of the largest square.
        if excess > (maxlen + 1):
            for i in range(maxlen + 1):
                grid[str(maxlen*(maxlen+1)+i)] = [maxlen,i,0]
            for i in range(excess - maxlen - 1):
                grid[str(maxlen**2 + i)] = [i,maxlen,0]
            return grid
            
        else: 
            for i in range(excess):
                grid[str(maxlen**2 + i)] = [maxlen,i,0]
            return grid
    if init_condition == "line":
        for i in range(npoints):
            grid[str(i)] = [0,0,i]
        return grid
    
    if init_condition == "square":
        maxlen = int(npoints**0.5)
        excess = npoints-maxlen**2
        
        for i in range(maxlen):
            for j in range(maxlen):
                grid[str(i*maxlen+j)] = [i,j,0]
        
        
        if excess > (maxlen + 1):
            for i in range(maxlen + 1):
                grid[str(maxlen*(maxlen+1)+i)] = [maxlen,i,0]
            for i in range(excess - maxlen - 1):
                grid[str(maxlen**2 + i)] = [i,maxlen,0]
            return grid
            
        else: 
            for i in range(excess):
                grid[str(maxlen**2 + i)] = [maxlen,i,0]
            return grid
