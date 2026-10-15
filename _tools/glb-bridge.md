---
layout: tool
slug: glb-bridge
dcc: maya
gumroad: GLBBridgeForMaya
name: GLB Bridge for Maya
title: Maya GLB Import and Export, GLB Bridge
description: Import and export glTF and GLB files in Maya with meshes, materials,
  skins, blend shapes, animation, cameras and lights.
summary: glTF and GLB in and out of Maya with materials already built.
features:
- Imports .glb and .gltf with materials and textures
- Skins, blend shapes and animation
- Cameras and lights
---

## glTF and GLB in and out of Maya

GLB Bridge imports and exports `.glb` and `.gltf` files with meshes, materials and textures, skins, blend shapes, animation, cameras and lights. Bring a Sketchfab, Blender, Unity, Unreal, three.js or game-asset file into Maya with its materials already built, and send your Maya scene back out in one click. It also adds `.glb` and `.gltf` to Maya's own File > Import, Open and Export dialogs.

{% include figure.html slug="glb-bridge" name="ui-both" alt="GLB Bridge import and export panels in Maya" caption="Import and export panels." %}

## Import

- **Materials:** OpenPBR materials with base color, metalness, roughness, normal, emissive, opacity and ambient occlusion maps, texture transforms and wrap modes. Older spec-gloss files and the common KHR material extensions (clearcoat, sheen, transmission, volume, IOR, unlit) come in too. Textures are saved into the project's sourceimages folder.
- **Skins and blend shapes:** joints, bind poses and weights become a Maya skinCluster, and morph targets become blend shapes with their names and default weights.
- **Animation:** every clip, with rotations unwrapped and blend shape weights keyed. Several clips are laid out one after another on the timeline.
- **Cameras, lights and instances:** perspective and orthographic cameras, point, spot and directional lights, and GPU-instanced meshes.
- **Compressed files:** Draco and meshopt compressed meshes, quantized meshes, and KTX2 (Basis Universal) and WebP textures, converted so Maya can use them.
- **Quads come back:** glTF only stores triangles, so exports record the original quads and n-gons and an import rebuilds them exactly. For files from other tools, an optional Guess Quads setting pairs flat, smooth triangles into quads.
- **Clean meshes:** split vertices are welded back together with UVs, normals, skin weights and morph targets kept, and flat-shaded models stay flat.

## Export

{% include figure.html slug="glb-bridge" name="ui-export" side="right" alt="GLB Bridge export panel in Maya" caption="The export panel." %}

- **Scene:** meshes (triangulated, one primitive per material), hierarchy, pivots and Maya's scene units, converted to glTF's meters and Y up.
- **Materials:** Standard Surface, OpenPBR, Arnold, Redshift and the classic shaders. Separate roughness and metalness maps are packed into one image, and tangents are written for normal-mapped materials.
- **Skins and blend shapes:** exported from the rest pose, with a limit on influences per vertex (a Web Viewers preset keeps it at 4), and morph target normals.
- **Animation:** baked from the timeline, including IK, constraints and expressions. Imported clips can be exported back out as separate clips.
- **Compression (optional):** Draco meshes, and WebP or KTX2 (Basis Universal) textures, each with a Balanced, Smallest or Highest Quality setting. A skinned character with textures went from 4.3 MB to 0.8 MB in our test.
- **Validate Scene:** checks the scene before export. Every file the tool writes passes the Khronos glTF Validator with no errors.

## Requirements

For Maya 2025, 2026 and 2027. Tested in Maya 2025 and 2027. Maya 2026 runs the same Python as 2025.

## Good to know

Geometry is stored as triangles in the file (quads are rebuilt on import), so convert NURBS and subdivision surfaces before exporting. Only direct file textures are exported.
