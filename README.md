# Credit 💳
A program that can identify if a credit/debit card is valid and what type it is.

## About the Project 📖
The program prompts the user to insert their card number which is then scannaed and analysed by a series of functions. Throuhgh the use of **Luhn's Algorithm**, the program checks if the card matches any of the following types:

+ American Express
+ MasterCard
+ Visa

### Card Validity - Lunh's Algorithm ✅
Most cards use an algorithm invented by Hans Peter Luhn of IBM. According to Luhn’s algorithm, you can determine if a credit card number is (syntactically) valid as follows:

1. Multiply every other digit by 2, starting with the number’s second-to-last digit, and then add those products’ digits together.
2. Add the sum to the sum of the digits that weren’t multiplied by 2.
3. If the total modulo 10 is congruent to 0 the number is valid

### Card Distinguishment 👥
Each card type can be distinguished from the others by their respective features; the number of digits and the first couple of digits.

| Card Type      | Number of Digits | First Digits      |
|----------------|------------------|-------------------|
|American Express|15                |34, 37             |
|MasterCard      |16                |51, 52, 53, 54, 55 |
|Visa            |13, 16            |4                  |

e.g.)

Visa: 4003600000000014.

For the sake of discussion, let’s first highlight every other digit, starting with the number’s second-to-last digit:

**4**0**0**3**6**0**0**0**0**0**0**0**0**0**1**4

Multiply each of the bolded digits by 2:

1•2 + 0•2 + 0•2 + 0•2 + 0•2 + 6•2 + 0•2 + 4•2

That gives us:

2 + 0 + 0 + 0 + 0 + 12 + 0 + 8

Add those products’ digits (i.e., not the products themselves) together:

2 + 0 + 0 + 0 + 0 + 1 + 2 + 0 + 8 = 13

Add that sum (13) to the sum of the digits that weren’t multiplied by 2 (starting from the end):

13 + 4 + 0 + 0 + 0 + 0 + 0 + 3 + 0 = 20

The last digit in that sum (20) is a 0, so the card is a valid Visa.

## Folders 🗂️
The repository includes two different folders. Each of them contains the same _credit_ project. One is written in _C_, `credit_c` whilst `credit_python` is written in _Python_. Either of the two folders can be used to test the program. The main idea was being able to demonstrate my skills in these two languages by building the same project.

## Execute the Project ▶️
Start by cloning the repository on your local machine.

```
git clone https://github.com/ErTucci674/credit.git
```

### Running the _C_ Project 🖹
The main library needed is the _CS50 C Library_ which can be downloaded from the [CS50 C Library GitHub](https://github.com/cs50/libcs50). If you have windows, you can install the library with the `winget` command.

```
winget install libcs50
```

To compile and run the project make sure to be in the `credit_c` path and enter the following commands in the terminal:

```
make credit.c
./credit
```

### Running the _Python_ Project 🐍
The main library needed is the _CS50_ library which can be downloaded from the [CS50 Python Library GitHub](https://github.com/cs50/python-cs50). You can also install the library through the command `pip`.

```
pip3 install cs50
```

To run the project make sure to be in the `credit_python` path and enter the following command in the terminal:

```
python credit.py
```

## Aknowledgements 🤝
The project has been developed during an online course with Harvard University.

Harvard University Online Course (edx50) - [Introduction to Computer Science](https://www.edx.org/learn/computer-science/harvard-university-cs50-s-introduction-to-computer-science)

## Licence 🖋️
This project is licensed under the terms of the GNU General Public License, version 3.0.