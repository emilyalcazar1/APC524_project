import random
import numpy as np

class IonImplant(inputgrid: SimulationGrid_3D, potential: Potential):
  time: int
  

  #Pseudo-random movement of points subject to some potential
  for i in range(len(inputgrid.points.keys())):
    #Random Number Generator; due to random kinetic motion; up to
    #ten units of distance per time stamp
    random_kinetic = [random.randrange(-10,10),random.randrange(-10,10),random.randrange(-10,10)]
    
    for j in range(len(inputgrid.points.keys())):
      #no repulsion from self
      if i == j:
        pass
      else:
        point1 = inputgrid.points(i)
        point2 = inputgrid.points(j)
        distance = np.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2+(point1[2]-point2[2])**2)
        
        force_mag = int(potential.force(1,1,distance))
        force_dir12 = np.array([point1[0]-point2[0],point1[1]-point2[1],point1[2]-point2[2]])/distance
        force_dir12norm = np.round(force_dir12).astype(int)
        force12 = force_mag * force_dir12norm
        
        
      
      
