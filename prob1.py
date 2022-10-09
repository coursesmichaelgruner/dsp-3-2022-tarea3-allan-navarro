#!/usr/bin/python3

import sounddevice as sd
import numpy as np
import sys

fs = 44100  # sample rate
samples = []  # queue to store samples
read_samples = 0  # counter of read samples

if len(sys.argv) != 2:
    print('need to specify delay D in ms')
    exit(1)

D = int(sys.argv[1])  # delay in ms

if D < 0:
    print('D must be >= 0')
    exit(1)

delay_samples = (D/1000) * fs  # delay expressed in number of samples

try:
    with sd.Stream(samplerate=fs, dtype='int16', latency='low', channels=1, blocksize=1) as stream:
        while True:
            read_available = stream.read_available

            # capture samples from stream
            data, _ = stream.read(read_available)

            # push samples to queue
            samples.append(data)

            if read_samples > delay_samples:
                # write samples to stream
                stream.write(samples.pop(0))
            else:
                # fill with zeros to avoid underrun errors
                stream.write(np.zeros((100, 1), dtype=np.int16))

                # increase the counter of samples read
                read_samples += read_available

except KeyboardInterrupt:
    pass

print('end')
