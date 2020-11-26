import string
from lxml import html
import requests
import random

while True:
  word = ''.join(random.choice(string.ascii_uppercase) for _ in range(4))
  page = requests.post('https://www.gamertagavailability.com/check.php', data={'Gamertag': word, 'Language': 'English'})
  tree = html.fromstring(page.content)
  available = tree.xpath('.//div[@id="yres"]')
  if available:
    print(word)
  else:
    print('.')