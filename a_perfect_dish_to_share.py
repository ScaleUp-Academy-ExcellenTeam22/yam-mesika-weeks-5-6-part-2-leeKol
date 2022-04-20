from typing import Generator


def perfect_dish_size_to_share() -> Generator[int, None, None]:
    """
        The function is a generator that infinitely returns sizes of dishes that are considered perfect for share.
        A dish is considered perfect for share if it holds that when we sum up all the ways to divide it,
        we get the size of the dish itself.
        :return: The size of a "perfect for share" dish.
    """
    current_dish_size = 2
    while True:
        divisor_sum = 0
        for number in range(1, int((current_dish_size / 2) + 1)):
            if current_dish_size % number == 0:
                divisor_sum += number
        if divisor_sum == current_dish_size:
            yield current_dish_size
        current_dish_size += 1


if __name__ == '__main__':
    for dish_size in perfect_dish_size_to_share():
        print(dish_size)
