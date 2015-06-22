import os
import re
from datetime import *
import feedparser
from newspaper import Article,Config

feeds = {
    '中文':[
        'http://feed.cnblogs.com/blog/u/50245/rss',
    ],
    'devops': [
        'http://devops.com/feed/',
        'http://dzone.com/mz/devops/rss',
        'http://www.planetdevops.net/?feed=rss2',
        'http://devops.linuxjournal.com/rss.xml',
        'http://blog.devopsguys.com/feed/',
    ],
    'ciandcd': [
        'http://continuousdelivery.com/feed/',
        'http://developer-blog.cloudbees.com/feeds/posts/default',
        'https://jazzweb1.torolab.ibm.com/blog/index.php/feed',
        'https://jazzweb1.torolab.ibm.com/pub/planet/feed.rss',
        'http://www.go.cd/feed/rss.xml',
        'http://openbuildservice.org/blog/',
        'http://feeds.feedburner.com/AtlassianChina',
        'http://blog.jetbrains.com/feed/',
        'http://www.pmease.com/rss/hotnews',
        'https://www.finalbuilder.com/DesktopModules/LiveBlog/Handlers/Syndication.ashx?mid=632&PortalId=0&tid=181&ItemCount=20',
    ],
    'scm':[
        'https://github.com/blog.atom',
        'http://blog.boxedice.com/feed/',
        'http://www.perforce.com/blog/rss.xml',
        'https://www.gitlab.com/atom.xml',
    ],
}

outputDir = 'content' + os.sep + 'category'
max_entries = 20
max_days = 10

config = Config()
config.memoize_articles = False
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

def writeHtml(outPath,content,title,link,date):
    html = '''<!DOCTYPE html>
    <html lang="zh-cn">
    <head>
    <meta charset="utf-8"/>
    <title>
    '''
    if(isinstance(date,datetime)):
        date = date.strftime('%Y-%m-%d %H:%M')
    html = html + '<meta name="date" content="' + date + '"/>'
    html = html + title + '</title></head><body>'
    html = html + 'from:' + link + '<br>'
    html = html + content + '</body></html>'
    writeFile(outPath,html)
    print("save to:" + outPath)

def download_file(link,title,config,outputDir,category,date):
    try:
        a = Article(link,config=config, keep_article_html=True)
        a.download()
        a.parse()

        title2 = re.sub(' ','_',title)
        outFileDir = outputDir + os.sep + category + os.sep
        if not os.path.exists(outFileDir):
            os.makedirs(outFileDir)
        outPath = outFileDir + title2 + '.html'

        content = a.text
        content_html = a.article_html

        date2 = ''
        try:
            date2 = a.publish_date
        except Exception as e:
            print(e)
        if(date2):
            date = date2

        if(content_html):
            writeHtml(outPath,content_html,title,link,date)
        elif(content):
            writeHtml(outPath,content,title,link,date)
        else:
            print('Error:cannot find content')
    except Exception as e:
        print('Exception:' + link)
        print(e)
        return 0
    return 1

#download_file('http://www.cnblogs.com/itech/p/4572275.html','SSH反向连接及Autossh',config,outputDir,'中文')
#exit();

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
