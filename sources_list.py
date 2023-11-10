#!/usr/bin/python3

import requests
import os
import yaml
import json
import itertools

def req(url):
    return requests.get(url, headers={"Accept": "application/vnd.github.raw"})

def get_subclasses(values):
    subclasses = []
    for v in values:
        if 'subclass' in v:
            s = v['subclass']
        elif '__AND__' in v:
            s = v['__AND__']['subclass']
        else:
            s = get_subclasses(v)

        if type(s) is str:
            subclasses = subclasses + [s]
        else:
            subclasses = subclasses + s

    return subclasses

def main():
    if os.path.exists("iconset.json"):
        with open("iconset.json", "r") as read_file:
            iconset = json.load(read_file)
    else:
        iconset = req('https://raw.githubusercontent.com/maputnik/osm-liberty/gh-pages/iconset.json').json()
    iconset_names = [list(group['svgs'].keys()) for group in iconset['iconGroups']]
    iconset_names = [item for sublist in iconset_names for item in sublist]
    # Remove the -11.svg and -15.svg from each name list to easily deduplicate
    iconset_names = list(set([x.replace('_11.svg', '').replace('.svg', '') for x in iconset_names]))

    if os.path.exists("omt.yaml"):
        with open("omt.yaml", "r") as read_file:
            omt_poi = yaml.safe_load(read_file)
    else:
        r = req('https://api.github.com/repos/openmaptiles/openmaptiles/contents/layers/poi/poi.yaml')
        omt_poi = yaml.safe_load(r.text)
    omt_poi_class = omt_poi['layer']['fields']['class']['values'].keys()
    omt_poi_subclass = get_subclasses(omt_poi['layer']['fields']['class']['values'].values())

    print('omt_poi_class=%s' % omt_poi_class)
    print('omt_poi_subclass=%s' % omt_poi_subclass)
    print()

    if os.path.exists("maki.json"):
        with open("maki.json", "r") as read_file:
            maki_names = json.load(read_file)
    else:
        r = req('https://api.github.com/repos/mapbox/maki/contents/icons')
        maki_names = r.json()
    maki_names = [x['name'] for x in maki_names]
    # Maki names are hyphenated; iconset names are underscored
    maki_names = [x.replace('-', '_') for x in maki_names]
    maki_names = [x.replace('.svg', '') for x in maki_names]

    class_unused = set(omt_poi_class).difference(iconset_names)
    subclass_unused = set(omt_poi_subclass).difference(iconset_names)
    omt_missing = set(iconset_names).difference(omt_poi_class).difference(omt_poi_subclass)
    maki_unused = set(maki_names).difference(iconset_names)
    maki_missing = set(iconset_names).difference(maki_names)

    print('%s names in our iconset' % len(iconset_names))
    print('%s classes in OpenMapTiles' % len(omt_poi_class))
    print('%s subclasses in OpenMapTiles' % len(omt_poi_subclass))
    print('%s names in Maki' % len(maki_names))

    print('\n%s classes in OpenMapTiles unused by our iconset:' % len(class_unused))
    print(sorted(class_unused))
    print('\n%s subclasses in OpenMapTiles unused by our iconset:' % len(subclass_unused))
    print(sorted(subclass_unused))
    print('\n%s names in our iconset missing in OpenMapTiles:' % len(omt_missing))
    print(sorted(omt_missing))

    print('\n%s names in Maki unused by our iconset:' % len(maki_unused))
    print(sorted(maki_unused))
    print('\n%s names in our iconset missing in Maki:' % len(maki_missing))
    print(sorted(maki_missing))


if __name__ == '__main__':
    main()
