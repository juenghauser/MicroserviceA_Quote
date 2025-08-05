import requests
import json

BASE_URL = "http://localhost:7005"

def print_json(response):
    print(json.dumps(response, ensure_ascii=False, indent=2))

def test_random_quote():
    res = requests.get(f"{BASE_URL}/quote")
    print("Random Quote:")
    print_json(res.json())

def test_author_quote(author):
    res = requests.get(f"{BASE_URL}/quote", params={"author": author})
    if res.status_code == 200:
        print(f"Random Quote by {author}:")
        print_json(res.json())
    else:
        print(f"Error: {res.json()['message']}")

def test_all_quotes():
    res = requests.get(f"{BASE_URL}/quotes")
    data = res.json()
    print(f"All Quotes ({len(data)} total):")
    for q in data:
        print("-", f"{q['quote']} — {q['author']}")

if __name__ == "__main__":
    test_random_quote()
    test_author_quote("Michael Margolis")
    test_author_quote("Unknown Author")
    test_all_quotes()
