import numpy as np

# Object Radius (duh)
object_radius = float(input("What is the radius of the object? (input value in meters) "))

# Rotational Period
rotation_period = float(input("How fast is the object rotating? (input value in rotations/s) "))

# Convert Radius into Circumference
circumference = 2*object_radius*np.pi

# Linear Velocity Equation (Convert Rotational Period to Linear Velocity)
linear_velocity = circumference*rotation_period

print("The object's linear velocity is",linear_velocity,"m/s")

