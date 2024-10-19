import pytest
from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe, pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction

def test_water_column_height():
    #the test values
    test_values = [
        (0.0, 0.0, 0.0),
        (0.0, 10.0, 7.5),
        (25.0, 0.0, 25.0),
        (48.3, 12.8, 57.9),
    ]

    for tower_height, tank_height, expected in test_values:
        result = water_column_height(tower_height, tank_height)
        assert abs(result - expected) < 0.001 # Tolerance of 0.001

def test_pressure_gain_from_water_height():
    #the test values
    test_values = [
        (0.0, 0.000),
        (30.2, 295.628),
        (50.0, 489.450)
    ]

    for height, expected in test_values:
        result = pressure_gain_from_water_height(height)
        
        assert abs(result - expected) < 0.001 # Tolerance of 0.001

def test_pressure_loss_from_pipe():
    #the test values
    test_values = [
         (0.048692, 0.00, 0.018, 1.75, 0.000),
         (0.048692, 200.00, 0.000, 1.75, 0.000),
         (0.048692, 200.00, 0.018, 0.00, 0.000),
         (0.048692, 200.00, 0.018, 1.75, -113.008),
         (0.048692, 200.00, 0.018, 1.65, -100.462),
         (0.286870, 1000.00, 0.013, 1.65, -61.576),
         (0.286870, 1800.75, 0.013, 1.65, -110.884)
    ]

    for pipe_diameter, pipe_length, friction_factor, fluid_velocity, expected in test_values:
        result = pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity)
        
        assert abs(result - expected) < 0.001 # Tolerance of 0.001

def test_pressure_loss_from_fittings():
    #the test values
    test_values = [
        (0.00, 3, 0.000),
        (1.65, 0, 0.000),
        (1.65, 2, -0.109),
        (1.75, 2, -0.122),
        (1.75, 5, -0.306)
    ]
    
    for fluid_velocity, quantity_fittings, expected in test_values:
        result = pressure_loss_from_fittings(fluid_velocity, quantity_fittings)
        
        assert abs(result - expected) < 0.001 # Tolerance of 0.001

def test_reynolds_number():
    #the test values
    test_values = [
        (0.048692, 0.00, 0),
        (0.048692, 1.65, 80069),
        (0.048692, 1.75, 84922),
        (0.286870, 1.65, 471729),
        (0.286870, 1.75, 500318)
    ]
    
    for hydraulic_diameter, fluid_velocity, expected in test_values:
        result = reynolds_number(hydraulic_diameter, fluid_velocity)
        
        assert abs(result - expected) < 1

def test_pressure_loss_from_pipe_reduction():

    test_values = [
        (0.28687, 0.00, 1, 0.048692, 0.000),
        (0.28687, 1.65, 471729, 0.048692, -163.744),
        (0.28687, 1.75, 500318, 0.048692, -184.182)
    ]
    
    for larger_diameter, fluid_velocity, reynolds_number, smaller_diameter, expected in test_values:
        result = pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter)
        assert abs(result - expected) < 0.001

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])