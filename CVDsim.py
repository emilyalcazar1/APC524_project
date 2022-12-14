# Monte Carlo Simulation of Material Growth through Chemical Vapor Deposition

# Based on J. Emery's adaptation of C. Battaille and D. J. Srolovitz,
# Annual Reviews of Materials Research, 32,  2002.

# Call CVDsim(nsites, timesteps, hmax) to run

# Inputs:
#   nsites: Number of sites on the substrate surface where growth can occur
#   timesteps: Number of time steps for the reaction to occur
#   hmax: Maximum height material growth can reach (simulation will terminate)
#   reac: An array of the activity for each chemical species (Defined
#         inside the function)

# Outputs:
#   tot: An array of size [nsites x hmax] of the most recent timestep
#   tottime: An array of size [(nsites x hmax) x (timesteps + 1)] that compiles 
#            the tot matrix for each timestep
#   height: Array of material height at each site
#   species: Array of chemical species at each site
#   time: An arry of size [(timesteps + 1) x 1] of the time
#   totact: An array of size [(timesteps + 1) x 1] that compiles the overall
#           surface activity over time
#   aveh: An array of size [(timesteps + 1) x 1] that gives the 
#         average height of the system at each timestep

def CVDsim(nsites = None,timesteps = None,hmax = None): 
    
    # This function simulates the chemical vapor deposition, a method of material
    # growth, to better understand the underlying kinetics of the process. The
    # material growth is regulated by the characteristic reaction rates of specific
    # chemical reactions. For this reason, this code (the reaction rates) may be
    # adapted to simulate the material growth of different materials.
    
    # Define the reaction rates for the chemical reaction (material growth)
    r1 = 0;     # Rate of reaction 1 (forward direction)
    rv1 = 500;  # Rate of reaction 1 (reverse direction)
    r2 = 500;   # Rate of reaction 2 (forward direction)
    rv2 = 0;    # Rate of reaction 2 (reverse direction)
    r3 = 500;   # Rate of reaction 3 (forward direction)
    
    # Create matrix of the chemical species: [A(s), B(s), AB2(s), *(s)]
    reac = np.array([0,rv1,rv2 + r3,r1 + r2])
    
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

    for i in np.arange(0,nsites):
        
        tot[i,0] = 1
        
        tot[i,1] = 2
        
        height[i] = 2
        
        species[i] = 2
    
    tottime.append(np.ndarray.tolist(tot))

    aveh[0] = 2

    time[0] = 0

    tm = 0

    for timestep in np.arange(0,timesteps):
        
        for i in np.arange(0,nsites):

            k = height[i]

            s = species[i]            

            act[i] = reac[int(s[0])-1]

        at = sum(act)

        acta = act / at

        ss = np.cumsum(acta)

        totact[0] = at

        k = 0

        rand1 = rm.randint(0,1)

        for j in np.arange(0,nsites-1):

            if rand1 > ss[j]:

                k = k + 1

        t = species[k-1]

        h = height[k-1]

        if t == 2:

            tot[k-1][int(h[0])] = 4

            species[k-1] = 4

        else:

            if t == 3:

                if rm.randint(0,1) < r3 / (r3 + rv2):

                    tot[k][int(h[0])] = 1

                    tot[k][int(h[0])+1] = 2

                    species[k] = 2

                    height[k] = h + 1

                else:

                    tot[k][int(h[0])] = 4

                    species[k] = 4

            else:

                if t == 4:

                    if rm.randint(0,1) < r1 / (r1 + r2):

                        tot[k][int(h[0])] = 2

                        species[k] = 2

                    else:

                        tot[k][int(h[0])] = 3

                        species[k] = 3

            rand1 = rm.randint(0,1)

            dt = - np.log(rand1 + 0.01) / (at + 0.01)

            tm = tm + dt

            time[timestep] = tm

            sh = sum(height)

            aveh[timestep] = sh / nsites

            totact[timestep] = sum(act)

            tottime.append(np.ndarray.tolist(tot))

    return tot,tottime,height,species,time,aveh,totact
