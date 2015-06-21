import os
import re
from datetime import *
import feedparser
from newspaper import Article,Config

feeds = {
    'zh':[
        'http://feed.cnblogs.com/blog/u/50245/rss',
    ],
    'devops': [
        'http://devops.com/feed/',
        'http://dzone.com/mz/devops/rss',
        'http://www.planetdevops.net/?feed=rss2',
        'http://devops.linuxjournal.com/rss.xml',
        'http://martinfowler.com/bliki/bliki.atom',
        'http://blog.devopsguys.com/feed/',
    ],
    'ciandcd': [
        'http://continuousdelivery.com/feed/',
        'http://developer-blog.cloudbees.com/feeds/posts/default',
    ],
    'scm':[
        'https://github.com/blog.atom',
        'http://blog.boxedice.com/feed/',
        'http://www.perforce.com/blog/rss.xml',
        'https://www.gitlab.com/atom.xml',
    ],
}

outputDir = 'content'
max_entries = 20
max_days = 3

config = Config()
config.memoize_articles = True
config.fetch_images = False
config.request_timeout = 60
config.number_threads = 20
config.keep_article_html = True
config.language = 'en'

def writeFile(outPath,content):
    file = open(outPath, 'w')
    if file:
        file.write(content)
        file.close()
    else:
        print ("Error Opening File " + outPath)

def writeHtml(outPath,content,title):
    html = '''<!DOCTYPE html>
    <html lang="zh-cn">
    <head>
    <meta charset="utf-8"/>
    <title>
    '''
    html = html + title + '</title></head><body>'
    html = html + content + '</body></html>'
    writeFile(outPath,html)

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
            try:
                a = Article(entry.link,config=config, keep_article_html=True)
                a.download()
                a.parse()
                title = re.sub(' ','_',entry.title)
                outFileDir = outputDir + os.sep + 'category' + os.sep + category + os.sep
                if not os.path.exists(outFileDir):
                    os.makedirs(outFileDir)
                outPath = outFileDir + title + '.html'
                content = a.text
                content_html = a.article_html
                if(content_html):
                    writeHtml(outPath,content_html,entry.title)
                elif(content):
                    writeHtml(outPath,content,entry.title)
                else:
                    print('Error:cannot find content')
            except:
                continue




