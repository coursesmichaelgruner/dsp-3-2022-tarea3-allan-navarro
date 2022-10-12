#!/usr/bin/python3

from math import pi, sin, cos
import queue
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd


fig, ax = plt.subplots()
r = 1

F = 440  # 440 Hz

fs = F * 30  # sampling rate

f = F/fs  # discrete frequency

samples = 3/(1/fs)  # 3s of sound

w_0 = 2 * pi * f

counter = 0
init = r*sin(w_0)

q0 = queue.Queue(1)
q1 = queue.Queue(1)
q2 = queue.Queue(1)

q0.put(init)

ys = []

while counter < samples:
    try:
        d0 = q0.get_nowait()
    except queue.Empty:
        d0 = 0

    try:
        d1 = q1.get_nowait()
    except queue.Empty:
        d1 = 0

    m1 = 2*r*cos(w_0) * d1

    try:
        d2 = q2.get_nowait()
    except queue.Empty:
        d2 = 0

    m2 = -r * r * d2

    y = d0 + m1 + m2

    q1.put(y)
    q2.put(d1)

    counter += 1

    ys.append(y)

x = np.arange(0, samples)


ax.plot(x[0:100], ys[0:100])  # only show some values
sd.play(ys, fs, blocking=False)  # play generated tone

plt.show()
