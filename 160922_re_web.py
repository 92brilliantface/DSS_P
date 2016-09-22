import os
import re

# 현재 디렉토리


webs = ['http://www.test.com', 
        'https://www.test1.com', 
        'http://www.test.com', 
        'ftp://www.test.com', 
        'http:://www.test.com',
       'htp://www.test.com',
       'http://www.google.com', 
       'https://www.homepage.com']

class website(object):
    def __init__(self, sitelist):
        self.sitelist = sitelist
    def correct(self):
        #웹 주소 정규표현식
        site_re = re.compile(r'^http\w*://\w+.\w+.\w+')
        list = []
        for site in self.sitelist:
            if site_re.findall(site) != []:
                list += site_re.findall(site)
        return list
    def _print_(self):
        print self.correct()
        return 0

urls = website(webs)

with open('urls.txt', 'w') as text:
    for url in urls.correct():
        text.write(url+"\n")
    