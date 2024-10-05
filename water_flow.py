# Copyright 2024, Thalyta Gouveia Ferreira Ashcraft. All rights reserved.

import math

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    water_density = 998.2  # kg/m^3
    pressure_loss = -0.04 * water_density * fluid_velocity**2 * quantity_fittings / 2000
    return pressure_loss

def reynolds_number(hydraulic_diameter, fluid_velocity):
    # Values preset
    water_density = 998.2  # kg/m^3
    dynamic_viscosity = 0.0010016
    # Formula for calculating the Reynolds number:
    r_number = (water_density * hydraulic_diameter * fluid_velocity) / dynamic_viscosity
    return r_number

# def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
#     water_density = 998.2  # kg/m^3
#     k = 0.1 + (50 * reynolds_number * (larger_diameter / smaller_diameter)**4 - 1)
#     pressure_loss = -k * water_density * fluid_velocity**2 / 2000
#     return pressure_loss

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    water_density = 998.2  # kg/m^3
    # Ajuste na fórmula para k
    k = (0.1 + 50 * reynolds_number) * (((larger_diameter / smaller_diameter)**4 - 1))      
    pressure_loss = -k * water_density * fluid_velocity**2 / 2000 
    return pressure_loss

def pressure_loss_from_pipe(diameter, length, friction_factor, fluid_velocity):
    water_density = 998.2  # kg/m^3
    pressure_loss = (friction_factor * length * water_density * fluid_velocity**2) / (2 * diameter * 2000)
    return pressure_loss

def water_column_height(tower_height, tank_height):
    
    return tower_height - tank_height

def pressure_gain_from_water_height(water_height):
    
    water_density = 998.2  # kg/m^3
    gravity_acceleration = 9.81  # m/s²
    pressure_gain = (water_density * gravity_acceleration * water_height) / 1000  # Convertendo para kilopascals
    return pressure_gain

PVC_SCHED80_INNER_DIAMETER = 0.28687  # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013    # (unitless)
SUPPLY_VELOCITY = 1.65                  # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692    # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018      # (unitless)
HOUSEHOLD_VELOCITY = 1.75               # (meters / second)

def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)

    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY

    reynolds = reynolds_number(diameter, velocity)

    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY

    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")

if __name__ == "__main__":
    main()
