import requests
from bs4 import BeautifulSoup
import pandas as pd

# Fetch the GraphLinq website
url = 'https://graphlinq.io'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# This will hold our extracted information
data = {'text': [], 'class': [], 'data-i18n': [], 'id': [], 'href': [], 'src': [], 'alt': [], 'title': [], 'style': [], 'role': [], 'aria': []}

# Iterate through all visible text elements
for tag in soup.find_all(text=True):
    if tag.parent.name not in ['script', 'meta', 'link', 'style', '[document]']:  # Exclude non-visible elements
        text = tag.strip()
        if text:  # If the text is not empty
            data['text'].append(text)
            data['class'].append(tag.parent.get('class'))
            data['data-i18n'].append(tag.parent.get('data-i18n'))
            data['id'].append(tag.parent.get('id'))
            data['href'].append(tag.parent.get('href'))
            data['src'].append(tag.parent.get('src'))
            data['alt'].append(tag.parent.get('alt'))
            data['title'].append(tag.parent.get('title'))
            data['style'].append(tag.parent.get('style'))
            data['role'].append(tag.parent.get('role'))
            data['aria'].append(tag.parent.get('aria-label'))

# Convert to DataFrame for easier manipulation and saving
df = pd.DataFrame(data)

# Save to local CSV
df.to_csv('graphlinq_landing.csv', index=False)

print("Data saved to 'graphlinq_landing.csv'")

