---
layout: tool
slug: camera-toolkit
dcc: maya
gumroad: CameraToolkitForMaya
name: Camera Toolkit for Maya
title: Maya Camera Tools, Camera Toolkit
description: 'Camera Toolkit for Maya: bake cameras, pull focus, add camera shake
  and show the frustum.'
summary: Everyday camera helpers for Maya in one window.
features:
- Bake
- Focus
- Shake and frustum
---

## Every camera tool in one dockable window

Camera Toolkit brings lens and film back presets, a frustum visualizer, focus rigs, procedural camera shake, and baking any camera rig down to one clean camera, all in one place in Maya.

{% include figure.html slug="camera-toolkit" name="viewport" alt="A camera frustum and focus plane shown in the Maya viewport" caption="The frustum visualizer shows what a camera sees from any other view." %}

Coming from Camera Bake? This is its replacement, and a free update if you already have it. Bake Camera does the same job as before (any rig to a single, clean, world-space camera) and now also handles film offsets, image planes and Arnold and Redshift camera settings.

## What's in the window

{% include figure.html slug="camera-toolkit" name="ui-desc" side="right" alt="Camera Toolkit window in Maya" caption="Everything lives in one dockable window." %}

- **Bake and Export:** bake any rig (aim and parent constraints, motion paths, nested groups, custom pivots, shake) to a new camera at the top of the hierarchy, with animated lens values. Export FBX bakes and exports in one step, ready for Unreal, Unity, Blender, Nuke or Houdini.
- **Lens:** one-click focal lengths from 12 to 300mm, film back presets (Full Frame, Super 35, ALEXA 35, Mini and Mini LF, V-RAPTOR, VENICE 2, IMAX, APS-C, Micro Four Thirds), gate, mask and safe frame toggles, overscan, and Camera from View.
- **Frustum:** see exactly what a camera sees from any other view, as a see-through pyramid that follows the lens, film back, film fit and render resolution. It can end at the focus distance to show the focus plane, and it never renders.
- **Focus:** a focus control in front of the camera that drives Maya's and Arnold's focus distance and Redshift's Bokeh. Pick Focus lets you click any surface in the viewport to focus there. Focus on Selection, optional keys on every pick, DOF on and off, and f-stop are included.
- **Shake:** procedural shake in 2D (film offset, so the camera does not move) or 3D (turns the camera in its own space, with optional movement for parallax). Presets cover Subtle, Handheld, Walking, Running, Vehicle and Impact. It works on top of existing keys, constraints and aim rigs, and Bake Shake turns it into keys.
- **Copy:** copy lens settings and, or, position from one camera to others, at the current frame or baked over the frame range.

## Good to know

Every button works on the selected cameras, or the camera you are looking through when none is selected. Everything is one Ctrl+Z, and every tool can also be called from a script or shelf button.

## Requirements

For Maya 2025, 2026 and 2027. Tested in Maya 2025 and 2027. Maya 2026 runs the same Python as 2025.
