# Dependencias
El programa fue desarrollado y probado utilizando Ubuntu version 22.04.1 
El programa depende de python en su version 3.10.4 y paquetes instalados de apt:
    - python3-numpy (1.21.5-1build2)
    - libportaudio2 (19.6.0-1.1)

Adicionalmente de pip:
    - sounddevice: python3 -m pip install sounddevice


# Instrucciones

## Problema 1
`python3 prob1.py <Delay D en ms>` p.ej: `python3 prob1.py 500` 
El programa retrasara la entrada del microfono en 500 ms

## Problema 3
`python3 prob3.py` 
El programa generara un tono de 440 Hz, lo reproduce y lo grafica