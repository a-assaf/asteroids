import math
import matplotlib.pyplot as plt

photons = float(input("What is total number of photons (signal)? "))
pixels = float(input("What is the number of pixels? "))
sky = float(input("What is the total number of photons per pixel from the background or sky? "))
darke = 0
#darke = float(input("What is the total number of dark current electrons per pixel? "))
#reade = float(input("What is the total number of electrons per pixel resulting from the read noise? "))
reade = 8.2   
#equation for the S/N of a measurement made with a CCD

ratio = photons / math.sqrt(photons + pixels*(sky + darke + (reade**2)))
print('The SNR is: ', ratio)



