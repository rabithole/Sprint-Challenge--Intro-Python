# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
# Base class
class Vehicle:
	pass

# Base class
class FlightVehicle:
	pass

# Base class
class Starship():
	pass 

# Vehicle
class GroundVehicle(Vehicle):
	pass

# GroundVehicle
class Car(GroundVehicle):
	pass

# GroundVehicle
class Motorcycle(GroundVehicle):
	pass

# FlightVehicle
class Airplane(FlightVehicle):
	pass

