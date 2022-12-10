def CVD_Simulation(nsites = None,timesteps = None,cmax = None): 
    
    r1 = 0;
    
    rm1 = 500;
    
    r2 = 500;
    
    rm2 = 0;
    
    r3 = 500;

    ar = np.array([0,rm1,rm2 + r3,r1 + r2])
    
    tot = np.zeros((nsites,cmax))

    height = np.zeros((nsites,1))

    species = np.zeros((nsites,1))

    act = np.zeros((nsites,1))

    aveh = np.zeros((timesteps + 1,1))

    tota = np.zeros((timesteps + 1,1))

    time = np.zeros((timesteps + 1,1))


    for i in np.arange(0,nsites):
        
        tot[i,0] = 1
        
        tot[i,1] = 2
        
        height[i] = 2
        
        species[i] = 2
        
    tottime = []
    
    tottime.append(np.ndarray.tolist(tot))

    aveh[0] = 2

    time[0] = 0

    tm = 0

    for timestep in np.arange(0,timesteps):
        
        for i in np.arange(0,nsites):

            k = height[i]

            s = species[i]            

            act[i] = ar[int(s[0])-1]

        at = sum(act)

        acta = act / at

        ss = np.cumsum(acta)

        tota[0] = at

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

                if rm.randint(0,1) < r3 / (r3 + rm2):

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

            tota[timestep] = sum(act)

            tottime.append(np.ndarray.tolist(tot))

    return tot,tottime,height,species,time,aveh,tota
