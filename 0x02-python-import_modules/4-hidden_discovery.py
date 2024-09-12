#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4  # Import the hidden_4 module

    # Get all names defined by the module using dir()
    names = dir(hidden_4)

    # Filter out names starting with '__'
    filtered_names = [name for name in names if not name.startswith("__")]

    # Sort the names in alphabetical order and print each one
    for name in sorted(filtered_names):
        print(name)
