---
layout: tool
slug: material-generator
dcc: maya
gumroad: MaterialGeneratorForMaya
name: Material Generator and Converter for Maya
title: Maya Material Converter for Arnold, Redshift, V-Ray
description: Generate and convert materials in Maya between Arnold, Redshift and V-Ray.
summary: Build materials from textures and convert them between renderers.
features:
- Arnold, Redshift and V-Ray
- Generate from texture sets
- Convert existing materials
---

## Build materials from a texture folder

{% include figure.html slug="material-generator" name="ui-desc" side="right" alt="Material Generator window in Maya with a texture folder chosen and a Redshift Standard Material build log" caption="Pick a folder and a renderer. The log shows every map it connects." %}
Point Material Generator at a folder of textures and it scans the folder and its subfolders, groups the files into materials by name, and builds one complete material per set in Arnold, Redshift or V-Ray. Every map is connected to the right attribute, with the right color space and the right helper nodes. Run it again after adding more maps and it only fills in what is missing.

- **Normal maps and displacement** are built the way each renderer expects: aiNormalMap for Arnold, RedshiftNormalMap with Bump Blender for Redshift, and tangent-space bump for V-Ray.
- **UDIMs** (1001, 1002 and so on) and **packed maps** such as ORM, where one texture feeds roughness and metalness, are handled automatically.
- **Redshift extras:** optional Round Corners on every normal map, and a choice of opacity or Sprite node for cutouts. Redshift Standard, OpenPBR and Legacy materials are supported.

## Convert materials between renderers

Select materials, or convert the whole scene, between Arnold, any Redshift material type and V-Ray. Texture connections and values are kept, and one Ctrl+Z undoes the whole conversion.

## Texture naming

Files are matched by the keyword at the end of the name, the same way Substance Painter exports them, for example `Wood_Oak_BaseColor.png` or `Wood_Oak_Roughness.1001.exr`. It recognizes BaseColor, Albedo and Diffuse, Metalness, Roughness, OcclusionRoughnessMetallic (ORM), Specular, Opacity, Emissive, Subsurface (color, weight, radius), Normal, and Height or Displacement. If your textures follow a different convention, every keyword and attribute can be changed in an editable config file.

## Requirements and install

For Maya 2025, 2026 and 2027, tested with Redshift and Arnold. Install by dragging the included installer file into a Maya viewport. A MAT button is added to the LP Tools shelf, with an entry in the LP Tools menu. One install covers all three Maya versions, and the download includes a README with a manual install option.

## A note for V-Ray users

V-Ray support is built from V-Ray's published attribute names and naming conventions, and has not been tested in a copy of V-Ray. If you use V-Ray, try it and tell us what works or breaks at Tools@LoomAndPixel.com.

## Who it is for

Look development and texturing artists who set up many PBR materials from Substance Painter or similar exports and want to skip the manual node wiring, or who need to move a scene from one renderer to another.
