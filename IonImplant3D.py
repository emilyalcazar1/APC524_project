import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class IonImplant3D:
    """
    This class takes in arguments of objects SimulationGrid_3D and Potential, and is used to simulate
    the process of ion implantation. There are several significant simplifying assumptions 
    as this whole implementation is created from scratch for this class. Firstly, all the 
    atoms were deposited on some initial position as defined in the SimulationGrid_3D class
    with the same kinetic energy. In addition, no additional atoms are introduced such that
    this process effectively describes the thermalization process after implantation. Lastly,
    the process of thermalization is dissipationless; that is, the random motion at each
    time step is governed by the same random number generator.

    Arguments:
    inputgrid: SimulationGrid_3D (class)
    potential: Potential (class)
    time: the number of time steps for the simulation.

    """
    
    def run(inputgrid: SimulationGrid_3D, potential: Potential, time: int, plot: bool):

        # Type checking
        if not isinstance(potential, Potential):
            raise TypeError("The argument for potential is not Potential or an inherited class of Potential")
        
        if not isinstance(inputgrid, SimulationGrid_3D):
            raise TypeError("The object passed for inputgrid is not of type SimulationGrid_3D")
        
        if type(time) != int:
            raise TypeError("time must be of type int")
        
        #declare arrays to store location history if plot is called.
        xhist = {}
        yhist = {}
        zhist = {}
        for i in inputgrid.points.keys():
            xhist[i] = [inputgrid.points[i][0]]
            yhist[i] = [inputgrid.points[i][1]]
            zhist[i] = [inputgrid.points[i][2]]
    
    #Pseudo-random movement of points subject to some potential
        for t in range(time):
            for i in inputgrid.points.keys():
                
            #Random Number Generator; due to random kinetic motion; up to
            #assume ten units of distance per time stamp
                random_kinetic = [random.randrange(-10,10),random.randrange(-10,10),random.randrange(-10,10)]
                for index in range(3):
                    inputgrid.points[i][index] += random_kinetic[index]

                for j in inputgrid.points.keys():
                    
                  #no repulsion from self
                    if i == j:
                        continue
                    
                    else:
                        point1 = inputgrid.points[i]
                        point2 = inputgrid.points[j]
                        distance = np.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2+(point1[2]-point2[2])**2)
                        
                                
                        # If two atoms are occupying the same position in the grid,
                        # let dist = 3 to overcome the singularity.
                        if distance == 0:
                            distance = 3;
                            
                        # find the force by calling the passed in potential;
                        # the charge is set to equal to 10
                        force_mag = int(potential.force(distance))
                        

                        #determines the force direction and magnitude in vector form
                        force_dir21 = np.array([point2[0]-point1[0],point2[1]-point1[1],point2[2]-point1[2]])/distance
                        force_dir21norm = np.round(force_dir21).astype(int)
                        force21 = force_mag * force_dir21norm
                        force12 = -1 * force21
                           
                        for index in range(3):
                            inputgrid.points[i][index] += force21[index]
                        
                        # apply equal and opposite force on the "other" particle j
                        for index in range(3):
                            inputgrid.points[j][index] += force12[index]
                
                # this makes sure that the atom is confined within the grid walls
                while inputgrid.points[i][0] >= inputgrid.x or inputgrid.points[i][0] < 0:
                    
                    if inputgrid.points[i][0] >= inputgrid.x:
                        residue_dist = inputgrid.points[i][0] - inputgrid.x
                        inputgrid.points[i][0] = inputgrid.x - residue_dist
                    
                    if inputgrid.points[i][0] < 0:
                        inputgrid.points[i][0] = -1 * inputgrid.points[i][0]
                    
                    if inputgrid.points[i][0] <= inputgrid.x and inputgrid.points[i][0] >= 0:
                        break

                while inputgrid.points[i][1] >= inputgrid.y or inputgrid.points[i][1] < 0:
                    
                    if inputgrid.points[i][1] >= inputgrid.y:
                        residue_dist = inputgrid.points[i][1] - inputgrid.y
                        inputgrid.points[i][1] = inputgrid.y - residue_dist
                    
                    if inputgrid.points[i][1] < 0:
                        inputgrid.points[i][1] = -1 * inputgrid.points[i][1]
                        
                    if inputgrid.points[i][1] <= inputgrid.y and inputgrid.points[i][1] >= 0:
                        break

                while inputgrid.points[i][2] >= inputgrid.z or inputgrid.points[i][2] < 0:
                    
                    if inputgrid.points[i][2] >= inputgrid.z:
                        residue_dist = inputgrid.points[i][2] - inputgrid.z
                        inputgrid.points[i][2] = inputgrid.z - residue_dist
                    
                    if inputgrid.points[i][2] < 0:
                        inputgrid.points[i][2] = -1 * inputgrid.points[i][2]
                        
                    if inputgrid.points[i][2] <= inputgrid.z and inputgrid.points[i][2] >= 0:
                        break
                    
                if plot == True:
                    xhist[i].append(inputgrid.points[i][0])
                    yhist[i].append(inputgrid.points[i][1])
                    zhist[i].append(inputgrid.points[i][2])

                    
        if plot == True:
            fig = plt.figure(figsize=(10,10))
            ax = fig.add_subplot(111, projection='3d')
            for i in inputgrid.points.keys():
                ax.plot(xhist[i],yhist[i],zhist[i])

            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_zlabel('z')
            ax.set_xlim(0,inputgrid.x)
            ax.set_ylim(0,inputgrid.y)
            ax.set_zlim(0,inputgrid.z)
            plt.show()
                
