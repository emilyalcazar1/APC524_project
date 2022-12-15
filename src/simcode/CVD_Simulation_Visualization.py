"""
This file is used to visualize the outputs of CVD_Simulation.py
using a color map. This color map is updated following each
timestep and the material growth is visualized.
"""

# Run CVD_Simulation
data = CVD_Simulation(5,25,10) 

# Save data as tottime
tottime = data[1]

# Procedure for visualizing the output of each timestep
for i in range(len(tottime)):
    
    # Plots a figure at each timestep depicting the system and
    # species.
    
    plt.figure(i)
    plt.imshow(tottime[i],interpolation = 'none', cmap = 'gray_r')
