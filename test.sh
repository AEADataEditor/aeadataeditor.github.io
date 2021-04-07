#!/bin/bash
key=$HOME/Dropbox/.myconfig/github-docker-secret
docker build -t aeaweb .
docker run -e JEKYLL_GITHUB_TOKEN=$(cat $key) --volume="$PWD:/usr/src/app" -p 4000:4000 -it aeaweb
