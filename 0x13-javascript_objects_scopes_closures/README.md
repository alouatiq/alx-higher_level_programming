# 0x13. JavaScript - Objects, Scopes and Closures

## Description
This repository contains solutions to the project **0x13. JavaScript - Objects, Scopes and Closures**. The project focuses on JavaScript concepts such as objects, prototypes, closures, inheritance, and scopes. Each task is implemented in a separate file.

## Learning Objectives
At the end of this project, you should be able to explain:
- Why JavaScript programming is amazing
- How to create an object in JavaScript
- The meaning of `this` in different contexts
- The concept of `undefined`
- The importance of variable types and scope
- What closures are
- How prototypes work
- How to inherit from another object

## Requirements
- All scripts are interpreted on Ubuntu 20.04 LTS using Node.js (version 14.x).
- Each file begins with the line `#!/usr/bin/node`.
- Code follows the Semistandard style guide.
- No use of `var`; only `const` or `let`.
- Files are executable.

## Installation
To run the scripts, ensure Node.js is installed:

```bash
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```
Install Semistandard globally:

```bash
$ sudo npm install semistandard --global
```

## Files

| File Name           | Description                                     |
|---------------------|-------------------------------------------------|
| `0-rectangle.js`    | Defines an empty `Rectangle` class.            |
| `1-rectangle.js`    | Adds a constructor for `Rectangle`.            |
| `2-rectangle.js`    | Validates width and height in the constructor. |
| `3-rectangle.js`    | Adds a `print()` method to display the rectangle. |
| `4-rectangle.js`    | Adds `rotate()` and `double()` methods.         |
| `5-square.js`       | Defines a `Square` class inheriting `Rectangle`. |
| `6-square.js`       | Adds a `charPrint(c)` method to `Square`.       |
| `7-occurrences.js`  | Returns the number of occurrences in a list.   |
| `8-esrever.js`      | Reverses a list without using `.reverse()`.    |
| `9-logme.js`        | Logs the count and value of arguments.         |
| `10-converter.js`   | Converts numbers between bases.                |
| `100-map.js`        | Maps values by their index.                    |
| `101-sorted.js`     | Groups user IDs by occurrences.                |
| `102-concat.js`     | Concatenates two files into one.               |

## Usage
Each file is executable and can be run using Node.js:

```bash
$ ./<filename>
```

Example:

```bash
$ ./3-rectangle.js
XX
XX
XX
```

## Author
Hassan Al Ouatiq
