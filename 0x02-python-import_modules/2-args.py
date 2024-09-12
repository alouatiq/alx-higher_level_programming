#!/usr/bin/python3
if __name__ == "__main__":
    import sys  # Import sys to access command-line arguments

    # Initialize total sum to 0
    total_sum = 0

    # Iterate over command-line arguments starting from index 1 (skipping the script name)
    for arg in sys.argv[1:]:
        total_sum += int(arg)  # Convert each argument to an integer and add to total_sum

    # Print the total sum followed by a new line
    print(total_sum)
