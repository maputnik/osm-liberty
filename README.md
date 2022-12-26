# OSM Liberty [![BSD licensed](https://img.shields.io/badge/license-BSD-blue.svg)](https://github.com/maputnik/osm-liberty/blob/gh-pages/LICENSE.md)

<img align="right" alt="OSM Liberty" src="logo.png" />

This is a fork from [osm-liberty](https://github.com/maputnik/osm-liberty). We use this as a base map style for the whole Ehrenamtskarte project. Whenever you see a map in the context of the Ehrenamtskarte, then this style should be used.

A free Mapbox GL basemap style for everyone with complete liberty to use and self host. OSM Liberty is a fork of OSM Bright based on free data sources with a mission for a clear good looking design for the everyday user. It is based on the vector tile schema of [OpenMapTiles](https://github.com/openmaptiles/openmaptiles).

**[Preview OSM Liberty with Maputnik](https://maputnik.github.io/editor/?style=https://digitalfabrik.github.io/ehrenamtskarte-maplibre-style/style.json)**

## Usage

You can use the style in your Mapbox GL maps.

By default, the vector tiles, raster tiles and sprites directly and glyphs are served from [Tür an Tür](https://maps.tuerantuer.org).


They were created using [OpenMapTiles](https://github.com/openmaptiles/openmaptiles).


## Data Sources

- [OpenMapTiles](http://openmaptiles.org/) as vector data source
- [Natural Earth Tiles](https://klokantech.github.io/naturalearthtiles/) for relief shading
- [Maki](https://www.mapbox.com/maki-icons/) as icon set
- Tiles from the Ehrenamtskarte project which shows stores

## Map Design

The map design originates from OSM Bright but strives to reach a unobtrusive and clean design for everyday use.
Colored relief shading from Natural Earth make the low zoom levels look good.

[![OSM Liberty Map demo](demo/zoom.gif)](demo/zoom.gif)

## Edit the Style

You can [edit the style directly online in Maputnik](https://maputnik.github.io/editor?style=https://digitalfabrik.github.io/ehrenamtskarte-maplibre-style/style.json).

You can also run maputnik locally:

```bash
wget https://github.com/maputnik/editor/releases/download/v1.7.0/maputnik-linux.zip
unzip maputnik-linux.zip
chmod +x maputnik
./maputnik --file style.json
```

A pre-commit hook is included to validate and format the JSON styles using
[`mapbox-gl-style-spec`](https://www.npmjs.com/package/@mapbox/mapbox-gl-style-spec).
To use, just install the NPM dev dependencies:
```
npm install
```
and then validate or format the style with
```
npm run validate
npm run format
```

Validation and reformatting will happen automatically on commit if you have the
dependencies installed.

## Icon Design

A [Maki](https://github.com/mapbox/maki) icon set using colors to distinguish between icon categories.

Maki is a living project and adds new icons over time, which means that there
could be new icons that OSM Liberty could use for POIs. `maki_list.py` is a
simple script to list both the names in OSM Liberty's iconset that don't map to
any valid Maki name, and the Maki names that are not currently used in OSM
Liberty's iconset. You can run the script with `python3 maki_list.py`.

**Color Palette**

Color Name   | Hex Value
-------------|----------
Blue         | `#5d60be`
Light Blue   | `#4898ff`
Orange       | `#d97200`
Red          | `#ba3827`
Brown        | `#725a50`
Green        | `#76a723`

**Modify Icons**

1. Take the `iconset.json` and import it to the [Maki Editor](https://www.mapbox.com/maki-icons/editor/).
2. Apply your changes and download the icons in SVG format and the iconset in JSON format.
3. Format the JSON with `cat iconset.json | jq -MS '.'` for better legibility.
4. Replace the current iconset.json in this repository with the updated one.
5. Replace all the icons in the `svgs_iconset` with the SVGs downloaded from the Make Editor.
