import requests
from bs4 import BeautifulSoup
import json
import re

def is_wiki_link(url):
    # Regular expression to check if the URL is a valid Wikipedia link
    pattern = r'^https://en\.wikipedia\.org/wiki/'
    return re.match(pattern, url) is not None

def get_links(url, n): # e.g. url https://en.wikipedia.org/wiki/Calgary
    visited = set()
    to_visit = [url]
    all_links = []

    for _ in range(n):
        new_links = []
        for link in to_visit:
            if link not in visited:
                visited.add(link)
                try:
                    page = requests.get(link)
                    page.raise_for_status()  
                    soup = BeautifulSoup(page.content, 'html.parser')
                    links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith('/wiki/') and ':' not in a['href']]
                    links = ['https://en.wikipedia.org' + l for l in links]
                    new_links.extend(links[:10])
                except requests.RequestException as e:
                    print(f"Failed to fetch {link}: {e}")
        all_links.extend(new_links)
        to_visit = new_links

    return all_links

def main():
    url = input("Enter a Wikipedia link: ")
    if not is_wiki_link(url):
        raise ValueError("The link is not a valid Wikipedia link.")
    try:
        n = int(input("Enter a valid integer between 1 to 3: "))
        if n < 1 or n > 3:
            raise ValueError("The integer is not valid. It should be between 1 to 3.")
    except ValueError as ve:
        raise ValueError("Invalid input for number of cycles.") from ve

    links = get_links(url, n)
    unique_links = list(set(links))

    with open('wiki_links.json', 'w') as f:
        for link in unique_links:
            f.write(json.dumps(link) + '\n')

    print(f"All found links: {len(links)}, unique count: {len(unique_links)}")

if __name__ == "__main__":
    main()
