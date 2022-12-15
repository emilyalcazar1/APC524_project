"""
Monte Carlo Simulation of Material Growth through Chemical Vapor Deposition

Based on J. Emery's adaptation of A Kinetic Monte Carlo method for the
atomic-scale simulation of chemical vapor deposition: Application to diamond.
Journal of Applied Physics, 82(12), 6293–6300. https://doi.org/10.1063/1.366532

Call CVDsim(nsites, timesteps, hmax) to run

Inputs:
  nsites: Number of sites on the substrate surface where growth can occur
  timesteps: Number of time steps for the reaction to occur
  hmax: Maximum height material growth can reach (simulation will terminate)
  reac: An array of the activity for each chemical species (Defined
         inside the function)

Outputs:
  tot: An array of size [nsites x hmax] of the most recent timestep
  tottime: An array of size [(nsites x hmax) x (timesteps + 1)] that compiles 
            the tot matrix for each timestep
  height: Array of material height at each site
  species: Array of chemical species at each site
  time: An arry of size [(timesteps + 1) x 1] of the time
  totact: An array of size [(timesteps + 1) x 1] that compiles the overall
           surface activity over time
  aveh: An array of size [(timesteps + 1) x 1] that gives the 
        average height of the system at each timestep
"""

import matplotlib as mpl
import numpy as np
import random as rm

import numpy as np
import random as rm

def CVDsim3(nsites = None,timesteps = None,hmax = None): 
    
    """
     This function simulates the chemical vapor deposition, a method of material
     growth, to better understand the underlying kinetics of the process. The
     material growth is regulated by the characteristic reaction rates of specific
     chemical reactions. For this reason, this code (the reaction rates) may be
     adapted to simulate the material growth of different materials.
    """
    
    # Define the reaction rates for the chemical reaction (material growth)
    r1 = 0;     # Rate of reaction 1 (forward direction)
    rv1 = 500;  # Rate of reaction 1 (reverse direction)
    r2 = 500;   # Rate of reaction 2 (forward direction)
    rv2 = 0;    # Rate of reaction 2 (reverse direction)
    r3 = 500;   # Rate of reaction 3 (forward direction)
    
    # Create matrix of the chemical species: [A(s), B(s), AB2(s), *(s)]
    reac = np.array([0,rv1,(rv2 + r3),(r1 + r2)])
    
    # Create empty matrices for the outputs
    tot = np.zeros((nsites,hmax))
    tottime = []
    height = np.zeros((nsites,1))
    species = np.zeros((nsites,1))
    time = np.zeros((timesteps + 1,1))
    totact = np.zeros((timesteps + 1,1))
    aveh = np.zeros((timesteps + 1,1))
    
    # Create empty matrices for additional necessary values
    act = np.zeros((nsites,1))
    
    # Create the initial state of the system
    for i in range(len(np.arange(0,nsites))):
        
        # This for loop sets the first layer of the model as species A
        # and the second layer of the model as species B
        
        tot[i,0] = 1
        tot[i,1] = 2
        height[i] = 2
        species[i] = 2
    
    tottime.append(np.ndarray.tolist(tot))      # Set the first total time array value
    
    aveh[0] = 2     # Set average height to 2 as the first two layers are occupied
    time[0] = 0     # Set the first value of the time array to zero
    tm = 0          # Set the total time equal to zero

    # Main body of the simulation that returns the final output matrices.
    for timestep in range(len(np.arange(1,timesteps+1))):
        
        # Loops through each timestep
        
        for i in range(len(np.arange(0,nsites))):
            
            # Calculates the activity at each site in the simulation.
            
            k = height[i]       # Edits row i of the height array
            s = species[i]      # Edits row i of the species array     
            act[i] = reac[int(s[0])-1]  # Finds the activity of species s in row i

        # Determine the total activity and activity per site
        at = sum(act)           # Total activity is the sum of all surface species
        avea = act / at         # Average activity at each surface site
        ss = np.cumsum(avea)    # Cumulative sum of the fractional activities
        totact[0] = at          # Set the initial value of totact as sum of activities

        # Pick the site at which a reaction will occur based on a randomly generated number
        # number (Monte-Carlo!) and the activity number line
        
        l = 0       # Reset l following each loop
        
        rand1 = rm.randint(0,1)     # Select a random value between 0 and 1 (Monte-Carlo!)
        
        for j in range(len(np.arange(0,nsites))):

            # Splits the system into j intervals
            
            if rand1 > ss[j]:
                
                # Returns an increased value of k if the cumulative sum of fractional
                # activities is less than the randomly generated number
                
                l = l + 1
        
        # Calculate the species and height at the selected site
        t = species[l-1]
        h = height[l-1]
        
        # Use randomly generated number to select the reaction, species, and height
        if t == 2:

            # If the second species (B(s)) is picked, the reaction k^-1 will proceed, 
            # changing B(s) into *(s).
            
            tot[l-1][int(h[0])-1] = 4
            species[l-1] = 4

        elif t == 3:
                
                # If the third species (AB2(s)) is picked, either reaction k^-2 or
                # k^3 will proceed, depending on the reaction rate.
                
            if rm.randint(0,1) < (r3 / (r3 + rv2)):
                    
                # Procedure if reaction k^-2 proceeds
                    
                tot[l-1][int(h[0])-1] = 1
                tot[l-1][int(h[0])] = 2
                species[l-1] = 2
                height[l-1] = h + 1

            else:

                # Procedure if reaction k^3 proceeds
                    
                tot[l][int(h[0])-1] = 4
                species[l] = 4

        elif t == 4:
                    
            # If the fourth species (*(s)) is picked, either reaction k^1 or
            # k^2 will proceed.
                    
            if rm.randint(0,1) < (r1 / (r1 + r2)):
                        
                # Procedure if reaction k^1 proceeds
                        
                tot[l-1][int(h[0])] = 2
                species[l-1] = 2

            else:

                # Procedure if reaction k^2 proceeds
                        
                tot[l-1][int(h[0])] = 3
                species[l-1] = 3

        # Calculate the change in time and the total time
        rand1 = rm.randint(0,1)
            
        # Set the timestep based on a randomly generated number and total activity
        dt = - np.log(rand1 + 0.0001) / (at + 0.0001) 
        tm = tm + dt    # Gives the next timestep
        time[timestep] = tm     # Change the time array
        toth = sum(height)      # Calculate the total height
            
        # Prepare outputs
        aveh[timestep] = toth / nsites  # Calculate the average height at each timestep
        totact[timestep] = sum(act)     # Calculate the total activity at each timestep
        tottime.append(np.ndarray.tolist(tot))  # Compile the data into tottime

    return tot,tottime,height,species,time,aveh,totact
