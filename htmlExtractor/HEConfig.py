import os
from newspaper import Article,Config

urls = {
    '中文': [
        'http://feed.cnblogs.com/blog/u/50245/rss,feed',
        'http://dockone.io/article/468,article',
        'http://dockone.io/article/470,article',
        'http://www.cnblogs.com/itech/category/245402.html,articles,http://www.cnblogs.com/itech/(?:archive).*?'
    ],
    'devops': [
        'http://devops.com/feed/,feed',
        'http://dzone.com/mz/devops/rss,feed',
        'http://www.planetdevops.net/?feed=rss2,feed',
        'http://devops.linuxjournal.com/rss.xml,feed',
        'http://blog.devopsguys.com/feed/,feed',
    ],
    'ciandcd': [
        'http://continuousdelivery.com/feed/,feed',
        'http://developer-blog.cloudbees.com/feeds/posts/default,feed',
        'https://jazzweb1.torolab.ibm.com/blog/index.php/feed,feed',
        'https://jazzweb1.torolab.ibm.com/pub/planet/feed.rss,feed',
        'http://www.go.cd/feed/rss.xml,feed',
        'http://openbuildservice.org/blog/,feed',
        'http://feeds.feedburner.com/AtlassianChina,feed',
        'http://blog.jetbrains.com/feed/,feed',
        'http://www.pmease.com/rss/hotnews,feed',
        'https://jazz.net/blog/index.php/feed/,feed',
        'https://www.finalbuilder.com/DesktopModules/LiveBlog/Handlers/Syndication.ashx?mid=632&PortalId=0&tid=181&ItemCount=20,feed',
    ],
    'scm':[
        'https://github.com/blog.atom,feed',
        'http://blog.boxedice.com/feed/,feed',
        'http://www.perforce.com/blog/rss.xml,feed',
        'https://www.gitlab.com/atom.xml,feed',
    ],
}

outputDir = 'content' + os.sep + 'category'
max_number = 20
max_days = 10

config = Config()
config.memoize_articles = False
config.fetch_images = False
config.request_timeout = 60
config.number_threads = 20
config.keep_article_html = True
config.MIN_WORD_COUNT = 20
config.verbose = True
