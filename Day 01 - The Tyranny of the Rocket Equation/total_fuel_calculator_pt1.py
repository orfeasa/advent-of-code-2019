import math

input_file = "input.txt"


def calc_fuel_for_mass(moduleMass: int) -> float:
    return math.floor(moduleMass / 3) - 2


totalFuel = 0
with open(input_file) as f:
    for line in f.readlines():
        totalFuel += calc_fuel_for_mass(int(line.strip()))

print(f"Total fuel: {totalFuel}")
