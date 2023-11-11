from models.intervals import IntervalSet, Interval

# Transform from [{"start": 10, "end": 19}, {"start": 31, "end": 100}] to [(10, 19), (31, 100)]
def transform_to_list_of_tuples(input_list):
    output_list = []

    for interval in input_list:
        if interval.start is not None and interval.end is not None:
            output_list.append((interval.start, interval.end))

    return output_list


# Transform from [(10, 19), (31, 100)] to [{"start": 10, "end": 19}, {"start": 31, "end": 100}]
def transform_to_list_of_dicts(input_list):
    output_list = []

    for item in input_list:
        if isinstance(item, tuple):
            output_list.append({'start': item[0], 'end': item[1]})

    return output_list