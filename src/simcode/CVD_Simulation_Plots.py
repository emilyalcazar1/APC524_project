def CVD_Simulation_Plots(data): 

    """
    This function plots two figures to better quantify the
    output of CVD_Simulation. The first figure is a plot of 
    the overall surface activity of the system over time, and 
    the second figure is a plot of the average height of the
    system versus time.
    """
  
    # Aquire time from data array
    time = data[4]
    
    # Acquire average height from data array
    aveh = data[5]

    # Acquire total activity from data array
    totact = data[6]

    # Plot the overall surface activity versus time
    plt.figure(1)
    plt.plot(time[:-1],totact[:-1],'red')
    plt.xlabel('Time')
    plt.ylabel('Overall Surface Activity')

    # Plot the average height versus time
    plt.figure(2)
    plt.plot(time[:-1],aveh[:-1],'red')
    plt.xlabel('Time')
    plt.ylabel('Average Height')
