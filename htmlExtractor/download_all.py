import os
import re
from datetime import *
import feedparser
from newspaper import Article,Config
from HEconfig import *
from HEcommon import *

for category in feeds.keys():
    print('category:' + category)
    fds = feeds[category]
    for feed in fds:
        print(feed)
        d = feedparser.parse(feed)
        for entry in d.entries[:max_entries]:
            print('entry:' + entry.title + ' ' + entry.link)
            #today = datetime.today()
            #days_ago = today - timedelta(days=max_days)
            #d = datetime(entry.published_parsed)
            #if(d < days_ago):
            #    continue
            date = ''
            try:
                date = entry.published
            except Exception as e:
                print(e)
            download_file(entry.link,entry.title,config,outputDir,category,date)
