import pprint
pp = pprint.PrettyPrinter(indent=4)
num_players = 404
player_list = {}
current_player = 0
highest_pebble = 71852
pebble_list = [0]
current_pebble = 0


def move_along_list(steps):
    global current_pebble
    current_pebble += steps
    current_pebble = current_pebble % len(pebble_list)


def prepare_player_list():
    global num_players, player_list
    for player in range(0, num_players):
        player_list[player] = 0


def get_next_player():
    global current_player, num_players
    current_player += 1
    if current_player > num_players:
        current_player = 0


def score_points(new_pebble):
    player_list[current_player] += new_pebble
    move_along_list(-7)
    player_list[current_player] += pebble_list[current_pebble]
    del pebble_list[current_pebble]
    pass


def add_pebble_to_list(pebble):
    global current_pebble
    move_along_list(2)
    pebble_list.insert(current_pebble, pebble)


def next_player():
    global current_player
    current_player += 1
    if current_player > (num_players - 1):
        current_player = 0


def play_game():
    for new_pebble in range(1, highest_pebble + 1):
        if new_pebble % 23 == 0:
            score_points(new_pebble)
        else:
            add_pebble_to_list(new_pebble)
        next_player()


def get_highest_score():
    highest_score = 0
    for player, score in player_list.iteritems():
        if score > highest_score:
            highest_score = score
    return highest_score

# Main Script Functionality
prepare_player_list()
play_game()
pp.pprint(player_list)
pp.pprint(get_highest_score())