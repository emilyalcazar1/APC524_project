import numpy as np
import random 
import math 


def function_example_1D(ran_vec: np.ndarray):
    """
        This function evaluates a function to approximate an integral via crude Monte Carlo simulations 
        and returns the cumulative sum of vector (1xn) of function evaluations.
        
    Args:
    - ran_vec np array of randomly generated numbers (np.ndarray)
    
    Return:
    - sum of n random function evaluations (np.float64)
    """
    
    if type(ran_vec) != np.ndarray:
            raise TypeError("ran_vec must be of type np.ndarray")
    
    # (e**(-1*x))/(1+(x-1)**2)
    e = 2.71828
    ran_func_vec = (e**(-1*ran_vec))*(1-ran_vec**3) 
    return np.sum(ran_func_vec)