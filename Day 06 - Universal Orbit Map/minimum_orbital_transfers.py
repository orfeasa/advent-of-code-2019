input_file = "input.txt"


planets = {}
"""
planets are stored in a dictionary, in the  the format "PL1" : "PL2",
which means PL2 orbits around PL1. The central planet orbits around
nothing, so for this case the value would be "COM": None.
"""
planets = {}
with open(input_file) as f:
    for line in f.readlines():
        orbit_pair = line.strip().split(")")
        planets.setdefault(orbit_pair[0], None)
        planets[orbit_pair[1]] = orbit_pair[0]


def find_path_to_COM_from(planet):
    while planets[planet] is not None:
        val = []
        val += find_path_to_COM_from(planets[planet])
        val.append(planet)
        return val
    return [planet]


# to calculate the transfers from YOU to SAN, we calculate the path
# of each one to the center COM, and then remove the common part of
# the paths
path_from_YOU_to_COM = find_path_to_COM_from("YOU")
path_from_SAN_to_COM = find_path_to_COM_from("SAN")
common_path = []
for item in range(min(len(path_from_YOU_to_COM), len(path_from_SAN_to_COM))):
    if path_from_YOU_to_COM[item] == path_from_SAN_to_COM[item]:
        common_path.append(path_from_SAN_to_COM[item])

result = (len(path_from_YOU_to_COM) - len(common_path) - 1) + (
    len(path_from_SAN_to_COM) - len(common_path) - 1
)

print(result)
