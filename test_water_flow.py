import pytest
from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe

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
        assert abs(result - expected) < 0.001

def test_pressure_gain_from_water_height():
    #the test values
    test_values = [
        (0.0, 0.000),
        (30.2, 295.628),
        (50.0, 489.450)
    ]

    for height, expected in test_values:
        result = pressure_gain_from_water_height(height)
        
        assert abs(result - expected) < 0.001

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
        
        assert abs(result - expected) < 0.001

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])