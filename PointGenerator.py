def PointGenerator(npoints: int, init_condition, xlim = 100, ylim = 100, zlim = 100):
    err_flag = 0;
    valid_param = ["random"]
    grid = {}
    
    print(init_condition)
    
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
    
    if isinstance(init_condition,list):
        for i in range(len(init_condition)):
            grid[str(i)] = init_condition[i]
        return grid
    
    if init_condition == "random":
        for i in range(npoints):
            x = random.randrange(0,xlim)
            y = random.randrange(0,ylim)
            z = random.randrange(0,zlim)
            grid[str(i)] = [x,y,z]
        return grid
