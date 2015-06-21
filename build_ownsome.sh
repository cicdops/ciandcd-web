#!/bin/bash -x

cwd=`pwd`;
cd content/pages && wget https://raw.githubusercontent.com/ciandcd/awesome-ciandcd/master/README.md && echo "Title: Awesome" > tmp && cat tmp README.md > awesome.md && rm README.md;
cd $cwd;

#pelican content -o output -s pelicanconf.py
#make clean && make html

#preview by ./develop_server.sh.
