#  Credit
#  
#  Copyright (c) 2023 Alessandro Amatucci Girlanda
#  
#  This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike
#  4.0 International License. To view a copy of this license, visit
#  http://creativecommons.org/licenses/by-nc-sa/4.0/ or send a letter to Creative
#  Commons, PO Box 1866, Mountain View, CA 94042, USA.
#  
#  You are free to:
#    - Share — copy and redistribute the material in any medium or format
#    - Adapt — remix, transform, and build upon the material
# 
#  Under the following terms:
#    - Attribution — You must give appropriate credit, provide a link to the license, and
#                   indicate if changes were made. You may do so in any reasonable manner,
#                   but not in any way that suggests the licensor endorses you or your use.
#    - NonCommercial — You may not use the material for commercial purposes.
#    - ShareAlike — If you remix, transform, or build upon the material, you must
#                   distribute your contributions under the same license as the original.
# 
#  No additional restrictions — You may not apply legal terms or technological measures
#  that legally restrict others from doing anything the license permits.
#
#  Acknowledgment:
#  This file includes the CS50 Python Library developed by Harvard University CS50.

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

    # Luhn's Algorithm
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
