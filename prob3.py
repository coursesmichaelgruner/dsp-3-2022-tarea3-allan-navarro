#!/usr/bin/python3

from math import pi, sin, cos
import queue
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd

fig, ax = plt.subplots() #plot

r = 1

F0 = 440  # F0 = 440 Hz

fs = F0 * 30  # sampling rate, high so that plot looks nice

f = F0/fs  # discrete frequency

samples = 3/(1/fs)  # 3s of sound

w_0 = 2 * pi * f

n = 0 # current n
init = r*sin(w_0) #initial value r*sin(w_0)*d(n-1)

# the unit delay blocks are implemented as queues of 1 max value
q0 = queue.Queue(1)
q1 = queue.Queue(1)
q2 = queue.Queue(1)

q0.put(init) # insert the initial value 

ys = [] # to store the output samples

def get_value(q : queue.Queue):
    #retrieve value from queue, if empty return 0
    try:
        return q.get_nowait()
    except queue.Empty:
        return 0

'''
loop to generate the output samples using the difference equation
(view block diagram in pdf)
'''
while n < samples:
    d0 = get_value(q0) 

    d1 = get_value(q1)

    m1 = 2*r*cos(w_0) * d1

    d2 = get_value(q2)

    m2 = -r * r * d2

    y = d0 + m1 + m2

    q1.put(y)
    q2.put(d1)

    n += 1

    ys.append(y)

x = np.arange(0, samples)


ax.plot(x[0:100], ys[0:100])  # only show some values
sd.play(ys, fs, blocking=False)  # play generated tone

plt.show()
