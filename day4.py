import re


def increasing(number):
    return number[0] <= number[1] <= number[2] <= number[3] <= number[4] <= number[5]


def repeating_digits(number):
    regexp = re.compile(r"(\d)\1+")
    if regexp.search(number):
        return True
    return False


def adjacent_matching_digits(number):
    return [str(number).count(d) for d in str("1234567890")].count(2) > 0


def valid_passwords():
    possible_passwords = list(map(lambda x: str(x), range(171309, 643604)))
    valid_passwords = list(
        filter(lambda x: increasing(x) and repeating_digits(x), possible_passwords)
    )
    return valid_passwords


def number_of_valid_passwords():
    return len(valid_passwords())


def number_of_valid_adjacent_matching_passwords():
    possible_passwords = valid_passwords()
    return len(list(filter(lambda x: adjacent_matching_digits(x), possible_passwords)))


print(number_of_valid_passwords())
print(number_of_valid_adjacent_matching_passwords())
