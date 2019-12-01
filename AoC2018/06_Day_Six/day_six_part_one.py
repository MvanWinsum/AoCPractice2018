import pprint
import csv

pp = pprint.PrettyPrinter(indent=4)
claim_list = {}
matrix_width = 0
matrix_height = 0
matrix = {}
claim_areas = {}
index = 0
with open('puzzle_input.txt') as input_file:
    for input_line in input_file:
        claim_list['#' + str(index)] = input_line.strip().split(', ')
        index += 1


def get_edge_claims():
    edge_claims = []
    for claimant, claim in claim_list.iteritems():
        if int(claim[0]) == matrix_width or int(claim[1]) == matrix_height:
            edge_claims.append(claim)
    return edge_claims


def set_matrix_dimensions():
    global matrix_width
    global matrix_height
    for claimant, claim in claim_list.iteritems():
        if int(claim[0]) > matrix_width:
            matrix_width = int(claim[0])
        if int(claim[1]) > matrix_height:
            matrix_height = int(claim[1])


def create_matrix():
    for w_index in range(0, matrix_width):
        for h_index in range(0, matrix_height):
            matrix[str(w_index) + ',' + str(h_index)] = []


def closest_claim(coordinate, distance):
    closer_claims = 0
    for close_claim in coordinate:
        if int(close_claim[1]) < distance:
            closer_claims += 2
        if int(close_claim[1]) == distance:
            closer_claims += 1
    return closer_claims


def calculate_closest_claim_for_points():
    for coordinate, claim_distances in matrix.iteritems():
        split_coordinate = coordinate.split(',')
        for claimant, claim in claim_list.iteritems():
            distance = abs(int(split_coordinate[0]) - int(claim[1])) + abs(int(split_coordinate[1]) - int(claim[1]))
            claim_distance_rank = closest_claim(matrix[coordinate], distance)
            if claim_distance_rank == 0:
                matrix[coordinate] = [[claimant, distance]]
            if claim_distance_rank == 1:
                matrix[coordinate].append([claimant,distance])


def filter_matrix_coordinates(edge_claims):
    filtered_matrix = {}
    for coordinate, closest_claims in matrix.iteritems():
        if len(closest_claims) == 1 and closest_claims[0][0] not in edge_claims:
            filtered_matrix[coordinate] = closest_claims
    return filtered_matrix


def calculate_claim_areas(filter_matrix):
    global claim_areas
    for coordinate, closest_claim in filter_matrix.iteritems():
        coordinate_pair = coordinate.split(',')
        claim_areas[closest_claim[0][0]] = claim_areas.get(closest_claim[0][0], 0) + 1
        if coordinate_pair[0] == (matrix_width - 1) or coordinate_pair[1] == (matrix_height - 1):
            claim_areas[closest_claim[0][0]] = -10000


def convert_to_visualization_data(filter_matrix):
    converted_matrix = []
    for coordinate, details in filter_matrix.iteritems():
        coordinate_pair = coordinate.split(',')
        converted_matrix.append([coordinate_pair[0], coordinate_pair[1], details[0][0]])
    return converted_matrix

# Main Script Functionality
set_matrix_dimensions()
create_matrix()
edge_claims = get_edge_claims()
calculate_closest_claim_for_points()
filter_matrix = filter_matrix_coordinates(edge_claims)
visualization_data = convert_to_visualization_data(filter_matrix)
area_distribution = calculate_claim_areas(filter_matrix)
with open("output.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(visualization_data)
pp.pprint(visualization_data)
