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

def cleanup_excerpt(filename):
    post = frontmatter.load(filename)
    soup = BeautifulSoup(post['excerpt'], 'html.parser')

    image = soup.find('img')
    if image:
        post['featured-image'] = image.get('src')

    post['excerpt'] = soup.get_text()
    with open(filename, mode='w', encoding="utf-8") as f:
        text = frontmatter.dumps(post)
        #print (text)
        f.write(text)


for filename in glob.glob(os.path.join(path, '*.md')):
    cleanup_excerpt(filename)


# post = frontmatter.load('_posts/2011-05-08-workshop-brno.md')
# stripped = cleanhtml(post['excerpt'])
# soup = BeautifulSoup(post['excerpt'], 'html.parser')

# print (soup.get_text())