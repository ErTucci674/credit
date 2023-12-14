# Copyright (C) 2023 Alessandro Amatucci Girlanda

# This file is part of Credit.

# Credit is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Credit is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Credit. If not, see
# <https: //www.gnu.org/licenses />.

from cs50 import get_int


MIN_LENGTH = 13
MAX_LENGTH = 16

lengths = {"AMEX": [15], "MASTERCARD": [16], "VISA": [13, 16]}
digits = {
    "AMEX": ["34", "37"],
    "MASTERCARD": ["51", "52", "53", "54", "55"],
    "VISA": ["4"],
}


def main():
    # Prompt for user's input
    # Check if a valid input has been inserted
    while True:
        number = get_int("Number: ")
        if number > 0:
            break

    # String conversion
    str_number = str(number)

    # Check validity
    valid = check_validity(str_number)
    if valid == False:
        card_type = "INVALID"
    else:
        # Check card type
        card_type = get_card(str_number)

    # Print out type of card or INVALID error
    print(card_type)


def check_validity(number):
    # Check if input length it's in the desired range
    number_len = len(number)
    if number_len < MIN_LENGTH or number_len > MAX_LENGTH:
        return False

    # Luhn's Agorithm
    rev = number[::-1]
    digits1 = 0
    digits2 = 0

    # Take every second digit starting from last digit
    # Add the new number to digits2
    for d in rev[0::2]:
        digits1 += int(d)

    # Take every second digit starting from second last digit
    # Multiply it by 2
    # Add the two digits if number is greater than 9
    # Add the new number to digits2
    for d in rev[1::2]:
        tmp_digit = int(d) * 2
        if tmp_digit > 9:
            tmp_digit = 1 + tmp_digit % 10
        digits2 += tmp_digit

    tot = digits1 + digits2
    if (tot % 10) == 0:
        return True

    return False


def get_card(number):
    # Check length
    number_len = len(number)

    # Check if AMERICAN EXPRESS
    if number[0:2] in digits["AMEX"]:
        if number_len in lengths["AMEX"]:
            return "AMEX"
        else:
            return "INVALID"

    # Check if VISA
    if number[0] in digits["VISA"]:
        if number_len in lengths["VISA"]:
            return "VISA"
        else:
            return "INVALID"

    # Check if MASTER CARD
    if number[0:2] in digits["MASTERCARD"]:
        if number_len in lengths["MASTERCARD"]:
            return "MASTERCARD"
        else:
            return "INVALID"

    return "INVALID"


if __name__ == "__main__":
    main()
