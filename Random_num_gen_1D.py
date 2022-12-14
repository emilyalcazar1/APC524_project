import numpy as np
import random 
import math 

def random_num_gen_1D(min: float, max: float, n: int):
    """
        This function generates a random number between range: [min, max] for 1D Monte Carlo simulation.
        
    Args:
    - min (float) lower bound
    - max (float) upper bound
    - n (int) number of random numbers
    
    Return:
    - 1xn array of random numbers between [min, max] (float)
    """
    
    if type(n) != int:
            raise TypeError("n must be of type int")
    if type(min) != float:
            raise TypeError("min must be of type float")
    if type(max) != float:
            raise TypeError("max must be of type float")
    assert max > min,"max is not greater than min fix input such that max>min"
            
    return np.random.default_rng().uniform(min,max,size=n)


