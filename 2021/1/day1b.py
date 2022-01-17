import logging
from itertools import islice, tee

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)


def pairwise(iterator):
    """Return an iterator yielding pairs of each element and the following"""
    i = iter(iterator)
    prev = next(i)
    for item in i:
        yield prev, item
        prev = item


def rolling_window(iterator, size=3):
    """Return an iterator yielding n-tuples of consecutive elements"""
    iter_tee = tee(iter(iterator), size)
    islice_tuple = (islice(iter_, n, None) for n, iter_ in enumerate(iter_tee))
    return zip(*(islice_tuple))


def sonar_filter(previous_and_current_reading):
    """Return True for each pair (a, b) with b > a (plus some debug logging)"""
    prev_reading, curr_reading = previous_and_current_reading
    if curr_reading > prev_reading:
        logging.debug("{0} (increased)".format(curr_reading))
        return True
    elif curr_reading == prev_reading:
        logging.debug("{0} (no change)".format(curr_reading))
    else:
        logging.debug("{0} (decreased)".format(curr_reading))
    return False


with open(file="input.txt", mode="r") as input_file:
    # input_file = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    readings = map(int, input_file)

    pair_iter = pairwise(map(sum, rolling_window(readings)))

    print(sum(1 for element in filter(sonar_filter, pair_iter)))
