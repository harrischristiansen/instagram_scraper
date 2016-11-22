''' Instagram Scraper
@Harris Christiansen (HarrisChristiansen.com)
November 2016
'''
from bs4 import BeautifulSoup
import urllib2

url = "http://www.pythonforbeginners.com"
html_content = urllib2.urlopen(url).read()

soup = BeautifulSoup(html_content, 'html.parser')
print soup.prettify()
