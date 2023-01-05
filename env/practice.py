# 10x10 zeros list
import array as arr
my_array = [[0] * 10 for i in range(10)]

# multiplication table
for i in range(0, 10):
    for j in range(0, 10):
        my_array[i][j] = (i + 1) * (j + 1)

for i in my_array:
    print(i)

# tuples
leaders = "Vladimir Lenin", "Thomas Jefferson", "Barack Obama", "Tsar Nicholas III", "John Curtin"
a, b, c, d, e = leaders
leaders_dictionary = {
    a : "Russia",
    b : "US",
    c : "US",
    d : "Russia",
    e : "Australia"
}
for k, v in leaders_dictionary.items():
    print(f"{k} : {v}")

# cars dictionary
customers = []
while True:
    user_input = input("Enter another name?: [Yes/No] ")
    user_input = user_input[0].lower()
    if user_input == "n":
        break
    else:
        first_name, last_name = input("Enter your name [first/last]: ").split("/")
        customers.append({"first_name": first_name, "last_name": last_name})
    for c in customers:
        print(c["first_name"], c["last_name"])

# Fizz Buzz
for n in range(1, 25):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)