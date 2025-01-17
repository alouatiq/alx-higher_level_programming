# 0x11. Python - Network #1

This project focuses on using Python to interact with network resources through libraries like `urllib` and `requests`. It covers fetching and manipulating internet data, handling HTTP methods, and working with APIs.

---

## Learning Objectives

By completing this project, you should understand:

- How to fetch internet resources using the Python `urllib` package.
- How to decode responses from `urllib`.
- How to use the `requests` package for simpler HTTP interactions.
- How to make HTTP GET, POST, PUT, and DELETE requests.
- How to handle JSON responses and manipulate data from external services.
- Error handling for HTTP requests.

---

## Requirements

- All scripts are written for Ubuntu 20.04 LTS using Python 3.8.5.
- All files must end with a new line.
- Python scripts must begin with:
  ```python
  #!/usr/bin/python3
  ```
- All code should follow `pycodestyle` (v2.8.*).
- Documentation is mandatory for all modules, classes, and functions.
- Use `with` statements for resource management.

---

## Tasks and Descriptions

### **Mandatory Tasks**

1. **`0-hbtn_status.py`**
   - Fetches `https://alx-intranet.hbtn.io/status` using `urllib`.
   - Displays the response body type, content, and decoded content.

2. **`1-hbtn_header.py`**
   - Sends a request to a URL and displays the `X-Request-Id` variable from the response header.
   - Uses `urllib` and `sys`.

3. **`2-post_email.py`**
   - Sends a POST request to a URL with an email as a parameter and displays the response body.
   - Uses `urllib` and `sys`.

4. **`3-error_code.py`**
   - Sends a request to a URL and displays the response body.
   - Handles HTTP errors (e.g., 404, 500) and prints `Error code: <status>`.
   - Uses `urllib` and `sys`.

5. **`4-hbtn_status.py`**
   - Fetches `https://alx-intranet.hbtn.io/status` using `requests`.
   - Displays the response body type and content.

6. **`5-hbtn_header.py`**
   - Sends a request to a URL and displays the `X-Request-Id` from the response header.
   - Uses `requests` and `sys`.

7. **`6-post_email.py`**
   - Sends a POST request to a URL with an email as a parameter and displays the response body.
   - Uses `requests` and `sys`.

8. **`7-error_code.py`**
   - Sends a request to a URL and displays the response body.
   - Handles HTTP errors by printing `Error code: <status>` if the status code is 400 or higher.
   - Uses `requests` and `sys`.

9. **`8-json_api.py`**
   - Sends a POST request to a URL with a letter as a parameter (`q`).
   - Displays `[<id>] <name>` if the response contains valid JSON with `id` and `name` fields.
   - Handles invalid JSON or empty results.
   - Uses `requests` and `sys`.

10. **`10-my_github.py`**
    - Takes GitHub credentials (username and personal access token) and uses the GitHub API to display the user ID.
    - Uses Basic Authentication.
    - Uses `requests` and `sys`.

### **Advanced Task**

11. **`100-github_commits.py`**
    - Fetches the 10 most recent commits from a specified GitHub repository and user.
    - Displays each commit as `<sha>: <author name>`.
    - Handles GitHub API rate limits for unauthenticated requests.
    - Uses `requests` and `sys`.

---

## Repository Structure

```
.
├── 0-hbtn_status.py
├── 1-hbtn_header.py
├── 2-post_email.py
├── 3-error_code.py
├── 4-hbtn_status.py
├── 5-hbtn_header.py
├── 6-post_email.py
├── 7-error_code.py
├── 8-json_api.py
├── 10-my_github.py
├── 100-github_commits.py
├── README.md
```

---

## Usage

1. Make all scripts executable:
   ```bash
   chmod +x *.py
   ```

2. Run a script:
   ```bash
   ./script_name.py [arguments]
   ```

---

## Author

Hassan Al Ouatiq
