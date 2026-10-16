---
layout: guide
title: How to Import Map Data into Maya (Work in Progress)
crumb: Import map data into Maya
description: "Maya has no built-in way to import real-world map data. Here is how I am building one: OpenStreetMap buildings, terrain, roads and roofs in Maya, with renders from the development."
date: 2026-10-15
tool: glb-bridge
faq:
- q: Can Maya import map data?
  a: "Not out of the box. Maya has no tool for real-world buildings, terrain or roads. The usual advice is a Blender plugin and a file round trip, which is what I am trying to avoid with a Maya-native importer."
- q: Where does the building data come from?
  a: "OpenStreetMap, which is open data. Building footprints and height tags become real geometry, and where heights are missing the importer estimates them from the number of floors."
- q: Is the Map Importer for Maya available?
  a: "Not yet. It is in development and not listed. This page follows its progress."
---

If you want a real place in Maya, such as a city block, a hillside or a street for a shot, there is **no built-in way to do it**. Ask around and the answer is nearly always the same: use a Blender plugin, export a file, and bring it into Maya.

That works, but it is a long way round. So I am building a map importer that lives inside Maya. It is not released yet. This page is a look at where it is, with renders straight from development.

## The idea

Type a place or click on a map, pick a radius, and get real geometry in your scene:

- **Buildings** from OpenStreetMap footprints, extruded to their real heights.
- **Terrain** from elevation data, so hills are hills.
- **A ground map** with roads, water, parks and paths painted on, or real roads as geometry.
- **Roofs** that are pitched or hipped where the data says so, instead of flat lids.

Everything lands in one group with the location stored on it, so the scene knows where it is in the world.

## Step by step

Every image below uses the same camera on the same place (Delft, in the Netherlands), with one more setting switched on each time.

### Buildings

Footprints come from OpenStreetMap, and heights come from the height or floor tags. Where a building has no tag, the importer assumes a floor count. Garages and sheds get one floor, so they do not turn into towers.

{% include figure.html slug="map-importer" name="buildings" alt="Grey building blocks of central Delft imported into Maya, cropped to a circle" caption="Buildings only, with flat roofs." %}

### Roof shapes

Where OpenStreetMap describes the roof, the importer builds it. The churches and the larger roofs stop being boxes.

{% include figure.html slug="map-importer" name="roofs" alt="The same Delft buildings with pitched and hipped red roofs" caption="Roof shapes on. Same camera, same place." %}

### Ground, water and roads

A ground map is painted from the map data: canals, roads, paths and green areas. Roads can also be built as real strips just above the terrain.

{% include figure.html slug="map-importer" name="ground" alt="Delft with the ground map showing blue canals, grey roads and green parks" caption="Ground map on: canals, streets and parks." %}

### Better buildings where the data exists

Some countries publish detailed 3D building models. In the Netherlands that is the 3D BAG dataset, and I am testing it as a source. The difference is large.

{% include figure.html slug="map-importer" name="bag" alt="Delft with detailed 3D BAG buildings and individual red roofs" caption="Detailed 3D BAG buildings in place of extruded footprints." %}

A square crop with a base gives you something that reads as a model on a plinth, which is handy for presentation shots.

{% include figure.html slug="map-importer" name="bag-base" alt="Square crop of Delft with a thin black base, detailed buildings and canals" caption="Square crop with a base." %}

## Other places

Dense cities and coastlines break things in different ways, so I keep testing on very different locations. Midtown Manhattan is mostly height, and the Embarcadero in San Francisco is mostly water.

{% include figure.html slug="map-importer" name="nyc" alt="Midtown Manhattan towers imported into Maya on a square base with streets" caption="Midtown Manhattan, square crop with a base." %}

{% include figure.html slug="map-importer" name="sf-sea" alt="San Francisco's Telegraph Hill and Embarcadero with a sea surface and piers" caption="San Francisco: piers, a waterfront road and a sea surface." %}

## Why not just use a Blender plugin?

Those plugins do the job, but the trip has costs:

- You export from one app and import into another, and every change means doing it again.
- Scale and orientation (Blender's Z-up against Maya's Y-up) have to be put right.
- Materials rarely arrive the way you expect.

Working in Maya means the result is already native geometry, in your scene units, with materials you can render.

## How GLB Bridge came out of this

Some map data arrives as glTF or GLB files, and Maya's own support for those is poor. I needed something that read them properly, with materials, textures and compression. That became [GLB Bridge for Maya](/tools/glb-bridge/), a general importer and exporter for GLB and glTF. It is a separate tool you can use on its own, and the map importer uses its reader.

## Where it stands

- Buildings, terrain, ground map, roads, trees and roof shapes work.
- Aerial photo textures, a sea surface and better building sources are being tested.
- Edges, bridges and heavy cities still need work.
- It is not released, there is no date, and nothing is listed yet.

I will update this page as it moves.

## Data credits

Map data is © OpenStreetMap contributors, available under the Open Database License. Detailed Dutch buildings are from 3D BAG. Terrain comes from public elevation datasets.
