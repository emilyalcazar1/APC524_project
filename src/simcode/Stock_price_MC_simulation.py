import numpy as np
import matplotlib.pyplot as plt
from Random_num_gen_matrix import *

def Stock_price_MC_sim(S: float, K: float, T: float, r: float, q: float, sigma: float, t_steps: int, N: int):
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
    
    -Return
    -[t_steps,N] matrix of asset paths 
    """
    # Type checks
    if type(S) != float:
            raise TypeError("S must be of type float")
    if type(K) != float:
            raise TypeError("K must be of type float")
    if type(T) != float:
            raise TypeError("T must be of type float")
    if type(r) != float:
            raise TypeError("r must be of type float")
    if type(q) != float:
            raise TypeError("q must be of type float")
    if type(sigma) != float:
            raise TypeError("sigma must be of type float")
    if type(t_steps) != int:
            raise TypeError("t_steps must be of type int")
    if type(N) != int:
            raise TypeError("N must be of type int")
            
    # Input Checks
    if S < 0.0:
            raise Exception("Stock price must be nonnegative")
    if K < 0.0:
            raise Exception("Strike must be nonegative")
    if T < 0.0:
            raise Exception("Time must be positive")
    if r < 0.0:
            raise Exception("interest rate must be positive")
    if q < 0.0:
            raise Exception("dividend interest rate must be positive")
    if t_steps < 0.0:
            raise Exception("time steps must be positive")
    if N < 0.0:
            raise Exception("Number of simulations must be positive")
    
    time_increments = T/t_steps
    
    Stock_price = np.log(S) +  np.cumsum(((r - q - sigma**2/2)*time_increments +\
                              sigma*np.sqrt(time_increments) * \
                              np.random.normal(size=(t_steps,N))),axis=0)
    
    return np.exp(Stock_price)

stock_price_MC_trials = Stock_price_MC_sim(150.0,111.0,2.0,0.1,0.02,0.3,100,100)
# print(stock_price_MC_trials)
plt.plot(stock_price_MC_trials)
plt.xlabel("time")
plt.ylabel("Monte Carlo Stock Price Simulations")

