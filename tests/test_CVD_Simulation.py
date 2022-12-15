import sys
sys.path.insert(1, 'src/simcode')
from CVD_Simulation import CVD_Simulation

def test_PassingTest1():
    try:
        CVD_Simulation(5,10,10)
        assert True
    except:
        assert False

def test_PassingTest2():
    try:
        CVD_Simulation(10,10,10)
        assert True
    except:
        assert False
        
def test_PassingTest3():
    try:
        CVD_Simulation(10,50,10)
        assert True
    except:
        assert False
        
def test_PassingTest4():
    try:
        CVD_Simulation(5,25,5)
        assert True
    except:
        assert False 
        
# This test should fail because there are zero sites being modeled
def test_Failing_NoSites():
    try:
        CVD_Simulation(0,10,10)
        assert False
    except IndexError:
        assert True

# This test should fail because the max height is set to zero
def test_Failing_NoHeight():
    try:
        CVD_Simulation(5,10,0)
        assert False
    except IndexError:
        assert True

# This test should fail because the timestep is set to zero
def test_Failing_NoTime():
    try:
        CVD_Simulation(5,0,10)
        assert False
    except IndexError:
        assert True
