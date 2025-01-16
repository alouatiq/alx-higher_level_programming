# 0x10. Python - Network #0

This repository contains scripts and a Python function to practice working with HTTP requests using `curl` and Python. Each task focuses on a different aspect of network programming and HTTP protocols.

## Learning Objectives

By completing this project, you should be able to:

- Understand URLs and their components (scheme, domain, port, query string, etc.)
- Make HTTP requests using `curl`
- Understand HTTP request methods (GET, POST, DELETE, etc.)
- Handle HTTP response codes and headers
- Work with HTTP cookies
- Parse and process JSON responses

## Requirements

- All Bash scripts must be exactly 3 lines long.
- Scripts must be executable.
- Python scripts must conform to PEP 8 style.
- All `curl` commands must use the `-s` flag (silent mode).
- All tasks are tested on Ubuntu 20.04 LTS.

---

## Files and Descriptions

### **Bash Scripts**

1. **`0-body_size.sh`**
   - Displays the size of the body of the HTTP response in bytes.

2. **`1-body.sh`**
   - Sends a GET request to a URL and displays the body of the response (only if the status code is 200).

3. **`2-delete.sh`**
   - Sends a DELETE request to a URL and displays the body of the response.

4. **`3-methods.sh`**
   - Displays all HTTP methods the server accepts for a given URL.

5. **`4-header.sh`**
   - Sends a GET request with a custom header (`X-School-User-Id: 98`).

6. **`5-post_params.sh`**
   - Sends a POST request with specific parameters (email and subject) and displays the response body.

7. **`100-status_code.sh`**
   - Displays only the status code of the HTTP response.

8. **`101-post_json.sh`**
   - Sends a JSON POST request to a URL with the contents of a file as the request body.

9. **`102-catch_me.sh`**
   - Sends a request to `0.0.0.0:5000/catch_me` to get the response `You got me!`.

---

### **Python Script**

1. **`6-peak.py`**
   - Contains a function `find_peak(list_of_integers)` that finds a peak in a list of unsorted integers.
   - Time complexity: `O(log(n))`.

---

## Usage

1. Make all scripts executable:
   ```bash
   chmod +x *.sh
   ```

2. Run a script:
   ```bash
   ./script_name.sh [arguments]
   ```

3. Run the Python script:
   ```bash
   ./6-peak.py
   ```

---

## Repository Structure

```
.
├── 0-body_size.sh
├── 1-body.sh
├── 2-delete.sh
├── 3-methods.sh
├── 4-header.sh
├── 5-post_params.sh
├── 6-peak.py
├── 6-peak.txt
├── 100-status_code.sh
├── 101-post_json.sh
├── 102-catch_me.sh
├── README.md
```

---

## Author

Hassan Al Ouatiq
