#!/bin/bash

mkdir temp
cp -a ./svgs/svgs_not_in_iconset/. ./temp/ 
cp -a ./svgs/svgs_iconset/. ./temp/ 
./node_modules/.bin/spritezero ./sprites/osm-liberty ./temp/
./node_modules/.bin/spritezero --retina ./sprites/osm-liberty@2x ./temp/
rm -r temp
