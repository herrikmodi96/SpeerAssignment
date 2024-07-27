# Wikipedia Link Scraper

This script scrapes Wikipedia links from a given Wikipedia page, following links up to a specified number of cycles, and saves the results to a JSON file.

## Features

Validates the input Wikipedia link.
Accepts an integer between 1 and 3 to determine the number of scraping cycles.
Scrapes the first 10 unique Wikipedia links from each page.
Avoids revisiting previously visited links.
Saves all found unique links to a JSON file.

## Requirements

Python 3.x
requests library
beautifulsoup4 library

## Installation

1. Clone the repository or download the script file.

2. Install the required libraries using pip:

## Usage

1. Run the Script- Python3 wiki_scraper.py
2. Enter valid Wikipedia link (e.g. https://en.wikipedia.org/wiki/Lionel_Messi)
3. Enter a valid integer between 1 and 3 for the number of cycles
4. The script will scrape the Wikipedia page and save the found links to links.json.

## Output

The script generates a wiki_links.json file containing all unique found links.

Unique links in wiki_links.json (example preview of links):
      "https://en.wikipedia.org/wiki/Argentina_national_football_team"
      "https://en.wikipedia.org/wiki/Glossary_of_association_football_terms#O"
      "https://en.wikipedia.org/wiki/Messi_(disambiguation)"
      "https://en.wikipedia.org/wiki/Defender_(association_football)"
      "https://en.wikipedia.org/wiki/English_language"
      "https://en.wikipedia.org/wiki/Association_football"
      "https://en.wikipedia.org/wiki/Messi_Bouli"
      "https://en.wikipedia.org/wiki/Free_content"
      "https://en.wikipedia.org/wiki/Argentine_Football_Association"
      "https://en.wikipedia.org/wiki/2022_FIFA_World_Cup"

  - All found links: 70, unique count: 35
   
