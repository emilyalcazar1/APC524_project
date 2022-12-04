import random
import numpy as np

class IonImplant(inputgrid: SimulationGrid_3D, potential: Potential):
  time: int
  
  #Random Number Generator; due to random kinetic motion; up to
  #ten units of distance per time stamp
  a = random.randrange(-10,10)

  #Add a bias due to coulombic repulsion
  for i in range(len(inputgrid.points.keys())):
    for j in range(len(inputgrid.points.keys())):
      #no repulsion from self
      if i == j:
        pass
      else:
        point1 = inputgrid.points(i)
        point2 = inputgrid.points(j)
        distance = np.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2+(point1[2]-point2[2])**2)
        force = potential.force(1,1,distance)
        
      
      
