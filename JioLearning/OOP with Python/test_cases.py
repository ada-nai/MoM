from rational_numbers import Rational
import sys

class test_cases:
    def check_code(self, obj):
        # Case 2
        assert obj.numerator == 2, 'Numerator attribute not declared correctly, check again.'
        print('Case 2 passed!')

        # Case 3
        assert obj.denominator == 7, 'Denominator attribute not declared correctly, check again.'
        print('Case 3 passed!')

        # Case 4
        assert str(obj) == '2/7', 'Object string representation not correct. Read the comments'
        print('Case 4 passed!')

        # Case 5
        v1 = str(obj * 3)
        assert v1 == str(Rational(6, 7)), 'Incorrect product result with int'
        print('Case 5 passed!')

        # Case 6
        v2 = str(obj * Rational(5, 3))
        assert v2 == str(Rational(10, 21)), 'Incorrect product result with Rational'
        print('Case 6 passed!')

        # Case 7
        v3 = Rational(1089, 2304)
        v3a = v3.isPerfectSquare()
        assert v3a == True, 'isPerfectSquare() might not be working as desired. Make\
        \sure square root result is converted to int'
        print('Case 7 passed!')

        # Case 8
        v4 = Rational(961, 2086)
        v4a = v4.isPerfectSquare()
        assert v4a == False, 'isPerfectSquare() might not be working as desired. Make\
        \sure square root result is converted to int'
        print('Case 8 passed!')

        # Case 9
        v5 = str(Rational(49832530, 1955622064).reduce())
        assert v5 == str(Rational(2265115, 88891912)), 'reduce() function results not matching.'
        print('Case 9 passed!')

        print('Great Work!!! All cases passed :)')


if __name__ == '__main__':
    try:
        obj = Rational(2, 7)
        print('Case 1 passed!')
    except Exception as e:
        print('Error initializing object: ', e)
        sys.exit()

    test_obj = test_cases()
    test_obj.check_code(obj)
