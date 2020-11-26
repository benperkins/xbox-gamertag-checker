import string
from lxml import html
import requests

letters = list(string.ascii_lowercase)

letters.extend([
  i+b+c+d
  for i in letters
  for b in letters
  for c in letters
  for d in letters
])

for word in letters:
  if len(word) > 2:
    page = requests.post('https://www.gamertagavailability.com/check.php', data={'Gamertag': word, 'Language': 'English'})
    tree = html.fromstring(page.content)
    available = tree.xpath('.//div[@id="yres"]')
    if available:
      print(word)
    else:
      print('.')
