import time
from collections.abc import Collection


def average_runtime(words: Collection) -> float:
    """
        The function is used to measure the performance of a data structure-
        it performs a search for the word "zwitterion", in the data structure that the function received,
        and returns the average time taken to search it.
        :param words: The data structure that contains words.
        :return: The average time taken to search the word "zwitterion" in the data structure.
    """
    runtime = 0
    for iteration in range(1000):
        start = time.time()
        foo = "zwitterion" in words
        end = time.time()
        runtime += end - start
    return runtime / 1000


if __name__ == '__main__':
    word_list = open("words.txt", "r").read().splitlines()
    word_set = set(word_list)

    print("Time of list:", average_runtime(word_list))
    print("Time of set:", average_runtime(word_set))
