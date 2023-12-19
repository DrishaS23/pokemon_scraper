import requests
import lxml.html
import csv

tree = lxml.html.fromstring(requests.get('https://scrapeme.live/product-category/pokemon/'))

with open('pokemon_character.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['SKU', 'Categories', 'Tags'])


    for character in tree.xpath('/html/body/div/form/div/div[contains(@class, "members")]/div[contains(@class, "featured-boxes")]');
    