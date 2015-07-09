import os
import re
from datetime import *
import feedparser
from newspaper import Article,Config
from HECommon import *
from HEConfig import *

from optparse import OptionParser
parser = OptionParser()
parser.add_option("-u", "--url", dest="url")
parser.add_option("-t", "--type", dest="type")
parser.add_option("-c", "--category", dest="category")
parser.add_option("-r", "--regex", dest="regex_for_links")
parser.add_option("-a", "--tags", dest="tags" )
parser.add_option("-f", "--force", dest="force")
(options, args) = parser.parse_args()
url = options.url
url_type = options.type #type
category = options.category
regex_for_links = options.regex_for_links
tags = options.tags
print (url)
print (url_type)
print (category)
print (regex_for_links)
print (tags)
print (args)

if url and url_type == 'article':
    downloadFile(url,category,config,outputDir,'',tags)
elif url and url_type == 'feed':
    downloadFeed(url,category,config,outputDir,'',max_number,tags)
elif url and url_type == 'articles':
    downloadArticles(url,category,config,outputDir,max_number,regex_for_links,tags)
else:
    downloadByConfig(urls,config,outputDir,max_number)
