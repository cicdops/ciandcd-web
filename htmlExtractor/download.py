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
parser.add_option("-c", "--category", dest="category" )
(options, args) = parser.parse_args()
print (options.url)
print (options.category)
print (args)

print('download link:' + options.url)
download_file(options.url,config,outputDir,options.category,'')

