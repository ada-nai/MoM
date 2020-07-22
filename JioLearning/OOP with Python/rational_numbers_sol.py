# import math package for calculating square root
import math

# ToDo: Create the `Rational` class
class Rational:
    '''
    name: Rational

    description:
    Class for initializing and operating on Rational Numbers. A rational number is a number that can be\
    expressed as the quotient or fraction p/q of two integers, a numerator p and a non-zero denominator q

    args:
    numerator - numerator of rational number
    denominator - denominator of rational number
    '''
    # Create the constructor for the class. It should have two arguments:
    # `numerator` and `denominator` (The attributes must be as mentioned here)
    def __init__(self, numerator, denominator):
        '''
        Rational Class constructor
        '''
        # ToDo: Instantiate the instance variables as mentioned in the arguments
        self.numerator = numerator
        self.denominator = denominator

    # ToDo: Define the string representation method for the Rational class.
    # The representation on printing a Rational class object should be `numerator/denominator`
    # e.g.: print(Rational(1, 2)) == '1/2'
    def __repr__(self):
        '''
        String representation method of the Rational class
        '''
        return f'{self.numerator}/{self.denominator}'

    # ToDo: Create a function to multiply two rational numbers
    # Argument: Another number - could be an int or another Rational number
    # Hint: Use the isinstance() method to check if the given number is an integer or Rational
    # number and create conditions to multiply accordingly
    def __mul__(self, number):
        '''
        Multiplies a Rational Number with an int or another Rational Number
        '''
        # Use if-else conditions
        # ToDo: Check if number is an instance of class int, multiply accordingly
        if isinstance(number, int):
            return Rational(self.numerator * number, self.denominator)
        # ToDo: Check if number is an instance of class Rational , multiply accordingly
        elif isinstance(number, Rational):
            return Rational(self.numerator * number.numerator, self.denominator * number.denominator)
        # # ToDo: Raise an error
        else:
            raise TypeError(f'Expected number to be int or Rational. Got {type(number)}')


    def isPerfectSquare(self):
        '''
        Checks if the Rational number is a perfect square
        '''
        # ToDo: Evaluate the square root of the numerator and denominator
        # Use the `sqrt` method of the math class
        sqr_num = math.sqrt(self.numerator)
        sqr_denom = math.sqrt(self.denominator)
#         print(sqr_num, sqr_denom)
        # ToDo: Check if the square root values indicate both are perfect squares
        if sqr_num - math.floor(sqr_num) != 0:
            return False
        if sqr_denom - math.floor(sqr_denom) != 0:
            return False
        # ToDo: Return appropriate boolean value
        sqr_num = int(sqr_num)
        sqr_denom = int(sqr_denom)
#         print(f'The square root of {Rational(self.numerator, self.denominator)} is {Rational(sqr_num, sqr_denom)}')
        return True

    # ToDo: Evaluate the rational number to its reduced form. For this we will require a
    # `_gcd` method to find the greatest common divisor of the numerator and denominator of rational
    # number
    def _gcd(self):
        '''
        Evaluates the GCD of the numerator and denominator of Rational number
        '''
        # ToDo: Find out the smaller and larger of the two numbers using the `min()` and `max()` function
        smaller = min(self.numerator, self.denominator)
        larger = max(self.numerator, self.denominator)

        # ToDo: Find the divisors of the smaller number
        small_divisors = {i for i in range(1, smaller + 1) if smaller % i == 0}

        # ToDo: Find the common divisors by checking if each divisor of the smaller number is also
        # a divisor of the larger number
        common_divisors = {i for i in small_divisors if larger % i == 0}

        # ToDo: Find the max of the common divisors
        gcd = max(common_divisors)

        return gcd


    def reduce(self):
        '''
        Reduce the Rational number to its lowest form
        '''
        # ToDo: Get the GCD of the numerator denominator from the _gcd method
        gcd = self._gcd()

        # ToDo: Divide the numerator and the denominator by the gcd and update their values
        self.numerator = int(self.numerator / gcd)
        self.denominator = int(self.denominator / gcd)
#         print(self.numerator, self.denominator)

        return self
