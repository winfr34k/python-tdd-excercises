import functools


def add(numbers: str) -> int:
    delimiter, string_numbers = _extract_delimiter_and_numbers_from_input(numbers)
    numbers_without_newlines = string_numbers.replace("\n", delimiter)
    integer_numbers = [int(number or 0) for number in numbers_without_newlines.split(delimiter)]

    negative_numbers = [number for number in integer_numbers if number < 0]
    if len(negative_numbers) > 0:
        raise NegativeNumbersException(negative_numbers)

    return functools.reduce(lambda a, b: a + b, integer_numbers, 0)


def _extract_delimiter_and_numbers_from_input(_input,
                                              custom_delimiter_starts_with="//",
                                              custom_delimiter_ends_with="\n",
                                              default_delimiter=","):
    if custom_delimiter_starts_with in _input and custom_delimiter_ends_with in _input:
        return _input.split(custom_delimiter_starts_with)[1].split(custom_delimiter_ends_with)

    return default_delimiter, _input


class NegativeNumbersException(Exception):
    def __init__(self, negative_numbers: list):
        self.negative_numbers = negative_numbers

    def __str__(self):
        return "negatives not allowed: %s" % self.negative_numbers
