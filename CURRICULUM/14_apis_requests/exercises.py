# Exercise 14: APIs & Requests
# Run this script with: python exercises.py

import urllib.request
import json

# We will use the JSONPlaceholder API, a free public fake API for testing.
URL = "https://jsonplaceholder.typicode.com/posts/1"

# TODO: Exercise 1
# Write a function named 'fetch_post' that makes a GET request to the URL using urllib.
# The function should return the dictionary loaded from the JSON response.
# Handle potential errors and return None if the request fails.

def fetch_post():
    # Write your code here
    return None

# Test your function:
post = fetch_post()
if post:
    print("Post fetched successfully!")
    print(f"Title: {post.get('title')}")
else:
    print("Failed to fetch post.")


# TODO: Exercise 2
# Write code to parse and print the 'body' of the post in upper-case.

