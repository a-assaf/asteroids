# asteroids
Physical characterization of Near Earth Objects
Co-worked with Zach Quinn & Wenting Zhang, supervised by Researcher Dr. Ries.

Attempting to derive refined absolute magnitudes, rotational periods, and if possible, axis ratios for Potentially Hazardous Asteroids (PHAs).
We extract from the catalog stars which bracket the estimated magnitude of the target and remove those pairs of stars from the file which are closer than ~20 arcseconds, reducing possible sky contamination in the automated photometry.
To test the robustness of our reduction, we compare the lightcurves using different photometric parameters, reference star editing and catalog based R magnitude determination.

EllipticalOrbitVersion2:
User will be prompted to enter the semi major axis, the eccentricity, the amount of iterations, and the value of mu. The program computes and outputs the value of n and the period, and then plots the time by the radius.

SNR Program:
User will be prompted to enter the total number of photons (signal) of the image being analyzed. Then the user will be asked for the number of pixels and the total number of photons per pixel from the background. The program computes and outputs the Signal-to-Noise ratio.

Background Star Analysis Program:
Not yet uploaded.

Smoothing Program:
Not yet uploaded.
