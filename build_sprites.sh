#!/bin/bash

mkdir -p ./temp/svgs
cp -a ./svgs/svgs_not_in_iconset/. ./temp/svgs/
cp -a ./svgs/svgs_iconset/. ./temp/svgs/
wget -P ./temp https://github.com/flother/spreet/releases/download/v0.13.1/spreet-x86_64-unknown-linux-musl.tar.gz
tar -xzvf ./temp/spreet-x86_64-unknown-linux-musl.tar.gz -C ./temp
./temp/spreet --unique --minify-index-file --recursive ./temp/svgs/ ./sprites/osm-liberty
./temp/spreet --unique --minify-index-file --recursive --retina ./temp/svgs/ ./sprites/osm-liberty@2x
rm -r temp
