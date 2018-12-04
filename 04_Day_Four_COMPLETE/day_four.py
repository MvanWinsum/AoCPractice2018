import pprint, operator, dateutil.parser, datetime

guard_list = {}
def preprocess_datetime(line):
    parsed_date = dateutil.parser.parse(line[0])
    if parsed_date.hour == 23:
        parsed_date = parsed_date.replace(hour=0)
        parsed_date = parsed_date + datetime.timedelta(days=1)
    else:
        parsed_date = parsed_date.replace(hour=1)

    return [parsed_date.strftime("%Y-%m-%d"), parsed_date.strftime("%H:%M")]


def create_sorted_date_action_list():
    for datetime_line in dp_prep_ordered:
        date_time = preprocess_datetime(datetime_line)
        if not date_time[0] in dp_prep_ord_by_day:
            dp_prep_ord_by_day[date_time[0]] = []
        dp_prep_ord_by_day[date_time[0]].append([date_time[1], datetime_line[1]])


def parse_guard_shift_start(event_words):
    global guard_list
    if not event_words[1] in guard_list:
        guard_list[event_words[1]] = {}


def add_up_sleepy_minutes(guard_on_duty, fell_asleep, woke_up):
    global guard_list
    for index, time in enumerate(woke_up):
        if fell_asleep[index] in fell_asleep:
            for slept_minute in range(int(fell_asleep[index]), int(time)):
                guard_list[guard_on_duty][slept_minute] = guard_list[guard_on_duty].get(slept_minute, 0) + 1


def parse_day(date_entries):
    guard_on_duty = 0
    fell_asleep = []
    woke_up = []
    for entry in date_entries:
        event_words = entry[1].strip().split(" ")
        if len(event_words) == 4:
            parse_guard_shift_start(event_words)
            guard_on_duty = event_words[1]
            continue
        if len(event_words) == 2:
            if event_words[0] == 'falls':
                time = entry[0].strip().split(":")[1]
                fell_asleep.append(time)
            if event_words[0] == 'wakes':
                time = entry[0].strip().split(":")[1]
                woke_up.append(time)
            continue
    if guard_on_duty > 0:
        add_up_sleepy_minutes(guard_on_duty, fell_asleep, woke_up)


def filter_most_frequent_minute(guard_list):
    for guardID, minuteData in guard_list.iteritems():
        highest_minute = 0
        most_times_asleep = 0
        for minute, timesAsleep in minuteData.iteritems():
            if timesAsleep > most_times_asleep:
                highest_minute = minute
                most_times_asleep = timesAsleep
        guard_list[guardID] = [highest_minute, most_times_asleep]
    return guard_list


dp_prep = []
pp = pprint.PrettyPrinter(indent=4)
with open('puzzle_input.txt') as input_file:
    for input_line in input_file:
        input_line_prepared = input_line.strip().replace('[', '')
        input_line_split = input_line_prepared.split(']')
        dp_prep.append(input_line_split)

dp_prep_ordered = sorted(dp_prep, key=operator.itemgetter(0))

dp_prep_ord_by_day = {}
create_sorted_date_action_list()
for date, entries in dp_prep_ord_by_day.iteritems():
    parse_day(entries)


guard_list = filter_most_frequent_minute(guard_list)


pp.pprint(guard_list)