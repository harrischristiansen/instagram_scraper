''' Instagram Scraper
@Harris Christiansen (HarrisChristiansen.com)
@Mehak Vohra (watthemehak.com)
November 2016
'''
from bs4 import BeautifulSoup
import urllib2
import re

url = "http://www.pythonforbeginners.com"
html_content = urllib2.urlopen(url).read()

test_html = open('test_html.html', 'r')
html_content = test_html.read()

soup = BeautifulSoup(html_content, 'html.parser')
bios = soup.findAll("div", { "class" : "uLBox-bio" })

emails = []

for bio in bios:
	match = re.search(r'[\w\.-]+@[\w\.-]+', str(bio))
	email = match.group(0)
	emails.append(email)

print(emails)