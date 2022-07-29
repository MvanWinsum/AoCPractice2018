# Sections needed -> One: 2 segments    Four: 4 segments    Seven: 3 segments   Eight: 7 segments
import string

with open('puzzle_input.txt') as input_file:
    instruction_list = [input_line.strip().split(' | ') for input_line in input_file]
    instruction_list = [[line[0].split(' '), line[1].split(' ')] for line in instruction_list]


numbers_to_segments = {
    0: [0, 1, 2, 4, 5, 6],
    1: [2, 5],
    2: [0, 2, 3, 4, 6],
    3: [0, 2, 3, 5, 6],
    4: [1, 2, 3, 5],
    5: [0, 1, 3, 5, 6],
    6: [0, 1, 3, 4, 5, 6],
    7: [0, 2, 5],
    8: [0, 1, 2, 3, 4, 5, 6],
    9: [0, 1, 2, 3, 5, 6]
}


def parse_two_segments(line, translation_map):
    for segment in line:
        if len(segment) != 2:
            continue
        else:
            translation_map['letter'][segment[0]] = 2
            translation_map['letter'][segment[1]] = 5
            translation_map['number'][2] = segment[0]
            translation_map['number'][5] =segment[1]
    return translation_map


def parse_three_segments(line,translation_map):
    for segment in line:
        if len(segment) != 3:
            continue
        else:
            for letter in segment:
                if translation_map['letter'][letter] == -1:
                    translation_map['letter'][letter] = 0
                    translation_map['number'][0] = letter
                    break
    return translation_map


def parse_four_segments(line,translation_map):
    new_letter_index = 0
    new_letter_positions = [1,3]
    for segment in line:
        if len(segment) != 4:
            continue
        else:
            for letter in segment:
                if translation_map['letter'][letter] == -1:
                    translation_map['letter'][letter] = new_letter_positions[new_letter_index]
                    translation_map['number'][new_letter_positions[new_letter_index]] = letter
                    new_letter_index += 1
    return translation_map


def parse_five_segments(line, translation_map):
    known_letters = ''.join(translation_map['number'].values())
    three_segment = ''
    two_segment = ''
    print(line)
    for segment in line:
        if len(segment) != 5:
            continue
        else:
            if not translation_map['number'][5] in segment:
                # It's a two
                print(f'Two: {segment}')
                two_segment = segment
            elif translation_map['number'][2] in segment and translation_map['number'][5] in segment:
                # It's a three
                print(f'Three: {segment}')
                three_segment = segment
    three_letter = ''.join(filter(lambda x: x not in known_letters, three_segment))
    if len(three_letter) == 1:
        translation_map['letter'][three_letter] = 6
        translation_map['number'][6] = three_letter
        known_letters += three_letter
    two_letter = ''.join(filter(lambda x: x not in known_letters, two_segment))
    if len(two_letter) == 1:
        print(f'Three: {two_letter}')
        translation_map['letter'][two_letter] = 4
        translation_map['number'][4] = two_letter
    return translation_map


def find_last_letter(translation_map):
    for key, value in translation_map['letter'].items():
        if value == -1:
            translation_map['letter'][key] = 4
            translation_map['number'][4] = key
    return translation_map


for segment_line in instruction_list:
    translation = {
        'letter': {letter:-1 for letter in 'abcdefg'},
        'number': {number:'' for number in range(7)}
    }
    translation = parse_two_segments(segment_line[0], translation)
    translation = parse_three_segments(segment_line[0], translation)
    translation = parse_four_segments(segment_line[0], translation)
    translation = parse_five_segments(segment_line[0], translation)
    translation = find_last_letter(translation)
    line_number = ''
    for signal in segment_line[1]:
        signal_numbers = []
        for letter in signal:
            signal_numbers.append(translation['letter'][letter])
        signal_numbers.sort()
        print(f'letters: {signal} signals: {signal_numbers}')
        for key, value in numbers_to_segments.items():
            if signal_numbers == value:
                line_number += str(key)
    print(f"Output: {segment_line[1]} \n line_number: {line_number} \n Translation: {translation}")
