import logging

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)


def pairwise(iterator):
    """Return an iterator yielding pairs of each element and the following"""
    i = iter(iterator)
    prev = next(i)
    for item in i:
        yield prev, item
        prev = item


def sonar_filter(previous_and_current_reading):
    """Return True for each pair (a, b) with b > a (plus some debug logging)"""
    prev_reading, curr_reading = previous_and_current_reading
    if curr_reading > prev_reading:
        logging.debug("{0} (increased)".format(curr_reading))
        return True
    else:
        logging.debug("{0} (decreased)".format(curr_reading))
        return False


with open(file="input.txt", mode="r") as input_file:
    # input_file = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    filtered_readings = filter(sonar_filter, pairwise(map(int, input_file)))
    print(sum(1 for element in filtered_readings))
