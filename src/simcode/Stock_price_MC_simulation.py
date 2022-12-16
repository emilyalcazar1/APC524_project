import numpy as np
import matplotlib.pyplot as plt
from Random_num_gen_matrix import random_num_gen_matrix

def Stock_price_MC_sim(S: float, K: float, T: float, r: float, q: float, sigma: float, t_steps: int, N: int, min: float, max: float):
    """
        This function calls the random matrix generator to conduct MC simulations to predict stock prices. 
        The MC simulation will be conductedN times at each time step to visualize the potential paths to the time until expired time.
    Args
    -S = Current stock Price
    -K = Strike
    -T = Time to expiration date
    -r = risk free interest rate
    -q = dividend yield interest rate
    -sigma = volatility (standard deviation)
    -t_steps = time steps
    -N = number of MC trials
    -min = lower bound of randomly selected numbers
    -max = upper bound of randomly selected numbers
    
    -Return
    -[t_steps,N] matrix of asset paths 
    """
    
    time_increments = T/steps
    ran_gen_matrix = random_num_gen_matrix(min, max, t_steps, N)
    
    Stock_price = np.log(S) +  np.cumsum(((r - q - sigma**2/2)*time_increments +\
                              sigma*np.sqrt(time_increments) * \
                              ran_gen_matrix),axis=0)
    
    return np.exp(Stock_price)

stock_price_MC_trials = geo_paths(S,T,r, q,sigma,steps,N)
plt.plot(stock_price_MC_trials);
plt.xlabel("time")
plt.ylabel("Monte Carlo Stock Price Simulations")

