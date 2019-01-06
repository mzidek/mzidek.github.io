# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 14:36:40 2019

@author: mzidek2
"""

import frontmatter
import xml
import re
from bs4 import BeautifulSoup
import glob
import os

path = '_posts_'



def remove_tags(text):
    return ''.join(xml.etree.ElementTree.fromstring(text).itertext())

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

def cleanwidget(raw_html):
    cleanr = re.compile('[.*?]')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

def cleanup_excerpt(filename):
    print("Processing " + filename + "...", end='')
    post = frontmatter.load(filename)

    if not 'excerpt' in post.keys():
        return

    soup = BeautifulSoup(post['excerpt'], 'html.parser')

    image = soup.find('img')
    if image:
        post['featured-image'] = image.get('src')

    soup = BeautifulSoup(post.content, 'html.parser')

    for image in soup.find_all('img'):
        src_old = image['src']
        image['src'] = "{{ site.baseurl }}/" + src_old

    post.content = soup.prettify()
    post['excerpt'] = soup.get_text()
    post['excerpt'] = cleanwidget(post['excerpt'])
    with open(filename, mode='w', encoding="utf-8") as f:
        text = frontmatter.dumps(post)
        #print (text)
        f.write(text)
        print("DONE")


for filename in glob.glob(os.path.join(path, '*.md')):
    cleanup_excerpt(filename)


# post = frontmatter.load('_posts/2011-05-08-workshop-brno.md')
# stripped = cleanhtml(post['excerpt'])
# soup = BeautifulSoup(post['excerpt'], 'html.parser')

# print (soup.get_text())