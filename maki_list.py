import requests


def main():
    osm_iconset_url = 'https://raw.githubusercontent.com/maputnik/osm-liberty/gh-pages/iconset.json'

    r = requests.get(osm_iconset_url)
    osm_iconset = r.json()

    osm_iconset_keys = [
        list(group['svgs'].keys()) for group in osm_iconset['iconGroups']]
    osm_iconset_keys = [
        item for sublist in osm_iconset_keys for item in sublist]

    maki_url = 'https://api.github.com/repos/mapbox/maki/contents/icons'
    r = requests.get(maki_url)
    maki_names = [x['name'] for x in r.json()]

    # Maki names are hyphenated; iconset names are both hyphenated and underscored
    # I'll take the iconset names and change the underscores to hyphens
    osm_iconset_keys = [x.replace('_', '-') for x in osm_iconset_keys]

    # Remove the -11.svg and -15.svg from each name list to easily deduplicate
    # each list
    maki_names = [
        x.replace('-11.svg', '.svg').replace('-15.svg', '.svg')
        for x in maki_names]
    osm_iconset_keys = [
        x.replace('-11.svg', '.svg').replace('-15.svg', '.svg')
        for x in osm_iconset_keys]

    maki_diff = set(maki_names).difference(osm_iconset_keys)
    osm_diff = set(osm_iconset_keys).difference(maki_names)

    print('Names in Maki unused by OSM Libery:')
    print(sorted(maki_diff))

    print('\nNames in Maki unused by OSM Libery:')
    print(sorted(osm_diff))


if __name__ == '__main__':
    main()
