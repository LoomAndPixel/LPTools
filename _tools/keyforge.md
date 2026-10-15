---
layout: tool
slug: keyforge
dcc: maya
gumroad: KeyForgeForMaya
name: KeyForge for Maya
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

KeyForge puts 25 blend sliders and more than 170 animation tools on one compact bar docked right under the timeline. Tween and blend poses, retime keys, mirror, bake, tint keys by type, work in world space and use temp controls, without digging through menus.

**Try it free first:** [KeyForge Lite](/tools/keyforge-lite/) gives you the Tween, Blend to Neighbors and Pull / Push sliders plus Smart Key, Reset Pose and Copy / Paste Pose, at no cost. If you like it, come back for the full KeyForge. Installing it removes KeyForge Lite for you.

{% include figure.html slug="keyforge" name="ui" alt="The KeyForge bar docked under the Maya Time Slider" caption="The KeyForge bar, docked right under the timeline." %}

## How it works

Select controls and drag a slider. The dot next to KeyForge shows what will change: the keys selected in the Graph Editor, the highlighted Time Slider range, or the current frame. While you drag, the slider shows what the end you are heading to means, plus the value, and one Ctrl+Z undoes the whole drag. If a tool can't run, the bar tells you why.

## Sliders

- **Blend to a pose:** Tween, Blend to Neighbors, Default, Frame (with a reference frame box), Mirror, Buffer, Mirror from Frame and Partial Undo.
- **Shape:** Pull / Push, Scale From (average, default, frame or neighbor key), Smooth / Rough, Ease In / Out, Blend to Ease and Wave.
- **Timing and cycles:** Gap Mender, Bridge to Neighbors, Blend to Cycle and Time Shift (with stagger).
- **World space:** Tween, Neighbors, Frame, Cycle, Align, Copied Xform and Relationship, all keeping hands and feet where they belong.

## Tools

{% include figure.html slug="keyforge" name="graph-editor" alt="A KeyForge strip inside Maya's Graph Editor" caption="A KeyForge strip sits inside the Graph Editor, right under its own buttons." %}

- **Keys and timing:** Smart Key, copy, cut and paste keys and key times, nudge, insert and remove inbetweens, share and snap key times, bake on ones to fours, and simplify.
- **Tangents:** Smart, Clean, Smooth and Contact recipes, every Maya tangent type, blend toward any of them, cycle match and Euler filter.
- **Key colors:** tint keys red, yellow or green, then jump to, play or delete keys by color, plus Auto Tint.
- **Pose and mirror:** copy and paste pose, reset, mirror pose and animation (names like Arm_L, armL, leftArm, or pairs you save) and preferred default poses.
- **World and rig:** copy and paste world transforms and relationships, align, Global Offset, space switching that keeps the world position, temp controls, and temp pivots you rotate controls around. These are keyed and the rig is never touched.
- **Navigate and view:** previous and next key by color, play keys only, play on twos, time bookmarks, visibility modes, isolate, live motion trails with a tick per frame, and Graph Editor and Channel Box helpers.

## Pose Library and Selection Sets

{% include figure.html slug="keyforge" name="pose-library" side="right" alt="KeyForge Pose Library with pose thumbnails" caption="The Pose Library saves poses with a thumbnail." %}

The Pose Library saves poses with a thumbnail, sorted by character into your own folders, with 2 to 8 thumbnails per row. Selection Sets are named groups of controls (Face, Eyebrows, Left Hand) that you select with one click.

Right-click a slider on the bar for a floating, movable, resizable slider with fine ranges and Overshoot. You can also make the S key run Smart Key.

## Requirements

For Maya 2025, 2026 and 2027. Tested in Maya 2025 and 2027. Maya 2026 runs the same Python as 2025.
