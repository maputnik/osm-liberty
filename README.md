# OSM Liberty

A fork of OSM Bright based on free data sources with a mission for a clear good looking design for the
everyday user.

## Data Sources

- [OSM2VectorTiles](http://osm2vectortiles.org/) as vector data source
- [Natural Earth Tiles](naturalearthtiles.org) for relief shading
- [Maki](https://www.mapbox.com/maki-icons/) as icon set

## Map Design

The map design originates from OSM Bright but strives to reach the clean design and elegance of Google Maps.
Colored relief shading from Natural Earth makes the low zoom levels look good.

![Europe](demo/europe.png)
![Switzerland](demo/europe.png)
![Zurich](demo/zurich.png)
![Zurich Bürkliplatz](demo/zurich_buerkliplatz.png)

## Icon Design

A [Maki](https://github.com/mapbox/maki) icon set using colors to distinguish between icon categories.

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

1. Take the style JSON file and upload it to the [Maki Editor]().
2. Apply your changes and download the icon set again.
3. Ensure you format the JSON first with `cat iconset.json | jq -MS '.'`

## License
