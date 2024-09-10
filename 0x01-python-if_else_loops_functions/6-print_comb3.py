#!/usr/bin/python3
for first_digit in range(9):
    for second_digit in range(x + 1, 10):
        if first_digit == 8:
            # For the last combination (89), print without a comma and space
            print(f"{x}{y}")
            break
        # Print other combinations with a comma and space
        print(f"{x}{y}", end=", ")
