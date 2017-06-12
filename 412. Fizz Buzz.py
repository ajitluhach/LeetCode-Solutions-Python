"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""

# Soution 1
def fizzBuzz(self, n):
    """
    :type n: int
    :rtype: List[str]
    """
    result = []

    for i in range(n):
        three = True if (i+1) % 3 == 0 else False
        five = True if (i + 1) % 5 == 0 else False
        if three and five:
            result.append('FizzBuzz')
        elif three:
            result.append('Fizz')
        elif five:
            result.append('Buzz')
        else:
            result.append(str(i+1))
    return result

    # Solution 2
    return ['Fizz'*(not i % 3) + 'Buzz'*(not i % 5) or str(i) for i in range(1, n + 1]
