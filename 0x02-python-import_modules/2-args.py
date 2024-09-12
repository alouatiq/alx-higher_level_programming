#!/usr/bin/python3
if __name__ == "__main__":
    import sys  # Importing sys to access command-line arguments

    argv = sys.argv  # List of command-line arguments
    arg_count = len(argv) - 1  # Number of arguments (excluding script name)

    if arg_count == 0:
        # If no arguments, print '0 arguments.'
        print("0 arguments.")
    elif arg_count == 1:
        # If one argument, print '1 argument:'
        print("1 argument:")
    else:
        # If more than one argument, print '<n> arguments:'
        print(f"{arg_count} arguments:")

    # Print each argument with its position (starting at 1)
    for i in range(1, len(argv)):
        print(f"{i}: {argv[i]}")
