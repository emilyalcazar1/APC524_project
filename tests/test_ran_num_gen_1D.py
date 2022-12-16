import sys
sys.path.insert(1, 'src/simcode')
from Random_num_gen_1D import random_num_gen_1D

def test_upper_bound():
    try:
        max(random_num_gen_1D(0.0,10.0,10)) < 10.0
        assert True
    except:
        assert False
        
def test_lower_bound():
    try:
        min(random_num_gen_1D(0.0,10.0,10)) > 1.0
        assert True
    except:
        assert False
        
