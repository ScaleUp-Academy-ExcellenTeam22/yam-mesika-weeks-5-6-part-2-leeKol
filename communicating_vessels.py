from collections.abc import Collection
import itertools


def interleave(*iterables: Collection) -> list:
    """
        The function receives one or more iterable parameters, and returns a list of intertwined items.
        For example, for the call: interleave('abc', [1, 2, 3], ('!', '@', '#')), the value to be returned
        is: ['a', 1, '!', 'b', 2, '@', 'c', 3, '#'].
        :param iterables: The iterables that need to be intertwined.
        :return: The intertwined list.
    """
    return list(filter(lambda item: item is not None, list(itertools.chain(*list(itertools.zip_longest(*iterables))))))


if __name__ == '__main__':
    interleave_generator = (list_item for list_item in interleave('abcde', [1, 2, 3], ('!', '@', '#')))  # the generator
    interwoven_list = list(interleave_generator)
    print(interwoven_list)
