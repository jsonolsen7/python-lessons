from type_practice import is_palindrome

# def is_palindrome(string):
#     letters = list(string)
#     flipped = reversed(letters)
#     rejoin = "".join(flipped)
#     return string == rejoin

def main():
    string1 = "kayak"
    string2 = "deer"
    print(is_palindrome(string1))
    print(is_palindrome(string2))

if __name__ == "__main__":
    main()