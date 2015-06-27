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
parser.add_option("-c", "--category", dest="category" )
parser.add_option("-r", "--regex", dest="regex_for_links" )
(options, args) = parser.parse_args()
url = options.url
url_type = options.type #type
category = options.category
regex_for_links = options.regex_for_links
print (url)
print (url_type)
print (category)
print (regex_for_links)
print (args)

if url and url_type == 'article':
    downloadFile(options.url,config,outputDir,options.category,'')
elif url and url_type == 'feed':
    downloadFeed(options.url,config,outputDir,options.category,'',max_number)
elif url and url_type == 'articles':
    downloadArticles(options.url,options.category,config,outputDir,max_number,regex_for_links)
else:
    downloadByConfig(urls,config,outputDir,max_number)
