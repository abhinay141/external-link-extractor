from lxml import html
import requests
url = input()
link = requests.get(url)
ht = html.fromstring(link.content)
all_links = ht.xpath('//a/@href')
print(all_links)


                     



