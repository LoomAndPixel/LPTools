---
layout: tool
slug: mixamo-auto-control-rig
dcc: maya
gumroad: MixamoAutoControlRigForMaya
name: Mixamo Auto Control Rig for Maya
maya_versions: "2024 to 2027"
maya_tested: "2024, 2025, 2027"
compat_note: "Needs a character autorigged by mixamo.com."
title: Mixamo Auto Control Rig for Maya 2024-2027
description: Mixamo Auto Control Rig for Maya, updated for Maya 2024 to 2027. Build
  an animator friendly control rig on a Mixamo character in a few clicks.
summary: Builds a control rig on a Mixamo character so you can animate it by hand
  instead of using the baked Mixamo motion.
note: Loom & Pixel holds no rights to Mixamo. The original authors of the Mixamo Auto
  Control Rig are credited in the tool and its documentation.
features:
- One window setup for Mixamo skeletons
- Updated for Maya 2024 through 2027
- Original authors credited
faq:
- q: Does it work in recent Maya versions?
  a: Yes. This version is updated for Maya 2024 through 2027.
---

## A Mixamo control rig that works in current Maya

Mixamo's original Auto Control Rig tool stopped being updated years ago and no longer runs in modern Maya. This is the original v1.6.0 ported to Python 3 and tested in Maya 2024, 2025 and 2027, so the community has a compatible version. It builds a control rig on a character autorigged by Mixamo, so you can edit Mixamo motions or keyframe your own animation.

{% include figure.html slug="mixamo-auto-control-rig" name="window-desc" side="right" alt="Mixamo Auto Control Rig window in Maya" caption="The Mixamo Auto Control Rig window." %}

## What it does

- **FK/IK arms and legs** that follow the animation data, with no baking.
- **AnimDataMult attributes** to exaggerate or ignore the animation data.
- **Bake or clear** the animation on the controls at any point in time. The animation is preserved.
- **Facial controls** on FacePlus-compatible characters (Osipa style, eye rotation and aim).
- **Hands and feet** custom attributes, and an optional pelvis control.
- **Dynamic joints** and joint chains.
- **Export** a baked FK skeleton, plus batch import and batch export tabs.

## How to use it

Import a Mixamo character (FBX) in its original pose or T-pose, click Rig Character, then import a Mixamo animation onto the rig. The download includes the original documentation PDF, written for version 1.6.0.

{% include figure.html slug="mixamo-auto-control-rig" name="character" side="left" alt="A Mixamo character with the control rig built in Maya" caption="A rigged Mixamo character." %}

## Requirements

Maya 2024 or later (tested in 2024, 2025 and 2027; Maya 2026 uses the same Python as 2025) and a character autorigged by mixamo.com. Characters and animations are not included.

## Credits and rights

This is an unofficial community update, not an Adobe or Mixamo release. Adobe and Mixamo do not support it, and it is provided as is. The original tool's About text credits Dan Babcock as creator and Paolo Dominici for additional code, and carries the notice "Copyright Mixamo www.mixamo.com 2012-2015." Those credits and notices remain applicable to the original work.
