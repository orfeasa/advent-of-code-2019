import copy
import math
import re

input_lines = """<x=3, y=3, z=0>
<x=4, y=-16, z=2>
<x=-10, y=-6, z=5>
<x=-3, y=0, z=-13>"""


def print_status(steps, vel, pos):
    print(f"After {steps} steps:")
    for moon in range(len(pos)):
        print(f"pos: = {pos[moon]}, vel: {vel[moon]}")
    print("")


def calc_next_state(vel, pos):
    # update velocity by applying gravity
    for moon1 in range(no_of_moons):
        for moon2 in range(moon1 + 1, no_of_moons):
            for coord in range(3):
                # change each coordinate for each axis by +1 or -1 to bring
                # them closer together
                if pos[moon1][coord] > pos[moon2][coord]:
                    vel[moon1][coord] -= 1
                    vel[moon2][coord] += 1
                elif pos[moon1][coord] < pos[moon2][coord]:
                    vel[moon1][coord] += 1
                    vel[moon2][coord] -= 1
                else:
                    pass

    # update position by applying velocity
    for moon in range(no_of_moons):
        # position += velocity
        for coord in range(3):
            pos[moon][coord] += vel[moon][coord]

    return vel, pos


# initialize values
input_regex = re.compile(r"<x=(.*), y=(.*), z=(.*)>")
regex_res = input_regex.findall(input_lines)

pos0 = [[int(x), int(y), int(z)] for (x, y, z) in regex_res]
pos = copy.deepcopy(pos0)
no_of_moons = len(pos)

# vel = [[vx1, vy1, vz1], [vx2, vy2, vz2], ...]
vel0 = [[0, 0, 0] for i in range(no_of_moons)]
vel = copy.deepcopy(vel0)
curr_step = 0

periods_per_axis = [None, None, None]
coords_left = list(range(3))

# each axis is independant from the others
# we calucalte the period of each dimention separately
while None in periods_per_axis:
    vel, pos = calc_next_state(vel, pos)
    curr_step += 1

    for coord in coords_left:
        found = True
        for moon in range(no_of_moons):
            if (pos[moon][coord] != pos0[moon][coord]) or (
                vel[moon][coord] != vel0[moon][coord]
            ):
                found = False
                break
        if found:
            periods_per_axis[coord] = curr_step
            coords_left.remove(coord)

# find lcm
lcm = periods_per_axis[0]
for i in periods_per_axis[1:]:
    lcm = int(lcm * i / math.gcd(lcm, i))

print(f"periods per axis: {periods_per_axis}")
print(f"result: {lcm}")
