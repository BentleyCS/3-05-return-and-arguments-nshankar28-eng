# Functions converted from input/print to arguments/returns

# Takes 2 numbers as arguments and returns the larger number
def larger(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2


# Takes a grade as an argument and returns the letter grade
# 90+ A
# 80+ B
# 70+ C
# 60+ D
# 59- F
def grade(g):
    if g >= 90:
        return "A"
    elif g >= 80:
        return "B"
    elif g >= 70:
        return "C"
    elif g >= 60:
        return "D"
    else:
        return "F"


# Takes a number as an argument and returns:
# "fizz" if divisible by 3
# "buzz" if divisible by 5
# "FizzBuzz" if divisible by both
# the number itself otherwise
def fizzBuzz(n):
    if n % 5 == 0 and n % 3 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return n


# Takes a number as an argument and returns:
# n/2 if n is even
# 3*n+1 if n is odd
def collatz(n):
    if n == 1:
        return n
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1


# Takes a temperature string (ending in F or C) and returns the converted temperature
# Example: "32F" -> "0C"  "20C" -> "68F"
def convertTemperature(input):
    if input[len(input) - 1] == "C":
        temp = int(input[0:len(input) - 1])
        out = temp * (9 / 5) + 32
        return str(int(out)) + "F"
    elif input[len(input) - 1] == "F":
        temp = int(input[0:len(input) - 1])
        out = (temp - 32) * 5 / 9
        return str(int(out)) + "C"


# Example usage:
if __name__ == "__main__":
    print("larger(10, 5):", larger(10, 5))
    print("grade(85):", grade(85))
    print("fizzBuzz(15):", fizzBuzz(15))
    print("collatz(6):", collatz(6))
    print("convertTemperature('32F'):", convertTemperature('32F'))