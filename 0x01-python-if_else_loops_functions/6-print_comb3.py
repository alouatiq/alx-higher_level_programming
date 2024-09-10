#!/usr/bin/python3
for x in range(9):
    for y in range(x + 1, 10):
        if x == 8:
            # For the last combination (89), print without a comma and space
            print(f"{x}{y}")
            break
        # Print other combinations with a comma and space
        print(f"{x}{y}", end=", ")
