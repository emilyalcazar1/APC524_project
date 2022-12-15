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
        CVD_Simulation(10,25,15)
        assert True
    except:
        assert False 
        
# This test should fail because there are zero sites being modeled
def test_Failing_NoSites():
    try:
        CVD_Simulation(0,10,10)
        assert False
    except TypeError:
        assert True
