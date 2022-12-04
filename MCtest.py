import SimulationGrid_3D

# This test should pass
def PassingTest():
  try:
    points = {'a':[1,1,1],'b':[2,2,2]}
    SimulationGrid_3D(3,3,3,points)
    assert True
  except:
    assert False
    
# This test should fail since the input type for the points is not a dict
def Failing_IncorrectPoints1():
  try:
    points = [[0,0,0],[1,1,1]]
    SimulationGrid_3D(3,3,3,points)
    assert False
  except TypeError:
    assert True
    
# This test should fail as a is out of bounds above in z
def Failing_OutOfBoundsAbove():
  try:
    points = {'a':[1,1,4],'b':[2,2,2]}
    SimulationGrid_3D(3,3,3,points)
    assert False
  except:
    assert True

# This test should fail as a is out of bounds below in z
def Failing_OutOfBoundsBelow():
  try:
    points = {'a':[1,1,-1],'b':[2,2,2]}
    SimulationGrid_3D(3,3,3,points)
    assert False
  except:
    assert True
