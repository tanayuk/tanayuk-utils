#!/bin/bash

git branch -r --merged | grep -v master | grep -v develop |  sed 's/origin\///' | xargs -n 1 git push --delete origin
