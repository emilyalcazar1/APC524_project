# This file is used to visualize the outputs of CVDsim.py
# using a color map. This color map is updated following each
# timestep. Additionally, the overall surface activity and
# average height are plotted as a function of time.

# Run CVDsim 
data = CVDsim(5,10,10,1) 

# Save data as tot
tot = data[1]

# Procedure for colormapping of the outputs
for i in range(len(tot)):
    
    # Plot the species as a specific color
    
    plt.figure(i)
    plt.imshow(tot[i],interpolation = 'none', cmap = 'gray_r')

# Plot the overall surface activity versus time
plt.figure(1)
plt.plot(time,totact,'red')
plt.xlabel('Time')
plt.ylabel('Overall Surface Activity')

# Plot the average height verus time
plt.figure(2)
plt.plot(time,aveh,'red')
plt.xlabel('Time')
plt.ylabel('Average Height')
