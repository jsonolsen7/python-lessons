# simple function
def my_first_function(n):
    print("I love " + n + "!")

my_first_function("cats")


new_list = [2, 5, 7, 32, 100, 9, 56, 74, 97, 22, 13, 80]

# filter - evens only
evens = list(filter(lambda x: x % 2 == 0, new_list))
print(evens)

# map - mutiply by 3
mult_by_3 = list(map(lambda x: x * 3, new_list))
print(mult_by_3)

# reduce - find sum
from functools import reduce
sum = reduce(lambda a, b: a + b, new_list)
print(sum)

# palindrome function
def is_palindrome(string):
    letters = list(string)
    flipped = reversed(letters)
    rejoin = "".join(flipped)
    return string == rejoin

print(is_palindrome("racecar"))
print(is_palindrome("goat"))

# multiple inputs to palindrome
answers = []
def are_palindromes(*args):
    for arg in args:
        answers.append(is_palindrome(arg))

are_palindromes("racecar", "goat", "kayak", "deer")
print(answers)