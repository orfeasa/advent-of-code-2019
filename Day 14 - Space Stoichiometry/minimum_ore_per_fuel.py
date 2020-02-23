import math

input_fileName = "input.txt"


def read_input(input_fileName):
    reactions = {}
    input_file = open(input_fileName, "r")

    for line in input_file.readlines():
        # Read the reactions
        reaction = line.split("=>")

        react_input_string = reaction[0].strip().split(", ")
        react_input = []
        for elem in range(len(react_input_string)):
            input_pair = react_input_string[elem].split(" ")
            react_input.append((int(input_pair[0]), input_pair[1]))

        output_pair = reaction[1].strip().split(" ")
        react_output = (int(output_pair[0]), output_pair[1])

        reactions[react_output[1]] = (react_output[0], react_input)
    input_file.close()
    return reactions


def create_levels(reactions):
    # create "layer" dictionary
    chemicals_levels = {"ORE": 0}
    # for every element there is
    for _ in reactions.keys():

        # for every reaction
        for react_key in reactions.keys():
            # populate list of input elements in the reaction that react_key produces
            input_element_list = [
                reactions[react_key][1][i][1]
                for i in range(len(reactions[react_key][1]))
            ]

            # if the reaction input only contains elements that are
            # keys in the dictionary chemicals_levels
            if set(input_element_list).issubset(chemicals_levels.keys()):
                # set the level of the elemnt produced as the max of the
                # input elements +1
                max_level = 0
                for i in range(len(input_element_list)):
                    if chemicals_levels[input_element_list[i]] > max_level:
                        max_level = chemicals_levels[input_element_list[i]]

                chemicals_levels[react_key] = max_level + 1

    # sort levels by value descending
    chemicals_levels = {
        k: v for k, v in sorted(chemicals_levels.items(), key=lambda item: item[1])
    }
    return chemicals_levels


def ore_for_1_fuel(reactions):
    # assign level to each chemical
    chemicals_levels = create_levels(reactions)

    # while input does not only contain ORE
    wasted_material = {}
    # initialize with desired output
    input_required = {"FUEL": 1}
    contains_only_ore = False
    while contains_only_ore is False:
        max_level = max(chemicals_levels.values())

        # for each layer of priority, starting from the greatest

        for level in range(max_level, 0, -1):
            # list of chemicals left with this priority
            chemicals_left = [
                chem
                for chem in list(input_required.keys())
                if chemicals_levels[chem] == level
            ]

            for chemical in chemicals_left:
                # for each item that is not ORE yet
                if chemical != "ORE" and input_required[chemical] > 0:

                    # calculate how many times to run the recipe:
                    times_to_run = math.ceil(
                        input_required[chemical] / reactions[chemical][0]
                    )
                    no_of_resulting_chemicals = reactions[chemical][0] * times_to_run

                    # add the elements that are needed as input in the reaction
                    for quant, elem in reactions[chemical][1]:
                        input_required.setdefault(elem, 0)
                        input_required[elem] += quant * times_to_run

                    # remove the output of the reaction from the dictionary
                    if input_required[chemical] >= no_of_resulting_chemicals:
                        input_required[chemical] -= no_of_resulting_chemicals
                    else:
                        input_required[chemical] = 0
                        wasted_material[chemical] = (
                            no_of_resulting_chemicals - input_required[chemical]
                        )

                    if input_required[chemical] == 0:
                        del input_required[chemical]

            contains_only_ore = True
            for key in input_required.keys():
                if key != "ORE" and input_required[key] != 0:
                    contains_only_ore = False
                    break

    return input_required["ORE"], wasted_material


ore_required, wasted_material = ore_for_1_fuel(read_input(input_fileName))
print(ore_required)
