import os
import re
from datetime import *
import feedparser
from newspaper import Article,Config

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
    if not date:
      html = html + '<meta name="date" content="' + date + '"/>'
    html = html + title + '</title></head><body>'
    html = html + 'From:<a href=' + link + '>' + link + '</a><br><br>'
    html = html + content + '</body></html>'
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

def download_file(link,config,outputDir,category,date):
    try:
        a = Article(link,config=config, keep_article_html=True)
        a.download()
        a.parse()
        if not a.title:
           print("cannot find title for " + link)
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

        if(content_html):
            domain = getDomain(link)
            content_html = fixLinks(content_html,domain)
            writeHtml(outPath,content_html,a.title,link,date)
        elif(content):
            writeHtml(outPath,content,title,link,date)
        else:
            print('Error:cannot find content')
    except Exception as e:
        print('Exception:' + link)
        print(e)
        return 0
    return 1

