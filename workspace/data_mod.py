# def classify_age(age):
#     if age < 18:
#         return "Minor"
#     elif 18 <= age <= 65:
#         return "Adult"
#     else:
#         return "Senior Citizen"


# age = float(input("Enter your age: "))
# print(classify_age(age))


def calculate_sum(lst):
    return sum(lst)


lstr = input("Enter a list of float values separated by commas: ")
lst = [float(x) for x in lstr.split(',')]
result = calculate_sum(lst)
print(result)