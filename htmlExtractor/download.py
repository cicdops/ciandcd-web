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
(options, args) = parser.parse_args()
url = options.url
url_type = options.type #type
category = options.category
print (url)
print (url_type)
print (category)
print (args)

if url and url_type == 'article':
    downloadFile(options.url,config,outputDir,options.category,'')
elif url and url_type == 'feed':
    downloadFeed(options.url,config,outputDir,options.category,'',max_number)
elif url and url_type == 'articles':
    downloadArticles(options.url,config,outputDir,options.category,max_number)
else:
    downloadByConfig(urls,config,outputDir,max_number)
