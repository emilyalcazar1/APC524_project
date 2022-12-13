from SimulationGrid_3D import *

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

# This test should fail as the coordinates are not lists
def Failing_IncorrectDictInput():
    try:
        points = {'a':'1,2,3','b':(2,3,4)}
        SimulationGrid_3D(3,3,3,points)
        assert False
    except TypeError:
        assert True
    
# This test should fail as the coordinates are not 3D
def Failing_IncorrectDictInputDim():
    try:
        points = {'a':[1,2],'b':[1,2,3,4]}
        SimulationGrid_3D(3,3,3,points)
        assert False
    except TypeError:
        assert True

# This test should fail as a is out of bounds below in z
def Failing_OutOfBoundsBelow():
    try:
        points = {'a':[1,1,-1],'b':[2,2,2]}
        SimulationGrid_3D(3,3,3,points)
        assert False
    except:
        assert True
