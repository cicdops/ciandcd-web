Title: 投稿

##LOGO
![logo](ciandcd.png)   

##build 状态
[![Build Status](https://travis-ci.org/ciandcd/ciandcd-web.svg?branch=master)](https://travis-ci.org/ciandcd/ciandcd-web/)  

##关于ciandcd.com  
本网站使用github pages技术维护，主要关注软件持续集成和持续发布，欢迎大家提供优秀的相关文章。  

##投稿
1. fork本网站源码:git clone https://github.com/ciandcd/ciandcd-web.git.　　
2. 将你的文章放到content/category/下对应的子目录中, 如果是原创文章可以放到content/category/原创.　　
3. 文章的格式可以为markdown，restructuredtext或html。  
4. 提交你的文章。  
5. 你也可以通过QQ群来提供相关的rss feed。  
 
.rst格式  
```
My super title
\##############

:date: 2010-10-03 10:20
:modified: 2010-10-04 18:40
:tags: thats, awesome
:category: yeah
:slug: my-super-post
:authors: Alexis Metaireau, Conan Doyle
:summary: Short version for index and feeds

This is the content of my super blog post.
```
.md格式  
```
Title: My super title
Date: 2010-12-03 10:20
Modified: 2010-12-05 19:30
Category: Python
Tags: pelican, publishing
Slug: my-super-post
Authors: Alexis Metaireau, Conan Doyle
Summary: Short version for index and feeds

This is the content of my super blog post.
```
.html格式  
```
<html>
    <head>
        <title>My super title</title>
        <meta name="tags" content="thats, awesome" />
        <meta name="date" content="2012-07-09 22:28" />
        <meta name="modified" content="2012-07-10 20:14" />
        <meta name="category" content="yeah" />
        <meta name="authors" content="Alexis Métaireau, Conan Doyle" />
        <meta name="summary" content="Short version for index and feeds" />
    </head>
    <body>
        This is the content of my super blog post.
    </body>
</html>
```

##联系
email: itech001@126.com  
QQ群：172758282，437085002  　　

##感谢
https://www.python.org/  
https://pythonhosted.org/feedparser/index.html  
https://github.com/codelucas/newspaper  
https://github.com/getpelican/pelican  
http://twitter.github.com/bootstrap  

##开发环境
1. prod环境请参考.travis.yml.  
2. 本地测试环境　　
*make clean && make html
*make devserver, or 'cd output && python -m http.server 8000'.

##自动deploy
1. 所有的修改会被trivs CI自动build和deploy到github pages.  

##问题
1. file issues.  
1. pull requests.  

###License
1. MIT License for this source code  
1. [Creative Commons Attribution 3.0 Unported License](http://creativecommons.org/licenses/by/3.0/) for the content of www.ciandcd.com which includes all blogs, pages and articles   
