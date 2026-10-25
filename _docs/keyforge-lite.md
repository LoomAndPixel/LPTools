---
layout: doc
title: KeyForge Lite for Maya Documentation
description: "Install KeyForge Lite, the free Maya tween machine, and learn the Tween, Blend to Neighbors and Pull / Push sliders."
date: 2026-10-15
tool: keyforge-lite
---

## Requirements

Maya 2025, 2026 or 2027. Tested in Maya 2025 and 2027. Maya 2026 runs the same Python as 2025.

## Install

Pick one of the two ways.

**A. Drag and drop (recommended)**

1. Unzip the whole download.
2. Start Maya and drag `KeyForgeLite_drag_and_drop_install.py` into a viewport.

KeyForge Lite opens, its **LITE** button goes on the LP Tools shelf, and it gets an entry in the LP Tools menu. Click the button to show or hide the bar by the Time Slider. Maya remembers which when you restart. One install covers Maya 2025, 2026 and 2027. In another version, the button appears the first time you start it.

To remove it, choose LP Tools menu > KeyForge Lite > Uninstall.

**B. By hand, with two lines of Python**

1. Copy the whole `lp_keyforge_lite` folder from `KeyForgeLite\python\py311` (Maya 2025 or 2026) or `KeyForgeLite\python\py313` (Maya 2027) into your Maya scripts folder, `Documents\maya\scripts`.
2. Restart Maya, then run these lines in the Script Editor (Python tab):

```python
import lp_keyforge_lite
lp_keyforge_lite.toggle()
```

To make a shelf button, select the lines and middle-mouse-drag them onto a shelf.

## Update

Drag `KeyForgeLite_drag_and_drop_install.py` from the new download into Maya. It replaces the old version, including a copy you put in your scripts folder by hand. If you installed by hand, replace the files in `Documents\maya\scripts` and restart Maya. Your settings are kept either way.

## Start here

{% include figure.html slug="keyforge-lite" name="ui" alt="The KeyForge Lite bar docked under the Maya Time Slider" caption="The KeyForge Lite bar, docked right under the timeline." %}

1. Select a control. The dot next to "KeyForge Lite" shows what the sliders will change: the selected Graph Editor keys, the highlighted Time Slider range, or the current frame.
2. Click anywhere on a slider and drag. One Ctrl+Z undoes the whole drag.

## The sliders

- **Tween:** puts a pose inbetween the previous and next key.
- **Blend to Neighbors:** blends toward the previous or next key.
- **Pull / Push:** softens or exaggerates the pose.

## The buttons

Smart Key, Delete Keys, Nudge Left and Nudge Right (one frame), Copy Pose, Paste Pose, Reset Pose and Tint Red. Delete Keys, Nudge and Tint act on the selected Graph Editor keys, else the keys in the highlighted Time Slider range, else the key on this frame.

The gear (or a right-click on the bar) has Overshoot, the Channel Box filter and the bar position.

## Upgrading to KeyForge

The full [KeyForge](/tools/keyforge/) adds the Pose Library, Selection Sets, mirroring, world-space tools, temp controls, the Graph Editor strip and more than 20 more sliders. Installing it with its drag and drop installer removes KeyForge Lite for you. See the [KeyForge documentation](/docs/keyforge/).
