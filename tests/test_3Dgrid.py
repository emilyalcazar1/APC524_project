import sys
sys.path.insert(1, 'src/simcode')
from SimulationGrid_3D import SimulationGrid_3D

def test_PassingTest():
    try:
        points = {'a':[1,1,1],'b':[2,2,2]}
        SimulationGrid_3D(3,3,3,points)
        assert True
    except:
        assert False
    
# This test should fail since the input type for the points is not a dict
def test_Failing_IncorrectPoints1():
    try:
        points = [[0,0,0],[1,1,1]]
        SimulationGrid_3D(3,3,3,points)
        assert False
    except TypeError:
        assert True
    
# This test should fail as a is out of bounds above in z
def test_Failing_OutOfBoundsAbove_z():
    try:
        points = {'a':[1,1,4],'b':[2,2,2]}
        SimulationGrid_3D(3,3,3,points)
        assert False
    except:
        assert True
        
# This test should fail as a is out of bounds above in y
def test_Failing_OutOfBoundsAbove_y():
    try:
        points = {'a':[1,4,1],'b':[2,2,2]}
        SimulationGrid_3D(3,3,3,points)
        assert False
    except:
        assert True
        
# This test should fail as a is out of bounds above in x
def test_Failing_OutOfBoundsAbove_x():
    try:
        points = {'a':[4,1,1],'b':[2,2,2]}
        SimulationGrid_3D(3,3,3,points)
        assert False
    except:
        assert True

# This test should fail as the coordinates are not lists
def test_Failing_IncorrectDictInput():
    try:
        points = {'a':'1,2,3','b':(2,3,4)}
        SimulationGrid_3D(3,3,3,points)
        assert False
    except TypeError:
        assert True
    
# This test should fail as the coordinates are not 3D
def test_Failing_IncorrectDictInputDim():
    try:
        points = {'a':[1,2],'b':[1,2,3,4]}
        SimulationGrid_3D(3,3,3,points)
        assert False
    except TypeError:
        assert True

# This test should fail as a is out of bounds below in z
def test_Failing_OutOfBoundsBelow_z():
    try:
        points = {'a':[1,1,-1],'b':[2,2,2]}
        SimulationGrid_3D(3,3,3,points)
        assert False
    except:
        assert True
        
# This test should fail as a is out of bounds below in y
def test_Failing_OutOfBoundsBelow_y():
    try:
        points = {'a':[1,-1,1],'b':[2,2,2]}
        SimulationGrid_3D(3,3,3,points)
        assert False
    except:
        assert True
        
# This test should fail as a is out of bounds below in x
def test_Failing_OutOfBoundsBelow_x():
    try:
        points = {'a':[-1,1,1],'b':[2,2,2]}
        SimulationGrid_3D(3,3,3,points)
        assert False
    except:
        assert True
