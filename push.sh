#!/bin/bash

git pull
echo `date` > date.txt
git add .
git commit -m "update"
git push  
