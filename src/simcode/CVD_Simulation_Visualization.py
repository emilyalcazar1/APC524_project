def CVD_Simulation_Visualization(data):
    
    """
    This function is used to visualize all timesteps of the outputs
    of CVD_Simulation.py using a color map. This color map is updated
    following each timestep and the material growth is visualized. In
    addition to the initial and final steps, this function includes all
    intermediary steps.
    """
    
    # Save data as tottime
    tottime = data[1]

    # Procedure for visualizing the output of each timestep
    for i in range(len(tottime)):

        # Plots a figure at each timestep depicting the system and
        # species.
        fig, ax = plt.subplots()
        
        plt.figure(i)
        plt.ylabel('Material Height')
        plt.xlabel('Nucleation Sites')
        plt.tick_params(left = False, right = False , labelleft = False ,
                labelbottom = False, bottom = False)
        plt.imshow(np.flip(np.transpose((tottime[i]))),interpolation = 'none', cmap = 'gray_r')

        
def CVD_Simulation_Visualization_I_F(data):
    
    """
    This function only returns the initial(I) and final(F) arrangement
    of the system. It is useful to use when one is not interested in the
    intermediary steps.
    """
    
    # Aquare tottime from data array
    tottime = data[1]
    
    # Aquire time from data array
    time = data[4]

    fig, ax = plt.subplots()
    
    # Plot the Initial arrangement of the system
    plt.figure(1)
    plt.ylabel('Material Height')
    plt.xlabel('Nucleation Sites')
    plt.tick_params(left = False, right = False , labelleft = False ,
        labelbottom = False, bottom = False)
    plt.imshow(np.flip(np.transpose((tottime[0]))),interpolation = 'none', cmap = 'gray_r')
    
    # Plot the Final arrangement of the system
    plt.figure(2)
    plt.ylabel('Material Height')
    plt.xlabel('Nucleation Sites')
    plt.tick_params(left = False, right = False , labelleft = False ,
        labelbottom = False, bottom = False)
    plt.imshow(np.flip(np.transpose((tottime[len(time)-1]))),interpolation = 'none', cmap = 'gray_r')
