import sys
sys.path.insert(1, 'src/simcode')
from CVDsim import CVDsim

def test_PassingTest():
    try:
        CVDsim(5,10,10)
        assert True
    except:
        assert False
    
# This test should fail because there are zero sites being modeled
def test_Failing_NoSites():
    try:
        CVDsim(0,10,10)
        assert False
    except TypeError:
        assert True
