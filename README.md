Wikipedia Link Scraper

This script scrapes Wikipedia links from a given Wikipedia page, following links up to a specified number of cycles, and saves the results to a JSON file.

Features
Validates the input Wikipedia link.
Accepts an integer between 1 and 3 to determine the number of scraping cycles.
Scrapes the first 10 unique Wikipedia links from each page.
Avoids revisiting previously visited links.
Saves all found unique links to a JSON file.
