import sys
sys.path.insert(1, 'src/simcode')
from Random_num_gen_1D import random_num_generator

def test_upper_bound():
    assert max(random_num_generator(0.0,10.0,10)) < 10.0
