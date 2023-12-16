# Credit - C 💳🖹
In the `credit.c` file, the lengths and first digits of the specific cards are stored in tables in global variables so the values can be accessed by any of the functions. Here, apart from `main()`, the following functions are declared.

```c
unsigned int get_digits(long number);
bool get_validity(long number, unsigned int digits);
unsigned int get_cardtype(long number, unsigned int digits);
void print_cardtype(unsigned int card_type);
```

The `main()` function mainly goes through several tasks which are accomplished by the list of functions previously mentioned.
1. Prompt the user for their card number

```c
do
{
    user_input = get_long("Number: ");
} while (user_input < 0);
```

2. Count the number of digits

```c
unsigned int digits = get_digits(user_input);
if (digits != MIN && digits != MIDDLE && digits != MAX)
{
    printf("INVALID\n");
    return 0;
}
```

The `get_digits()` function contains a _for loop_ specifically designed to count the number of digits of the inserted input using the **modulo** operator (%).

3. Check whether the card is valid or not

The `get_validity()` uses Luhn's Algorithm to check the card's validity. Two _for loops_ go through every second number of the list (one starting from the first one and the other starting from the second one) 

```c
// First values
for (unsigned int i = 0; i < digits; i += 2)
{
    first_values += number_check % 10;
    number_check /= 100;
}

// Second Values
for (unsigned int i = 0; i < digits; i += 2)
{
    tmp_value = (number_check % 10) * 2;
    if (tmp_value >= 10)
        tmp_value = 1 + (tmp_value % 10);
    second_values += tmp_value;
    number_check /= 100;
}
```

Lastly, the _digits_' values are added together and if the total modulo 10 is congruent to 0 the number is valid.

```c
sum = first_values + second_values;
sum %= 10;

if (sum == 0)
    return true;
return false;
```

4. In case the card is valid, what type of card it is.

The function `get_cardtype()` compares the length of the inserted card number and the first digits with the global variables previously declared through a series of _if statements_. In case of any match, the corresponding card value equivalent to the card type is returned.

```c
const unsigned int AMEX = 1;
const unsigned int MASTERCARD = 2;
const unsigned int VISA = 3;
const unsigned int INVALID = 4;
```

5. Print out the card type

The function `print_cardtype()` check the value returned by the `get_cardtype()` function and prints out the card corresponding to that value.