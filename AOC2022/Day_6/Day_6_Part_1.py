with open('puzzle_input.txt') as input_file:
    data_stream = [list(line.strip()) for line in input_file][0]
    print(data_stream)


required_distincts = 4
stream_index = required_distincts

while stream_index <= len(data_stream):
    stream_characters = data_stream[stream_index-required_distincts:stream_index]
    if len(stream_characters) == len(set(stream_characters)):
        print(stream_index)
        break
    else:
        stream_index += 1
