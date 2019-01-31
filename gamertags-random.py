import string
from lxml import html
import requests
import random

while True:
  word = ''.join(random.choice(string.ascii_uppercase) for _ in range(4))
  page = requests.post('https://www.gamertag.net/check.php', data={'tag': word})
  tree = html.fromstring(page.content)
  available = tree.xpath('.//div[@class="available"]')
  if available:
    print word
  else:
    print '.'