import matplotlib.pyplot as plt
import numpy as np
import serial
import time


Fs = 300

t = np.arange(0,10,1/10)

x = np.zeros(100) 
y = np.zeros(100)
z = np.zeros(100) 

serdev = '/dev/ttyACM0'

s = serial.Serial(serdev,115200)

for i in range(300):
    line=s.readline()
    if(i%3 == 0): x[int(i/3)] = float(line)
    elif(i%3 == 1): y[int(i/3)] = float(line)
    elif(i%3 == 2): z[int(i/3)] = float(line)

tilt = np.zeros(100)

origin = [x[0],y[0],z[0]]
# ori_len = np.sqrt(np.square(abs(origin[0]))+np.square(abs(origin[1]))+np.square(abs(origin[2])))
# thres = np.sqrt(2)/2

ti = 0
thedis = 0

for i in range(1,100):

    dis_x = 9.8*(x[i])*0.1*0.1*100/2

    thedis += dis_x
    if thedis > 5 or thedis < -5:   tilt[i] = 1
    else:   tilt[i] = 0


fig, ax = plt.subplots(2, 1)

ax[0].plot(t,x, label = 'x')
ax[0].plot(t,y, label = 'y')
ax[0].plot(t,z, label = 'z')
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Acc Vector')
ax[0].legend()

ax[1].stem(t,tilt) 
ax[1].set_xlabel('Time')
ax[1].set_ylabel('Horizontal Displacement')

plt.show()

s.close()