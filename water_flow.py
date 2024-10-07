# Copyright 2024, Thalyta Gouveia Ferreira Ashcraft. All rights reserved.

import math

def water_column_height(tower_height, tank_height):
    h = tower_height + (3/4) * tank_height

    return h

def pressure_gain_from_water_height(height):
    water_density = 998.2  # kg/m^3
    gravity = 9.80665      # m/s²
    
    pressure = (water_density * gravity * height) / 1000
    return pressure

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    water_density = 998.2  # kg/m³

    pressure_loss = - (friction_factor * pipe_length * water_density * fluid_velocity**2) / (2000 * pipe_diameter)
    return pressure_loss