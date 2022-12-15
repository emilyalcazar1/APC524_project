"""
This file contains code to plot two figures to better
quantify the output of CVD_Simulation. The first figure
is a plot of the overall surface activity of the system
over time, and the second figure is a plot of the average
height of the system versus time.
"""

# Run CVD_Simulation 
data = CVD_Simulation(5,25,10) 

# Save data as tot
tottime = data[1]
time = data[4]
aveh = data[5]
totact = data[6]

# Plot the overall surface activity versus time
plt.figure(1)
plt.plot(time[:-1],totact[:-1],'red')
plt.xlabel('Time')
plt.ylabel('Overall Surface Activity')

# Plot the average height versus time
plt.figure(2)
plt.plot(time[:-1],aveh[:-1],'red')
plt.xlabel('Time')
plt.ylabel('Average Height')
