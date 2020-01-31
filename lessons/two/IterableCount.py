from collections import Counter
from itertools import repeat, chain


def iterable(array):
    result = list(chain.from_iterable(repeat(i, c) for i, c in Counter(array).most_common()))
    print(result)


iterable([4, 6, 2, 2, 6, 4, 4, 4])
iterable(['bob', 'bob', 'carl', 'alex', 'bob'])
iterable([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 1, 1, 1, 5, 5, 6, 6, 6])
