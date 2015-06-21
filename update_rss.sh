#!/bin/bash -x 

# let git to cache password
# need input user and password for the first time
# git config --global credential.helper "cache --timeout=9999999"

if [ -d ~/ciandcd-web ]; then
  cd ~/ciandcd-web && git pull;
else 
  cd ~ && git clone https://github.com/ciandcd/ciandcd-web.git;
fi

git config --global credential.helper "cache --timeout=9999999";

cd ~/ciandcd-web ;

for a in http://devops.com/feed/ http://dzone.com/mz/devops/rss http://www.planetdevops.net/?feed=rss2 http://continuousdelivery.com/feed/ https://github.com/blog.atom http://blog.boxedice.com/feed/ http://www.perforce.com/blog/rss.xml http://martinfowler.com/bliki/bliki.atom http://devops.linuxjournal.com/rss.xml https://www.gitlab.com/atom.xml http://blog.devopsguys.com/feed/ http://developer-blog.cloudbees.com//feeds/posts/default; do
     echo "$a\n" 
    pelican-import --feed --output content --markup markdown  --dir-cat $a;
done

git add .
git commit -m "update rss"
git push
