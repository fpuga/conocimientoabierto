#!/bin/sh
docker run --rm -e CARDS=true -v "${PWD}":/docs squidfunk/mkdocs-material build
# Add symlink to preserve old feed url operation
# cd site && cp feed_rss_created.xml feed.xml
