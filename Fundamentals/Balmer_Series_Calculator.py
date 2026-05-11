import numpy as np
def ordinal_suffix(n):
    # Copied from the internet (i kinda forgot where lol sorry)
    # Handle negative numbers if necessary, the logic assumes non-negative integers
    if n < 0:
        raise ValueError("Ordinal numbers must be non-negative")
    
    # Special case for numbers ending in 11, 12, or 13 (e.g., 11th, 112th)
    if n % 100 in [11, 12, 13]:
        suffix = 'th'
    # General cases for numbers ending in 1, 2, or 3
    elif n % 10 == 1:
        suffix = 'st'
    elif n % 10 == 2:
        suffix = 'nd'
    elif n % 10 == 3:
        suffix = 'rd'
    # All other numbers get 'th' (e.g., 4th, 5th, 20th)
    else:
        suffix = 'th'
    
    return f"{n}{suffix}"
while True:
    n1 = int(input("Input n1: "))   # Initial Energy Level
    n2 = int(2)                     # Final Energy Level
    R = 1.0986 * 10**7              # Rydberg Constant
    b = R *((1/n2**2) - (1/n1**2))  # Equation for wavelength of hydrogen emission and absorption lines
    c = 1/b                         # Reciprocal to give us wavelength
    a = c*(10**9)                   # Conversion to nanometers
    print("The wavelength of the",ordinal_suffix(n1-2),"balmer series is",a,"nanometers")
    decision = input("do you want to continue? ")
    if decision == "yes":
        continue
    else: break
        
