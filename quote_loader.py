import re

def load_quotes(filename="Quotes.txt"):
    quotes = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("List of Quotes:"):
                continue
            match = re.match(r"“(.+?)”\s+—\s+(.+)", line)
            if match:
                quote, author = match.groups()
                author = author.replace('\u202f', ' ').strip()
                quotes.append({
                    "quote": quote.strip(),
                    "author": author.strip()
                })
    return quotes
