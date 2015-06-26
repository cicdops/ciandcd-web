import os
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
        'https://jazz.net/blog/index.php/feed/',
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

