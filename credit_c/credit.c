// Credit
//
// Copyright(c) 2023 Alessandro Amatucci Girlanda
//
// This work is licensed under the Creative Commons Attribution - NonCommercial - ShareAlike
//  4.0 International License.To view a copy of this license, visit
// http: // creativecommons.org/licenses/by-nc-sa/4.0/ or send a letter to Creative
// Commons, PO Box 1866, Mountain View, CA 94042, USA.
//
// You are free to:
// - Share — copy and redistribute the material in any medium or format
// - Adapt — remix, transform, and build upon the material
//
// Under the following terms:
// - Attribution — You must give appropriate credit, provide a link to the license, and
// indicate if changes were made.You may do so in any reasonable manner,
// but not in any way that suggests the licensor endorses you or your use.
// - NonCommercial — You may not use the material for commercial purposes.
// - ShareAlike — If you remix, transform, or build upon the material, you must
// distribute your contributions under the same license as the original.
//
// No additional restrictions — You may not apply legal terms or technological measures
// that legally restrict others from doing anything the license permits.
//
// Acknowledgment:
// This file includes the CS50 C Library developed by Harvard University CS50.

#include <cs50.h>
#include <math.h>
#include <stdio.h>

const unsigned int AMEX = 1;
const unsigned int MASTERCARD = 2;
const unsigned int VISA = 3;
const unsigned int INVALID = 4;

const unsigned int MIN = 13;
const unsigned int MIDDLE = 15;
const unsigned int MAX = 16;

unsigned int get_digits(long number);
bool get_validity(long number, unsigned int digits);
unsigned int get_cardtype(long number, unsigned int digits);
void print_cardtype(unsigned int card_type);

int main(void)
{
    long user_input;

    // Prompt user for a card number
    do
    {
        user_input = get_long("Number: ");
    } while (user_input < 0);

    // Find Number of Digits
    unsigned int digits = get_digits(user_input);
    if (digits != MIN && digits != MIDDLE && digits != MAX)
    {
        printf("INVALID\n");
        return 0;
    }

    // Luhn's Algorithm Check
    bool validity = get_validity(user_input, digits);
    if (validity == false)
    {
        printf("INVALID\n");
        return 0;
    }

    // Check Card type
    unsigned int card_type = get_cardtype(user_input, digits);

    // Print out card-type/Error
    print_cardtype(card_type);
}

unsigned int get_digits(long number)
{
    unsigned int digits = 0;
    long number_check = number;

    while (number_check != 0)
    {
        digits++;
        number_check /= 10;
    }

    return digits;
}

bool get_validity(long number, unsigned int digits)
{
    unsigned int first_values = 0, second_values = 0, sum;
    long number_check = number;

    // First values
    for (unsigned int i = 0; i < digits; i += 2)
    {
        first_values += number_check % 10;
        number_check /= 100;
    }

    // Second values
    unsigned int tmp_value;
    number_check = number / 10;
    for (unsigned int i = 0; i < digits; i += 2)
    {
        tmp_value = (number_check % 10) * 2;
        if (tmp_value >= 10)
            tmp_value = 1 + (tmp_value % 10);
        second_values += tmp_value;
        number_check /= 100;
    }

    sum = first_values + second_values;
    sum %= 10;

    if (sum == 0)
        return true;
    return false;
}

unsigned int get_cardtype(long number, unsigned int digits)
{
    unsigned int card_type = INVALID;

    // First Digits Check
    int first_digit = number / pow(10, digits - 1);
    int second_digit = (int)(number / pow(10, digits - 2)) % 10;

    // Check card type
    // VISA card check
    if (digits == MIN && first_digit == 4)
    {
        card_type = VISA;
    }
    // AMERICAN EXPRESS card check
    else if (digits == MIDDLE)
    {
        if (first_digit == 3 && (second_digit == 4 || second_digit == 7))
            card_type = AMEX;
        else
            card_type = INVALID;
    }
    // MASTERCARD and VISA card check
    else if (digits == MAX)
    {
        // VISA check
        if (first_digit == 4)
            card_type = VISA;

        // MASTERCARD check
        else if (first_digit == 5)
        {
            for (unsigned int i = 1; i < 6; i++)
            {
                if (second_digit == i)
                {
                    card_type = MASTERCARD;
                    break;
                }
            }
        }
    }

    return card_type;
}

void print_cardtype(unsigned int card_type)
{
    switch (card_type)
    {
    case AMEX:
        printf("AMEX\n");
        break;

    case MASTERCARD:
        printf("MASTERCARD\n");
        break;

    case VISA:
        printf("VISA\n");
        break;

    default:
        printf("INVALID\n");
        break;
    }
}