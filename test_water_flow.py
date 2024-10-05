from water_flow import pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction
import pytest

def test_pressure_loss_from_fittings():
    # Defining the test values
    tests_values = [
        (0.00, 3, 0.000),
        (1.65, 0, 0.000),
        (1.65, 2, -0.109), 
        (1.75, 2, -0.122),    
        (1.75, 5, -0.306)
    ]
    
    for fluid_velocity, quantity_fittings, expected in tests_values:
        result = pressure_loss_from_fittings(fluid_velocity, quantity_fittings)
        assert abs(result - expected) < 0.001   # Tolerance of 0.001
        

def test_reynolds_number():
    # Defining the test values
    test_values = [
        (0.048692, 0.00, 0),
        (0.048692, 1.65, 80069),
        (0.048692, 1.75, 84922),
        (0.286870, 1.65, 471729),
        (0.286870, 1.75, 500318)
    ]
    
   
    for hydraulic_diameter, fluid_velocity, expected in test_values:
        
        result = reynolds_number(hydraulic_diameter, fluid_velocity)
        
        assert abs(result - expected) < 1 # Tolerance of 1


def test_pressure_loss_from_pipe_reduction():
    # Defining the test values
    test_values = [
        (0.28687, 0.00, 1, 0.048692, 0.000),
        (0.28687, 1.65, 471729, 0.048692, -163.744),
        (0.28687, 1.75, 500318, 0.048692, -184.182)
    ]
    
    for larger_diameter, fluid_velocity, reynolds_number, smaller_diameter, expected in test_values:
        
        result = pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter)
        
        assert abs(result - expected) < 0.001  # Tolerance of 0.001