''' Instagram Scraper
@Harris Christiansen (HarrisChristiansen.com)
@Mehak Vohra (watthemehak.com)
November 2016
'''
from bs4 import BeautifulSoup
import urllib2
import mechanize
import Cookie
import cookielib
import re

url = 'https://dashboard.audiense.com/?email=watthemehak%40gmail.com&_ga=1.246766148.1374939999.1479356195#!272441706/self//search/{"ub":9,"a":"Youtuber","b":"@gmail.com","p":"1","i":"2","ge":"F","e_t":"P","f_f":1000,"f_t":50000,"fi_f":150,"fi_t":20000}'
br = mechanize.Browser
html_content = urllib2.urlopen(url).read()

cookiejar =cookielib.LWPCookieJar()

br.set_cookiejar(cookiejar)
cookie = cookielib.Cookie(version=0, name='Name', value='1', port=None, port_specified=False, domain='www.example.com', domain_specified=False, domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=None, discard=True, comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False)
cookiejar.set_cookie(cookie)
for index, cookie in enumerate(cookiejarj):
    print index, ' : ', cookie



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