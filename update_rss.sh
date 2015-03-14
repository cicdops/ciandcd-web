#!/bin/sh

# let git to cache password
# need input user and password for the first time
# git config --global credential.helper "cache --timeout=9999999"

if [! -d ~/ciandcd-web] ; then
  git clone https://github.com/ciandcd/ciandcd-web.git
fi

git config --global credential.helper "cache --timeout=9999999"

cd ~/ciandcd-web/
git pull
git add rss.txt
git commit -m "update rss"
git push
