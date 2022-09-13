def divide(dividend: int, divisor: int) -> float:
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0")
    return dividend/divisor

# grades = []

# print("Welcome to the average grade program.")

# try:
#     average = divide(sum(grades), len(grades))
# except ZeroDivisionError as e:
#     # print(e)
#     print("There are no grades yet in your list")
# else: 
#     # if the try is executed success execute this
#     print(f"The average grade is {average}")
# finally:
#     # executes no matter what appends error or success
#     print("Done")

students = [
    {"name": "Bob", "grades": [75, 90]},
    {"name": "Rolf", "grades": [50]},
    {"name": "Jen", "grades": [100,90]}
    ]

try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = divide(sum(grades), len(grades))
        print(f"name: {name}, average: {average}.")
except ZeroDivisionError:
    print(f"ERROR: {name} has no grades!")
else:
    print("-- All student averages calculated --")
finally:
    print("-- End of student average calculation --")
