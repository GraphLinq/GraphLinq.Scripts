#!/bin/sh
# Recursively convert files from GitBook into Markdown files

find . -name "*.md" | while read i; do pandoc -f html -t markdown "$i" -o "$i"; done

# Don't overwrite original
# find . -name "*.ht*" | while read i; do pandoc -f html -t markdown "$i" -o "${i%.*}.md"; done
