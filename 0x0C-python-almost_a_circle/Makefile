# Variables
PYTHON = python3
PYCODSTYLE = pycodestyle

# Directories and files
TEST_DIR = tests
MAIN_FILES = 0-main.py 1-main.py 2-main.py 3-main.py 4-main.py 5-main.py 6-main.py 7-main.py 8-main.py 9-main.py \
             10-main.py 11-main.py 12-main.py 13-main.py 14-main.py 15-main.py

# Default rule
all: test

# Rule to run all unit tests
test:
	@$(PYTHON) -m unittest discover $(TEST_DIR)

# Rule to run specific main test files
run_main: $(MAIN_FILES)
	@echo "Running all main test files..."
	@for file in $(MAIN_FILES); do \
		echo "Running $$file..."; \
		$(PYTHON) $$file || exit 1; \
	done

# Rule to check PEP8 compliance
pep8:
	@echo "Checking PEP8 compliance..."
	@$(PYCODSTYLE) *.py models/*.py $(TEST_DIR)/test_models/*.py || exit 1

# Rule to clean up __pycache__ and .pyc files
clean:
	@echo "Cleaning up..."
	@find . -type d -name "__pycache__" -exec rm -r {} +
	@find . -type f -name "*.pyc" -exec rm -r {} +

# Rule to test, run main files, check PEP8, and clean up
full: test run_main pep8 clean

# Phony targets to avoid conflicts with files
.PHONY: all test run_main pep8 clean full
