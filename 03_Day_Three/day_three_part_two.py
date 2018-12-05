import pprint

pp = pprint.PrettyPrinter(indent=4)
coordinates = {}
claimants_and_conflicts = {}

with open('puzzle_input.txt') as input_file:
    claim_inputs = [input_line.strip() for input_line in input_file]


def fill_sheet_matrices():
    for w_index in range(0, 1000):
        for h_index in range(0, 1000):
            coordinate = str(w_index) + ',' + str(h_index)
            coordinates[coordinate] = []


def stake_claims(claimant, offset_width, offset_height, width, height):
    for w_index in range(0, int(width)):
        for h_index in range(0, int(height)):
            coordinate = str(int(offset_width) + int(w_index)) + ',' + str(int(offset_height) + int(h_index))
            coordinates[coordinate].append(claimant)


# Returns the important values from the input string
def split_input_string_to_values(claim_input_line):
    # #1236 @ 123,901: 14x25 <-- #1236 | 123,901: 14x25
    claim_id_split = claim_input_line.split(' @ ')
    claimant = claim_id_split[0]
    # 123,901: 14x25 <-- 123 | 901: 14x25
    offset_width_split = claim_id_split[1].split(',')
    offset_width = offset_width_split[0]
    # 901: 14x25 <-- 901 | 14x25
    offset_height_split = offset_width_split[1].split(': ')
    offset_height = offset_height_split[0]
    # 14x25 <-- 14 | 25
    dimensions_split = offset_height_split[1].split('x')
    width = dimensions_split[0]
    height = dimensions_split[1]

    return [claimant, offset_width, offset_height, width, height]


def parse_claims_onto_sheet(claims):
    for claim in claims:
        claim_parameters = split_input_string_to_values(claim)
        stake_claims(
            claim_parameters[0],  # Claimant
            claim_parameters[1],  # Offset Width
            claim_parameters[2],  # Offset Height
            claim_parameters[3],  # Width
            claim_parameters[4],  # Height
        )


def get_lonely_claims():
    for inch in coordinates.iteritems():
        for claim_to_inch in inch[1]:
            claimants_and_conflicts[claim_to_inch] = claimants_and_conflicts.get(claim_to_inch,0) + (len(inch[1]) - 1)
    for claimant, conflicts in claimants_and_conflicts.iteritems():
        if int(conflicts) == 0:
            pp.pprint(claimant + ' <--------- THIS IS THE CLAIMANT')
            return


# Main Script Functionality
fill_sheet_matrices()
parse_claims_onto_sheet(claim_inputs)
get_lonely_claims()

