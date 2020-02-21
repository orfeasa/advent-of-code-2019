import re

input_lines = """<x=3, y=3, z=0>
<x=4, y=-16, z=2>
<x=-10, y=-6, z=5>
<x=-3, y=0, z=-13>"""

no_of_steps = 1000

input_regex = re.compile(r"<x=(.*), y=(.*), z=(.*)>")

regex_res = input_regex.findall(input_lines)

# pos = [[x1, y1, z1], [x2, y2, z2], ...]
pos = [[int(x), int(y), int(z)] for (x, y, z) in regex_res]
no_of_moons = len(pos)

# vel = [[vx1, vy1, vz1], [vx2, vy2, vz2], ...]
vel = [[0, 0, 0] for i in range(no_of_moons)]
# pot, kin, total = [pot1, pot2, ...]
pot = [0 for i in range(no_of_moons)]
kin = [0 for i in range(no_of_moons)]
total_energy = [0 for i in range(no_of_moons)]


total_system_energy = 0
# iterate through time steps
for step in range(no_of_steps):
    # update velocity by applying gravity
    # for every pair
    for moon1 in range(no_of_moons):
        for moon2 in range(moon1 + 1, no_of_moons):
            for coord in range(3):
                # change each coordinate for each axis by +1 or -1 to bring them closer together
                if pos[moon1][coord] > pos[moon2][coord]:
                    vel[moon1][coord] -= 1
                    vel[moon2][coord] += 1
                elif pos[moon1][coord] < pos[moon2][coord]:
                    vel[moon1][coord] += 1
                    vel[moon2][coord] -= 1
                else:
                    pass

    # update position by applying velocity
    # for each moon
    for moon in range(no_of_moons):
        # position += velocity
        for coord in range(3):
            pos[moon][coord] += vel[moon][coord]

    # calculate potential energy
    # sum of abs values of position coordinates
    for moon in range(no_of_moons):
        pot[moon] = 0
        for coord in range(3):
            pot[moon] += sum([abs(pos[moon][coord])])

    # calculate kinetic energy
    # kinetic energy is the sum of abs values of velocity coordinates
    for moon in range(no_of_moons):
        kin[moon] = 0
        for coord in range(3):
            kin[moon] += sum([abs(vel[moon][coord])])

    # total energy = potential * kinetic
    for moon in range(no_of_moons):
        total_energy[moon] = pot[moon] * kin[moon]

    # total energy of the sytem is the sum of the total energy of all particles
    total_system_energy = sum(total_energy)

print(total_system_energy)
