import numpy as np
from astropy.constants import G

# Function for T
def Ask_T():
    return float(input("What is the period of the orbit? (input in seconds) "))

def Ask_a():
    return float(input("What is the semi-major axis of the orbit? (input in meters) "))

def Ask_M():
    return float(input("What is the Mass of the first object? (input in kg) "))

def Ask_m():
    return float(input("What is the Mass of the second object? (input in kg) "))

# Converting G to value without units
G = G.to_value()

# Welcome Messages and Guide
print("Welcome to the Kepler's Third Law Calculator!")

# Asking for which Variable to Solve For
missing_variable = input("In the general physics equation for Kepler's Third Law, which variable do you want to solve for? This includes variables T (time in seconds), a (semi-major axis in meters), M (first mass in kg), and m (second mass in kg) ")

# If and elif statement for 
if missing_variable.lower() in ['t']:
    a = Ask_a()
    M = Ask_M()
    m = Ask_m()
    T = np.sqrt((4*(np.pi**2)*(a**3))/(G*(M+m)))
    print ("T =",T,)
elif missing_variable.lower() in ['a']:
    T = Ask_T()
    M = Ask_M()
    m = Ask_m()
    a = np.cbrt((G*(M+m)*(T**2))/(4*(np.pi**2)))
    print("a =",a,"m")
elif missing_variable in ['M']:
    T = Ask_T()
    a = Ask_a()
    m = Ask_m()
    M = (4*(np.pi**2)*(a**3))/(G*(T**2))-m
    print("M =",M,"kg")
elif missing_variable in ['m']:
    T = Ask_T()
    a = Ask_a()
    M = Ask_M()
    m = (4*(np.pi**2)*(a**3))/(G*(T**2))-M
    print("m =",m,"kg")
else:
    print("Error with missing variable input. Please have a valid input other than",missing_variable)