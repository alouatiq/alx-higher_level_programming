#!/usr/bin/python3
if __name__ == "__main__":
    import sys  # Import sys to access command-line arguments

    # Initialize the total sum to 0
    total_sum = 0

    # Iterate over all command-line arguments starting from index 1 (ignoring the script name)
    for arg in sys.argv[1:]:
        total_sum += int(arg)  # Convert each argument to an integer and add to the total sum

    # Print the total sum
    print(total_sum)
