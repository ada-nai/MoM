from RationalNumbers import Rational
import sys

class test_cases:
    def check_code(self, obj):
        # Case 2
        assert obj.numerator == 2, 'Numerator attribute not declared correctly, check again.'

        # Case 3
        assert obj.denominator == 7, 'Denominator attribute not declared correctly, check again.'

        # Case 4
        assert str(obj) == '2/7', 'Object not printed correctly'

        # Case 5
        v1 = str(obj * 3)
        assert v1 == str(Rational(6, 7))

        # Case 6
        v2 = str(obj * Rational(5, 3))
        assert v2 == str(Rational(10, 21))

        # Case 7
        v3 = Rational(1089, 2304)
        v3a = v3.isPerfectSquare()
        assert v3a == True

        # Case 8
        v4 = Rational(961, 2086)
        assert v4.isPerfectSquare() == False

        # Case 9
        v5 = str(Rational(49832530, 1955622064).reduce())
        assert v5 == str(Rational(2265115, 88891912))

        print('Great Work!!!')


if __name__ == '__main__':
    try:
        obj = Rational(2, 7)
    except Exception as e:
        print('Error initializing object: ', e)
        sys.exit()

    test_obj = test_cases()
    test_obj.check_code(obj)
