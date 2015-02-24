#!/bin/bash
pelican content -o output -s pelicanconf.py
ghp-import output
git push https://github.com/ciandcd/ciandcd.github.io.git gh-pages:master
