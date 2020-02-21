import math

input_file = "input.txt"


def calc_fuel_for_mass_and_fuel(moduleMass):
    total_fuel = 0
    next_fuel = math.floor(moduleMass / 3) - 2
    while next_fuel > 0:
        total_fuel += next_fuel
        next_fuel = math.floor(next_fuel / 3) - 2
    return total_fuel


total_fuel = 0
with open(input_file) as f:
    for line in f.readlines():
        total_fuel += calc_fuel_for_mass_and_fuel(int(line.strip()))

print(f"Total fuel including fuel fuel: {total_fuel}")
