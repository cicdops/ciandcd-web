import os
import re
from datetime import *
import feedparser
from newspaper import Article,Config
import newspaper
import urllib.request

def writeFile(outPath,content):
    file = open(outPath, 'w')
    if file:
        file.write(content)
        file.close()
    else:
        print ("Error Opening File " + outPath)

def writeHtml(outPath,content,title,link,date,authors,tags):
    print('date:authors:tags' + date + authors + tags)
    html = '''<!DOCTYPE html>
    <html lang="zh-cn">
    <head>
    <meta charset="utf-8"/>
    <title>
    '''
    html = html + title + '</title>'

    if(isinstance(date,datetime)):
        date = date.strftime('%Y-%m-%d %H:%M')
    if date != '':
      html = html + '<meta name="date" content="' + date + '"/>'
    if authors != '':
        html = html + '<meta name="authors" content="' + authors + '" />'
    if tags != '':
        html = html + '<meta name="tags" content="' + tags + '" />'
    html = html + '</head><body>'
    html = html + 'From:<a href=' + link + '>' + link + '</a><br><br>'
    html = html + content + '</body></html>'
    force = 0
    if(force == 0):
        if os.path.exists(outPath):
            print("The file " + outPath + " is existed, will ignore.")
        else:
            writeFile(outPath,html)
            print("save to:" + outPath)
    else:
        writeFile(outPath,html)
        print("save to:" + outPath)

def getDomain(url):
  m = re.search(r'http[s]?://(.*?)/',url)
  if m:
     return m.group()
  else:
     return ''

def fixLinks(html,link):
  def f(m):
    return link + m.group(1)

  reobj = re.compile('href="(/.*?)"')
  new = reobj.sub(f,html)
  return new

def getLinks(url,regex):
    website = urllib.request.urlopen(url)
    html = website.read().decode('utf-8')
    regex_new = '"(' + regex + ')"'
    print('regex:' + regex_new)
    links = re.findall(regex_new, html)

    return list(set(links))

def downloadFile(link,category,config,outputDir,date,tags):
    print('download article from:' + link)
    try:
        try:
            a = Article(link,config=config, keep_article_html=True)
            a.download()
            a.parse()
        except Exception as e:
            print("Error for download and parser:" + link)
            print(e)
            return 0

        if a.title == '':
           print("cannot find title for " + link)
           return 0

        print('title:' + a.title)
        title2 = re.sub(' ','_',a.title)
        title2 = re.sub('/','_',title2)
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
            print("Warning:cannot find date")
        if(date2):
            date = date2

        authors = ','.join(a.authors)
        if(content_html):
            domain = getDomain(link)
            content_html = fixLinks(content_html,domain)
            writeHtml(outPath,content_html,a.title,link,date,authors,tags)
        elif(content):
            writeHtml(outPath,content,a.title,link,date,authors,tags)
        else:
            print('Error:cannot find content')
    except Exception as e:
        print('Exception:' + link)
        print(e)
        return 0
    return 1

def downloadArticles(url,category,config,outputDir,max_number,regex_for_links,tags):
    print('download from articles:' + url)
    all = getLinks(url,regex_for_links)
    for article in all[:max_number]:
        downloadFile(article,category,config,outputDir,'',tags)

def downloadFeed(feed,category,config,outputDir,max_number,tags):
            print('download from feed:' + feed)
            d = feedparser.parse(feed)
            for entry in d.entries[:max_number]:
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
                downloadFile(entry.link,category,config,outputDir,date,tags)

def downloadByConfig(urls,config,outputDir,max_number):
  print('download from config')
  for category in urls.keys():
    print('category:' + category)
    us = urls[category]
    for u in us:
        u2,type,regex_for_links,tags = u.split(',')
        tags = re.sub(':',',',tags)
        if(type == 'feed'):
            downloadFeed(u2,category,config,outputDir,max_number,tags)
        elif(type == 'articles'):
            downloadArticles(u2,config,outputDir,category,max_number,regex_for_links,tags)
        else: #article
            downloadFile(u2,category,config,outputDir,'',tags)
