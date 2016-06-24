import os
from newspaper import Article,Config

# item: url,type,regex_for_links,tags
# type can be article,articles,feed
# regex_for_links is python regex to match links
# tags is seperated by :

urls = {
    'devops': [
        'http://devops.com/feed/,feed,,devops',
        'http://dzone.com/mz/devops/rss,feed,,devops',
        'http://www.planetdevops.net/?feed=rss2,feed,,devops',
        'http://devops.linuxjournal.com/rss.xml,feed,,devops',
        'http://blog.devopsguys.com/feed/,feed,,devops',
    ],
    'ciandcd': [
        'http://continuousdelivery.com/feed/,feed,,ciandcd',
        'http://feeds.feedburner.com/AtlassianBlogsBamboo,feed,,bamboo',
        'http://feeds.feedburner.com/ContinuousBlog,feed,,jenkins',
        'http://developer-blog.cloudbees.com/feeds/posts/default,feed,,jenkins',
        'https://jazzweb1.torolab.ibm.com/blog/index.php/feed,feed,,jazz',
        'https://jazzweb1.torolab.ibm.com/pub/planet/feed.rss,feed,,jazz',
        'http://www.go.cd/feed/rss.xml,feed,,go',
        'http://openbuildservice.org/blog/,feed,,ops',
        'http://blog.jetbrains.com/feed/,feed,,jetbrains',
        'http://www.pmease.com/rss/hotnews,feed,,visualbuild',
        'https://jazz.net/blog/index.php/feed/,feed,,jazz',
        'https://www.finalbuilder.com/DesktopModules/LiveBlog/Handlers/Syndication.ashx?mid=632&PortalId=0&tid=181&ItemCount=20,feed,,finalbuilder',
        'http://blog.travis-ci.com/blog.xml,feed,,travis-ci',
    ],
    'scm':[
        'https://github.com/blog.atom,feed,,github',
        'http://blog.boxedice.com/feed/,feed,,devops',
        'http://www.perforce.com/blog/rss.xml,feed,,perforce',
        'https://www.gitlab.com/atom.xml,feed,,gitlab',
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
