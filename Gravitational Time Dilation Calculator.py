import numpy as np
import astropy
import astropy.units as u
from astropy.constants import M_earth
from astropy.constants import c, G

# Welcome messages and guide
print("Welcome to the Time Dilation Calculator!")


# Mass input
mass = float(input("What is the mass of the object? (input value in kg) "))
distance = float(input("What is the distance from the object? (input value in km) "))

# Earth time dilation factor for comparison
earth_dilation_factor = np.sqrt(1-((2*G.to_value()*M_earth.to_value())/(6371*1000*(c.to_value()**2))))

# Object time dilation
object_dilation_factor = np.sqrt(1-((2*G.to_value()*mass)/(distance*1000*(c.to_value()**2))))

# Earth_Time
earth_time = float(input("How many seconds have elapsed for an observer on Earth? "))

# Relative adjustments
relative_factor = object_dilation_factor / earth_dilation_factor
object_time_from_earth_reference = earth_time * relative_factor

# Time Comparisons and Output Message
print("For",earth_time,"second(s) on Earth,",object_time_from_earth_reference,"seconds passes near the object")



