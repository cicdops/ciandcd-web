Title: 投稿

#关于ciandcd
本网站使用github pages技术维护，主要关注软件持续集成和持续发布，欢迎大家提供优秀的相关文章。

#投稿
1. fork本网站源码:git clone https://github.com/ciandcd/ciandcd-web.git.　　
1. 将你的文章放到content/category/下对应的子目录中, 如果是原创文章可以放到content/category/原创.　　
1. 文章的格式可以为markdown，restructuredtext或html,需要一下额外的tags:　　
　　
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
1. 提交你的文章  
```
git add .
git commit -m "comment"
git push
```
1. 你也可以通过QQ群来提供相关的rss feed。  

#联系
QQ群：172758282，437085002　　

#感谢
https://www.python.org/  
https://pythonhosted.org/feedparser/index.html  
https://github.com/codelucas/newspaper  
https://github.com/getpelican/pelican  
http://twitter.github.com/bootstrap  
