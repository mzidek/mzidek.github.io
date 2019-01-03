# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 14:36:40 2019

@author: mzidek2
"""

import frontmatter
import xml
import re

def remove_tags(text):
    return ''.join(xml.etree.ElementTree.fromstring(text).itertext())

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

post = frontmatter.load('posts/2011-05-08-workshop-brno.markdown')
stripped = cleanhtml(post['excerpt'])

print (stripped)