data = CVD_Simulation(5,10,10,1)
tot = data[1]

for i in range(len(tot)):
    plt.figure(i)
    plt.imshow(tot[i],interpolation = 'none', cmap = 'gray_r')
    
plt.figure(1)
plt.plot(time,tota,'red')
plt.xlabel('Time')
plt.ylabel('Overall Surface Activity')

plt.figure(2)
plt.plot(time,aveh,'red')
plt.xlabel('Time')
plt.ylabel('Average Height')
