# www.ciandcd.com

![logo](ciandcd.png)  

###build status
![build and deploy status:](https://travis-ci.org/ciandcd/ciandcd-web.svg?branch=master)

###env
1. need python installed
1. install pelican : pip install pelican Markdown typogrify
1. install ghp-import: pip install ghp-import

###edit or add
1. add new blog entities or pages in content/.
1. build by make clean && make html
1. preview by ./develop_server.sh.

###push and deploy
1. submit by git commit and git push
1. deploy by make clean && make publish && make github (obsolete)
1. will be deployed by trivs CI automatically

###contribution
1. file issues.
1. pull requests.

###contact
1. by email itech001@126.com.

