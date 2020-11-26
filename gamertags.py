import string
from lxml import html
import requests
from os import listdir
from os.path import isfile, join
import csv

path = './words'
files = [f for f in listdir(path) if isfile(join(path, f))]

prev = ''

for file in files:
  with open(join(path, file)) as f:
    reader = csv.reader(x.replace('\0', '') for x in f)
    if reader:
      for r in reader:
        if len(r) > 0:
          word = r[0].replace(' ', '')
          if word != prev and len(word) > 2 and len(word) < 6:
            prev = word
            page = requests.post('https://www.gamertagavailability.com/check.php', data={'Gamertag': word, 'Language': 'English'})
            tree = html.fromstring(page.content)
            available = tree.xpath('.//div[@id="yres"]')
            if available:
              print(word)
            else:
              print('.')

print('Done...')
exit()
