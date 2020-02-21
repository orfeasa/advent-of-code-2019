input_file = "input.txt"


def calculate_height(planet):
    while planets[planet] != None:
        return calculate_height(planets[planet]) + 1
    return 0


planets = {}
"""
planets are stored in a dictionary, in the  the format "PL1" : "PL2", 
which means PL2 orbits around PL1. The central planet orbits around
nothing, so for this case the value would be "COM": None.
"""
with open(input_file) as f:
    for line in f.readlines():
        orbit_pair = line.strip().split(")")
        planets.setdefault(orbit_pair[0], None)
        planets[orbit_pair[1]] = orbit_pair[0]

total_orbits = 0
for planet in planets.keys():
    total_orbits += calculate_height(planet)

print(total_orbits)
