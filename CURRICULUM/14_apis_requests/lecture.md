# Lecture 14: APIs & Requests

An **Application Programming Interface (API)** allows different software applications to communicate with each other over the web. Most web APIs use the HTTP protocol and exchange data in the **JSON** format.

---

## 1. How Web APIs Work
When you make a request to a web server (like typing a URL into a browser), the server responds.
- **Client**: Your program making the request.
- **Server**: The remote computer listening for requests and returning responses.
- **HTTP Methods**:
  - `GET`: Retrieve data from the server.
  - `POST`: Send new data to the server.
  - `PUT`/`PATCH`: Update existing data on the server.
  - `DELETE`: Remove data from the server.
- **Status Codes**:
  - `200 OK`: Request succeeded.
  - `201 Created`: Resource successfully created.
  - `400 Bad Request`: The server could not understand the request.
  - `404 Not Found`: The requested resource does not exist.
  - `500 Internal Server Error`: The server encountered an error.

---

## 2. Using the `requests` Library (Third-Party)
The most popular way to make HTTP requests in Python is the `requests` library. First, install it:
```bash
pip install requests
```

### Making a GET Request:
```python
import requests

response = requests.get("https://api.github.com/users/octocat")

# Check status code
if response.status_code == 200:
    # Parse JSON response
    data = response.json()
    print(data["name"])      # Output: The Octocat
    print(data["company"])   # Output: GitHub
else:
    print(f"Failed to fetch data: {response.status_code}")
```

---

## 3. Using the Standard Library (`urllib.request`)
If you want to make requests without installing third-party libraries, you can use Python's built-in `urllib` module:

```python
import urllib.request
import json

url = "https://api.github.com/users/octocat"
# Add a User-Agent header so GitHub doesn't block the request
req = urllib.request.Request(url, headers={'User-Agent': 'Python Study Client'})

try:
    with urllib.request.urlopen(req) as response:
        if response.status == 200:
            raw_data = response.read()
            data = json.loads(raw_data.decode("utf-8"))
            print(data["name"])
except Exception as e:
    print(f"Error occurred: {e}")
```

---

## 🧠 Try It Yourself
1. Use the public API `https://jsonplaceholder.typicode.com/todos/1` to fetch a sample todo item and print its title.
2. Experiment with handling exceptions in case the API endpoint is down or returning a 404 status.
