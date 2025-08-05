# Quote Microservice A

## Overview

This microservice provides motivational and inspirational quotes over a REST API.  
It supports retrieving a random quote, filtering quotes by author, and returning the full list of stored quotes.

---

## Communication Contract

### Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/quote` | Returns a random quote |
| GET | `/quote?author={author}` | Returns a random quote by the specified author (case-insensitive) |
| GET | `/quotes` | Returns all quotes and authors as a JSON array |

---

## How to Request Data from this Microservice

You can access the microservice using an HTTP GET request from any language or platform that supports web requests.

Assuming the microservice is running locally on port `7005`, here are example requests:

```python
import requests

# Get a random quote
res1 = requests.get("http://localhost:7005/quote")
print(res1.json())

# Get a quote by a specific author
res2 = requests.get("http://localhost:7005/quote?author=Michael Margolis")
print(res2.json())

# Get all quotes
res3 = requests.get("http://localhost:7005/quotes")
print(res3.json())

```

## How to Receive Data from this Microservice

All responses are returned in JSON format. Any coding language can be used so long as it is parsed from the JSON tree.

Example: Random Quote Response

{
  "quote": "If you want to change the world, change your story.",
  "author": "Michael Margolis"
}

Example: All Quotes Response

[
  {
    "quote": "We tell ourselves stories in order to live.",
    "author": "Joan Didion"
  },
  {
    "quote": "Stories have to be told or they die.",
    "author": "Sue Monk Kidd"
  }
  // More quotes...
]

Example: Author Not Found

{
  "success": false,
  "message": "No quotes found for author: Unknown Author"
}

![UML Sequence Diagram](uml_sequence.png)