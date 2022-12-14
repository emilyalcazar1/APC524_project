import numpy as np
import random 
import math 
from Random_num_gen_1D import random_num_gen_1D
from function_example_1D_eval import function_example_1D

def MC_1D_integral_eval(lower: float, upper: float, num_samples: int):
    """
        This function conducts the Monte Carlo simulation for a 1D arrangement of random numbers.
        
    Args:
    - lower: lower bound for evaluated integral (float)
    - upper: upper bound for evaluated integral (float)
    - num_samples: number of random samples for function eval (int)
    
    Return:
    - MC approximation of 1D integral evaluation (np.float64)
    """
    
    if type(num_samples) != int:
            raise TypeError("num_samples must be of type int")
    if type(lower) != float:
            raise TypeError("lower must be of type float")
    if type(upper) != float:
            raise TypeError("upper must be of type float")
    assert upper > lower,"upper bound is not greater than lower bound fix input such that upper>lower"
    
    ran_vec = random_num_gen_1D(lower,upper,num_samples)
    sum_ran_func_eval = function_example_1D(ran_vec)
    return (upper-lower)/num_samples * sum_ran_func_eval