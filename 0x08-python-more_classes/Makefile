# Makefile for testing Python files in 0x08-python-more_classes

# Python interpreter
PYTHON = python3

# List of Python files to make executable
PY_FILES = 0-rectangle.py 1-rectangle.py 2-rectangle.py 3-rectangle.py 4-rectangle.py \
           5-rectangle.py 6-rectangle.py 7-rectangle.py 8-rectangle.py 9-rectangle.py \
           101-nqueens.py tests/0-main.py tests/1-main.py tests/2-main.py \
           tests/3-main.py tests/4-main.py tests/5-main.py tests/6-main.py \
           tests/7-main.py tests/8-main.py tests/9-main.py tests/101-main.py

# List of test files inside the tests directory
TESTS = tests/0-main.py tests/1-main.py tests/2-main.py tests/3-main.py \
        tests/4-main.py tests/5-main.py tests/6-main.py tests/7-main.py \
        tests/8-main.py tests/9-main.py tests/101-main.py

# Default target to run all tests
all: make_executable $(TESTS)
	@echo "Running all tests..."
	@for test in $(TESTS); do \
		echo "Running $$test..."; \
		$(PYTHON) $$test || exit 1; \
		echo "----------------------"; \
	done
	@echo "All tests completed successfully!"

# Target to make Python scripts executable
make_executable:
	@echo "Making all Python files executable..."
	@chmod +x $(PY_FILES)
	@echo "All Python files are now executable!"

# Target to run a specific test (e.g., make test TEST=tests/1-main.py)
test:
	@if [ -z "$(TEST)" ]; then \
		echo "Please specify a test file using TEST=<path_to_test>"; \
	else \
		echo "Running $(TEST)..."; \
		$(PYTHON) $(TEST); \
		echo "Test completed!"; \
	fi

# Clean up any __pycache__ directories and .pyc files
clean:
	@echo "Cleaning up..."
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -name "*.pyc" -exec rm -f {} +
	@echo "Cleanup completed!"

# Help target to display available commands
help:
	@echo "Makefile commands:"
	@echo "  make                 - Make Python files executable and run all tests"
	@echo "  make make_executable - Make Python scripts executable"
	@echo "  make test            - Run a specific test file (e.g., make test TEST=tests/1-main.py)"
	@echo "  make clean           - Remove __pycache__ directories and .pyc files"
	@echo "  make help            - Display this help message"

.PHONY: all test clean help make_executable
