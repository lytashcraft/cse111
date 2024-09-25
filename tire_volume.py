import math 
from datetime import datetime

#Thalyta Gouveia Ferreira, CSE111 class

#User input the values
tire_width = (input('Enter the width of the tire in mm (ex: 205): '))

tire_ratio = (input('Enter the aspect ratio of the tire (ex: 60): '))

tire_diameter = (input('Enter the diameter of the wheel in inches (ex: 15): '))

#convertion to str to float
tire_width = float(tire_width)
tire_ratio = float(tire_ratio)
tire_diameter = float(tire_diameter)

#the volume formula
volume = math.pi * tire_width**2 * tire_ratio * (tire_width * tire_ratio + 2540 * tire_diameter) / 10000000000

#the function returns the current date
current_date = datetime.now().date()

#the function prints the approximate volume and current date
print(f'The appoximate volume is {volume:.2f} liters. Date: {current_date}')

with open ('volumes.txt', 'a') as tires:
    tires.write(f'Tire Width: {tire_width}, Tire Ratio: {tire_ratio}, Tire Diameter: {tire_diameter}, witch the approximate volume is {volume:.2f} liters. Date: {current_date}')