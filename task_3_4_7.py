import requests as req
import re

A = 'https://en.wikipedia.org/wiki/Main_Page'  # input()
# A = 'https://stepic.org/media/attachments/lesson/24472/sample0.html'  # input()
# B = 'https://stepic.org/media/attachments/lesson/24472/sample2.html'  # input()

def extract_domain(link):
    if link.startswith('./') or link.startswith('../') or link.startswith('#'):
        return None
    return re.findall(r'([\w]+://)*([^ /:]+):?([^?\s]*)(\?[\S]*)?', link)[0][1]

def extract(text):
    raw_domains = [extract_domain(tup[1]) for tup in re.findall(r'<a .*href ?= ?([\'"])([^>\s]+)(\1).*>', text)]
    domains = [domain for domain in raw_domains if domain is not None]
    print("\n".join(sorted(set(domains))))


def process(link):
    try:
        res = req.get(link)
        text = res.text
        extract(text)
    except:
        pass

extract(
    """
<h4 class="lightGreen mBottom4"><a href="http://www.nashidengi.ru">"РќР°С€Рё РґРµРЅСЊРіРё"</a></h4>
    """
)


process('https://stepic.org/media/attachments/lesson/24471/03﻿')
#
# print(extract_domain('http://stepic.org/courses'))
# print(extract_domain('https://stepic.org'))
# print(extract_domain('http://neerc.ifmo.ru:1345'))
# print(extract_domain('ftp://mail.ru/distib'))
# print(extract_domain('ya.ru'))
# print(extract_domain('www.ya.ru'))
# print(extract_domain('../skip_relative_links'))
