---
layout: tool
slug: fspy-importer-maya
dcc: maya
gumroad: fspyCameraMaya
name: fSpy Importer for Maya
maya_versions: "Maya with Python 3"
maya_tested: "2025, 2027"
title: fSpy Importer for Maya, Photo Camera Match
description: Import an fSpy project into Maya as a matched camera and image plane
  for photo camera matching.
summary: Bring an fSpy camera match into Maya.
note: Based on fSpy by Per Gantelius, released under GPL-3.0-or-later.
features:
- Imports fSpy projects
- Matched camera and image plane
- Free and open source (GPL)
---

## Import an fSpy camera match into Maya in one click

fSpy matches a camera to a single photo from its perspective lines. This free importer turns the saved `.fspy` project into a ready-to-use Maya camera, image plane and camera projection shader, so you can model, animate or composite against the photo right away. It works with any image size and aspect ratio.

{% include figure.html slug="fspy-importer-maya" name="ui-desc" side="right" alt="fSpy Importer window in Maya" caption="Pick an .fspy project and import." %}

## What it creates

- **A matched camera** with the position, rotation, focal length and field of view from the fSpy solve, including film offset for off-center principal points.
- **An image plane** showing the reference photo, pushed behind your scene.
- **Render resolution** set to the photo's size.
- **A camera projection surface shader** that projects the photo onto your geometry (optional).

The photo embedded in the `.fspy` file is extracted automatically, so there is nothing extra to manage. The whole import is one undo step.

## Options

- **Up axis:** Auto picks fSpy's up axis for you (Maya is Y-up), or choose it yourself for photos looking straight down.
- **True scale:** if you set a reference distance in fSpy, the camera comes in at real-world scale in your scene's units.
- **Lock camera:** locks the transform and lens so the match cannot be nudged by accident.

## Requirements

Tested in Maya 2025 and 2027 (Python 3).

## About fSpy

fSpy is free, open-source camera matching software by Per Gantelius. This importer follows his official fSpy importer for Blender and is free and open source too, under GPL-3.0.
