reversed_number = 0
original_number = int(input("enter"))

while original_number > 0:
    last_digit = original_number % 10
    reversed_number = (reversed_number * 10) + last_digit
    original_number = original_number // 10

print(reversed_number)
