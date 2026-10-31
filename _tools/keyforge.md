---
layout: tool
slug: keyforge
dcc: maya
gumroad: KeyForgeForMaya
name: KeyForge for Maya
maya_versions: "2024, 2025, 2026, 2027"
maya_tested: "2024, 2025, 2027"
title: KeyForge, a Maya Animation Toolkit
description: KeyForge is a Maya animation toolkit with a tween machine, pose library
  and fast keying tools for animators.
summary: 'An animation toolkit for Maya: tweening, a pose library and quick keying
  tools in one window.'
features:
- Tween machine bar
- Pose library
- Fast keying tools
---

## An animation toolkit by Maya's Time Slider

I'm not an animator, but I've worked next to animators my whole career, and I've seen how much of their day goes to clicking through menus instead of animating. KeyForge puts 25 blend sliders and more than 170 animation tools on one compact bar docked right under the timeline. Tween and blend poses, retime keys, mirror, bake, tint keys by type, work in world space and use temp controls, without digging through menus.

**Try it free first:** [KeyForge Lite](/tools/keyforge-lite/) gives you the Tween, Blend to Neighbors and Pull / Push sliders plus Smart Key, Delete Keys, Nudge, Copy / Paste Pose, Reset Pose and Tint, at no cost. If you like it, come back for the full KeyForge. Installing it removes KeyForge Lite for you.

{% include figure.html slug="keyforge" name="ui" alt="The KeyForge bar docked under the Maya Time Slider" caption="The KeyForge bar, docked right under the timeline: one slim row by default." %}

## A bar that stays out of your way

The bar starts as one slim 32 pixel row with the 14 buttons you use every shot and three sliders you choose yourself. Each slider slot has a small arrow that swaps in any of the 25 tools. Switch to two rows for the next tier of tools and five sliders, or pick a ready-made workspace (Essentials, Blocking, Polish, Layout and Rig, Full, or the classic 0.7 bar) from the gear menu.

{% include figure.html slug="keyforge" name="ui-two-rows" alt="The KeyForge bar in two rows under the Maya Time Slider" caption="The same bar in two rows: every button on top, five sliders below." %}

## How it works

Select controls and drag a slider. The dot next to KeyForge shows what will change: the keys selected in the Graph Editor, the highlighted Time Slider range, or the current frame. While you drag, the slider shows what the end you are heading to means, plus the value, and one Ctrl+Z undoes the whole drag. If a tool can't run, the bar tells you why.

## What you get

{% include figure.html slug="keyforge" name="graphbar-1row" alt="The KeyForge Graph Bar in one row inside Maya's Graph Editor, with the tools and the Translate, Rotate and Scale fields side by side" caption="The KeyForge Graph Bar sits inside the Graph Editor, right under its own buttons: tools and channel fields in one row." %}

- **25 blend sliders:** tween and blend to neighbors, a default pose, a frame or a mirrored pose, shape and ease your curves, mend gaps and cycle, and move poses in world space.
- **More than 170 tools:** smart keying, copy and paste keys, tangents and key colors, pose and mirror tools, world-space and rig helpers, and navigation and view tools.
- **A Graph Bar inside the Graph Editor,** so the same tools work while you look at curves, with Translate, Rotate and Scale fields that color like the Channel Box.

- **KeyForge Tools, one window for everything:** a searchable catalog of every tool. Click a star to put a tool on the bar, press keys to give it a hotkey, or run it right there.

{% include figure.html slug="keyforge" name="window" alt="The KeyForge Tools window showing the tool catalog" caption="KeyForge Tools: browse, search, pin and give hotkeys." %}

Every slider and tool is listed in the [KeyForge documentation](/docs/keyforge/).

## Pose Library

{% include figure.html slug="keyforge" name="pose-library" side="right" alt="KeyForge Pose Library with pose thumbnails" caption="The Pose Library saves poses with a thumbnail." %}

Save the selected controls as a pose in one click, with a thumbnail of the viewport so you can find it later. Poses are sorted by character into folders you name yourself (Face, Body, Hands), and a Thumbnails slider sets 2 to 8 poses per row. Search looks through every character at once, and you can drag poses between folders.

- **Apply or blend:** double-click a pose to apply it at the current frame, or use the blend slider to bring it in gradually. Applying is one Ctrl+Z.
- **Across rigs and scenes:** controls are matched by name with namespaces ignored, so a pose saved on one character can go onto another rig that uses the same control names.
- **Yours to keep:** the library lives in a folder on disk, outside your scenes, so it stays when you open a new file.

## Selection Sets

{% include figure.html slug="keyforge" name="selection-sets" side="left" alt="The KeyForge Selection Sets window with one button per set" caption="One button per set, with the control count." %}

Selection Sets are named groups of controls, such as Face, Eyebrows or Left Hand, with one button each. Select some controls, click **+ New Set from Selection**, and name it. From then on one click selects the whole group, even on a rig with a lot of controls.

- **Click** a set to select it, **Shift + click** to add it to the selection, **Ctrl + click** to remove it.
- **Right-click** a set to replace its controls with your selection, add to it, remove from it, rename it or delete it.
- **Saved with the scene:** sets are ordinary Maya object sets, so they travel with the file and stay when you hand the scene to someone else.

<div style="clear:both"></div>

Right-click a slider on the bar for a floating, movable, resizable slider with fine ranges and Overshoot. You can also make the S key run Smart Key.

## Requirements

For Maya 2024, 2025, 2026 and 2027. Tested in Maya 2024, 2025 and 2027. Maya 2026 runs the same Python as 2025.
