# def divide(dividend: int, divisor: int) -> float:
#     if divisor == 0:
#         raise ZeroDivisionError("Divisor cannot be 0")
#     return dividend/divisor

# def calculate(*values, operator) -> float:
#     return operator(*values)

# result = calculate(20, 4 , operator=divide)

# print(result)

def search(sequence, expected, finder):
    for elem in sequence:
        print(elem)
        if finder(elem) == expected:
            return elem
        raise RuntimeError(f"Could not find an element with the expected {expected}")


friends = [
    {"name": "Rolf Smith", "age": 30},
    {"name": "Adam Wool ", "age": 18},
    {"name": "Anne Pun", "age": 24}
    
]


print(search(friends, "Rolf Smith", lambda friend: friend["name"]))
