import SimulationGrid_3D

# This test should pass
def PassingTest():
  try:
    points = {'a':[1,1,1],'b':[2,2,2]}
    SimulationGrid_3D(3,3,3,points)
    assert True
  except:
    assert False

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
