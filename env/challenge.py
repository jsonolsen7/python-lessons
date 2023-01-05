# only integers
test_list = [1, "goat", 12, "pig", 27, "sloth"]

def only_integers(l):
    integers = list(filter(lambda x: type(x) == int, l))
    print(integers)

only_integers(test_list)

# hide credit card
credit_card = "4444444444444444"

def hide_numbers(card):
    print(("*" * (len(card) - 4)) + card[-4:])

hide_numbers(credit_card)