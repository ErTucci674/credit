# Credit - Python 💳🐍
In the `credit.py` file, the lengths and first digits of the specific cards are stored in tables: `lengths`, `digits`.

```python
lengths = {"AMEX": [15], "MASTERCARD": [16], "VISA": [13, 16]}
digits = {
    "AMEX": ["34", "37"],
    "MASTERCARD": ["51", "52", "53", "54", "55"],
    "VISA": ["4"],
}
```

The `main()` function mainly goes through 3 different tasks:
1. Prompt the user for their card number

```python
while True:
    number = get_int("Number: ")
    if number > 0:
        break
```

2. Check whether the card is valid or not

```python
valid = check_validity(str_number)
```

The `check_validity()` function compares the user's input legth with the pre-requisites stored in the global variables. A simple _if_ statement is used.

```python
number_len = len(number)
if number_len < MIN_LENGTH or number_len > MAX_LENGTH:
    return False
```

Luhn's Algorithm is applied to check the validity. Since all the calculations start from the last number of the user's input, for simplicity, the number is reversed and stored in a new vartiable `rev`. Through a couple of _for loops_ the algorithm is executed and the digits stored in `digits1` and `digits2`.

```python
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
```

Lastly, the _digits_' values are added together and if the total modulo 10 is congruent to 0 the number is valid.

```python
tot = digits1 + digits2
if (tot % 10) == 0:
    return True
```

3. In case the card is valid, what type of card it is.

```python
if valid == False:
    card_type = "INVALID"
else:
    card_type = get_card(str_number)
```

The function `get_card()` compares the length of the inserted card number and the first digits with the `lengths` and `digits` lists through a series of _if statements_. In case of any match, the corresponding card name is returned.

4. Print out the card type

```python
print(card_type)
```