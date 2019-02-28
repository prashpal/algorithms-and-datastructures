# Integer multiplication using recursion
# Author: Prashanth Palaniappan

'''
Description:
This is an algorithm that performs multiplication of 2 integers of size n using recursion.

Solution:
The algorithm recursively divides the input numbers by half, until we are left with single digits.
This is the base case for recursion.
Once we hit the base case, we perform regular multiplication of the single digits
'''


def multiply(x, y, n):
    '''
    :param x: input number 1
    :param y: input number 2
    :param n: length of the input numbers
    :return: multiplied result of the 2 input numbers

    a = first half of x
    b = second half of x
    c = first half of y
    d = second half of y

    x * y   = ((10^n/2 * a) + b) * ((10^n/2 * c) + d)
            = (10^n * ac) + (10^n/2 * (ad + bc)) + bd
    '''
    if n == 1:
        return x * y
    a = int(x / pow(10, n/2))
    b = int(x - (a * pow(10, n/2)))
    c = int(y / pow(10, n/2))
    d = int(y - (c * pow(10, n/2)))
    ac = multiply(a, c, n/2)
    bd = multiply(b, d, n/2)
    bc_plus_ad = multiply(a + b, c + d, n/2) - ac - bd
    mul_result = (pow(10, n) * ac) + (pow(10, n/2) * bc_plus_ad) + bd
    return mul_result


# Get the input numbers from an user
x = int(input('First number: '))
y = int(input('Second number: '))
n = len(str(x))

# Compute and print the result
result = int(multiply(x, y, n))
print(result)
