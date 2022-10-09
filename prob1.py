#!/usr/bin/python3

import sounddevice as sd
import numpy as np
import sys

fs = 44100
queue = []
counter = 0

if len(sys.argv) != 2:
    print('need to specify delay D in ms')
    exit(1)

D = int(sys.argv[1])

if D < 0:
    print('D must be >= 0')
    exit(1)

delay_samples = (D/1000) * fs

try:
    with sd.Stream(samplerate=fs, dtype='int16', latency='low', channels=1,blocksize=1) as stream:
        while True:
            read_available=stream.read_available
            data,oflow = stream.read(read_available)

            queue.append(data)

            if counter > delay_samples:
                stream.write(queue.pop(0))
            else:
                stream.write(np.zeros((100,1),dtype=np.int16))
            counter += read_available

except KeyboardInterrupt:
    pass

print('end')