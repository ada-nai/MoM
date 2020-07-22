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
    def __init__():
        '''
        Rational Class constructor
        '''
        # ToDo: Instantiate the instance variables as mentioned in the arguments
        pass
    
    # ToDo: Define the string representation method for the Rational class.
    # The representation on printing a Rational class object should be `numerator/denominator`
    # e.g.: print(Rational(1, 2)) == '1/2'
    def __repr__():
        '''
        String representation method of the Rational class
        '''
        return None
    
    # ToDo: Create a function to multiply two rational numbers
    # Argument: Another number - could be an int or another Rational number
    # Hint: Use the isinstance() method to check if the given number is an integer or Rational 
    # number and create conditions to multiply accordingly
    def __mul__():
        '''
        Multiplies a Rational Number with an int or another Rational Number
        '''
        # Use if-else conditions
        
        # ToDo: Check if number is an instance of class int, multiply accordingly
        
        # ToDo: Check if number is an instance of class Rational , multiply accordingly
        
        # # ToDo: Raise an error
        
        return None
    
    def isPerfectSquare():
        '''
        Checks if the Rational number is a perfect square
        '''
        # ToDo: Evaluate the square root of the numerator and denominator 
        # Use the `sqrt` method of the math class
        sqr_num = 
        sqr_denom = 
        
        # ToDo: Check if the square root values indicate both are perfect squares
        
        # ToDo: Return appropriate boolean value
        return None
    
    # ToDo: Evaluate the rational number to its reduced form. For this we will require a 
    # `_gcd` method to find the greatest common divisor of the numerator and denominator of rational
    # number
    def _gcd(self):
        '''
        Evaluates the GCD of the numerator and denominator of Rational number
        '''
        # ToDo: Find out the smaller and larger of the two numbers using the `min()` and `max()` function
        smaller = 
        larger = 
        
        # ToDo: Find the divisors of the smaller number
        small_divisors = 
        
        # ToDo: Find the common divisors by checking if each divisor of the smaller number is also 
        # a divisor of the larger number
        common_divisors = 
        
        # ToDo: Find the max of the common divisors
        gcd = 
        return None
    
    
    def reduce():
        '''
        Reduce the Rational number to its lowest form
        '''
        # ToDo: Get the GCD of the numerator denominator from the _gcd method
        gcd =
        
        # ToDo: Divide the numerator and the denominator by the gcd and update their values
        
        
        return self
    