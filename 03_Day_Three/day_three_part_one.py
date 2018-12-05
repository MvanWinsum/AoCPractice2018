import pprint

pp = pprint.PrettyPrinter(indent=4)
coordinates = {}

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


def get_multi_claimed_inches():
    multi_claimed_inches = 0
    for inch in coordinates.iteritems():
        if len(inch[1]) > 1:
            multi_claimed_inches += 1
    return multi_claimed_inches


# Main Script Functionality
fill_sheet_matrices()
parse_claims_onto_sheet(claim_inputs)
multi_claimed = get_multi_claimed_inches()
pp.pprint(multi_claimed)

