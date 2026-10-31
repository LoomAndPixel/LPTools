---
layout: doc
title: KeyForge for Maya Documentation
description: "Install KeyForge for Maya, learn how the sliders work, and set up hotkeys, the Pose Library and Selection Sets."
date: 2026-10-15
tool: keyforge
---

## Requirements

Maya 2024, 2025, 2026 or 2027. Tested in Maya 2024, 2025 and 2027. Maya 2026 runs the same Python as 2025.

## Install

Pick one of the two ways.

**A. Drag and drop (recommended)**

1. Unzip the whole download.
2. Start Maya and drag `KeyForge_drag_and_drop_install.py` into a viewport.

KeyForge opens, its **KEY** button goes on the LP Tools shelf, and it gets an entry in the LP Tools menu. Click the button to show or hide the bar by the Time Slider. Maya remembers which when you restart. One install covers Maya 2025, 2026 and 2027. In another version, the button appears the first time you start it.

To remove it, choose LP Tools menu > KeyForge > Uninstall.

**B. By hand, with two lines of Python**

1. Copy the whole `lp_keyforge` folder from `KeyForge\python\py310` (Maya 2024), `KeyForge\python\py311` (Maya 2025 or 2026) or `KeyForge\python\py313` (Maya 2027) into your Maya scripts folder, `Documents\maya\scripts`.
2. Restart Maya, then run these lines in the Script Editor (Python tab):

```python
import lp_keyforge
lp_keyforge.toggle()
```

To make a shelf button, select the lines and middle-mouse-drag them onto a shelf.

## Update

Drag `KeyForge_drag_and_drop_install.py` from the new download into Maya. It replaces the old version, including a copy you put in your scripts folder by hand. If you installed by hand, replace the files in `Documents\maya\scripts` and restart Maya. Your settings are kept either way.

If you have KeyForge Lite installed, installing KeyForge removes it for you.

## Start here

{% include figure.html slug="keyforge" name="ui" alt="The KeyForge bar docked under the Maya Time Slider" caption="The KeyForge bar, docked right under the timeline." %}

- **The dot next to "KeyForge"** shows what the sliders will change: the keys selected in the Graph Editor, the highlighted Time Slider range, or the current frame.
- **Click anywhere on a slider and drag.** While you drag, the slider shows what the end you are heading to means, plus the value. One Ctrl+Z undoes the whole drag.
- **Right-click anything for options.** A right-click on a slider gives a floating, movable, resizable slider with fine ranges and Overshoot.
- **The ? button** opens the Quick Guide.
- **If a tool can't run,** the bar tells you why.

{% include figure.html slug="keyforge" name="floating-slider-desc" alt="A floating KeyForge slider with fine ranges" caption="Right-click a slider for a floating, resizable slider." %}

## Hotkeys

Open **KeyForge Tools** (gear menu, or right-click the bar), pick a tool in the Catalog, click the Hotkey box and press the keys. If the key is already taken, KeyForge asks before it replaces it. **Clear** takes the key away. Try the pop-up slider first. You can also make the S key run Smart Key, or use **Assign hotkeys** on the bar's right-click menu to work in Maya's Hotkey Editor.

## The Graph Bar

{% include figure.html slug="keyforge" name="graphbar-1row" alt="The KeyForge Graph Bar in one row inside Maya's Graph Editor, with the channel fields beside the tools" caption="The KeyForge Graph Bar in one row: the tools, then the channel fields, right under the Graph Editor's own buttons." %}

The Graph Bar puts the same tools inside the Graph Editor, so you can use them while you look at curves. In a wide editor it is one row, with the tools and the channel fields side by side. When the editor is narrower, it switches to two rows by itself, with the channel fields below the tools, so nothing gets hidden. Only a very narrow editor folds the last tools into a » menu. Click the **?** at the right end for a short guide.

{% include figure.html slug="keyforge" name="graphbar-2row" alt="The KeyForge Graph Bar in two rows, with the channel fields on the second row" caption="In a narrower editor it switches to two rows by itself: tools above, channels below." %}

**Channel fields.** Translate, Rotate and Scale of the object picked in the Graph Editor's list, like the Channel Box:

- **Colors:** red means keyed on this frame, pink means animated but between keys, yellow means connected, grey means locked. A channel your rigger hid is left empty and can't be changed.
- **Several at once:** click and drag across the small labels (Tx, Ty, Tz and so on) to select channels, and hold Ctrl to add more. Locked and hidden channels are skipped. Then type a value to set them all, or middle-drag a box to scrub them together (Ctrl for fine, Shift for coarse). One Ctrl+Z undoes a whole scrub.
- **Right-click a channel** for Key, Remove key, Key Translate, Rotate or Scale, Lock and Unlock, Mute and Unmute, Break connections, Reset to default, and Copy and Paste value.

## Pose Library

{% include figure.html slug="keyforge" name="pose-library" side="right" alt="KeyForge Pose Library with pose thumbnails" caption="The Pose Library saves poses with a thumbnail." %}

Open it from the **Poses** button in KeyForge Tools, or from the Pose Library button on the bar. It is a persistent pose browser:

- **Characters and folders:** characters are listed on the left, each with the folders you make inside it (Face, Body, Hands, named however you like). Use **+ Character** and **+ Folder**, and right-click to rename or delete. Poses saved without a character go to *Unassigned*.
- **Thumbnails:** pick a character or folder to see its poses as a grid on the right. The **Thumbnails** slider, or Ctrl + mouse wheel, sets how many fit in a row, from 2 to 8.
- **Save:** select the controls, choose a character and folder, and save. KeyForge also captures the viewport as the thumbnail, a visual reference only that is not part of the pose data. Saving over an existing name asks before it replaces it.
- **Apply:** double-click a pose, or select it and press **Apply**. Use the blend slider to bring a pose in part of the way. Applying makes keys on animated channels at the current frame and sets channels that aren't animated directly, all in one undo step.
- **Organize:** drag poses onto a folder to move them, or use **Move...**. Search looks through every character. Right-click a pose to replace it with the current pose, retake its thumbnail or rename it, and use **Delete** to remove poses.
- **Across rigs:** controls are matched by short name, so a pose saved on one rig applies to another with the same control names, even in a different namespace.
- **Where it lives:** pose data is stored as JSON under `Data/KeyForge/PoseLibrary/<Character>/<Folder>/` in your LP Tools data folder, outside your scenes. A library from an earlier build is sorted into this layout the first time it opens.

<div style="clear:both"></div>

## Selection Sets

{% include figure.html slug="keyforge" name="selection-sets" side="left" alt="The KeyForge Selection Sets window with one button per set" caption="The Selection Sets window: one button per set, with its control count." %}

Selection Sets are named groups of controls, one button each. Open the window from the Selection Sets button on the bar (it sits beside Pose Library in two rows) or from the Select group in the gear menu.

1. Select some controls.
2. Click **+ New Set from Selection** and name it, for example Face, Eyebrows or Left Hand.
3. Click the set any time to select its controls.

- **Click** selects the set, **Shift + click** adds it to your selection, and **Ctrl + click** removes it.
- **Right-click** a set to replace its controls with your current selection, add your selection to it, remove your selection from it, rename it or delete it.
- The window grows and wraps as you make more sets, and shows how many controls each one holds.
- Sets are ordinary Maya object sets saved in the scene, so they travel with the file.

<div style="clear:both"></div>

## One row or two, workspaces and slider slots

The bar starts as one slim 32 pixel row: the 14 everyday buttons and three sliders. The rows button at the far left switches to two rows, which show every button on top and up to five sliders on the row below.

{% include figure.html slug="keyforge" name="ui-two-rows" alt="The KeyForge bar in two rows" caption="Two rows: every button on top, five sliders below." %}

- **Workspaces** (gear menu > Workspace): Essentials, Blocking, Polish, Layout and Rig, Full, and Classic, the exact 0.7 bar. A workspace never changes the row count. Save the current bar as your own preset from the same menu.
- **Slider slots:** each slot has a small arrow that swaps its tool for any of the 25 sliders, and the choice is remembered.
- **The gear:** the switches (Overshoot, Smart Euler, Channel Box filter, Auto Tint, Pause Viewport), Workspace, every command in groups, Settings, KeyForge Tools and the Quick Guide. Small pills next to the target dot show the Channel Box filter and Overshoot while they are on.

## KeyForge Tools

{% include figure.html slug="keyforge" name="window" side="right" alt="The KeyForge Tools window, Catalog tab" caption="The Catalog lists every tool with its hotkey and a star." %}

Open it from the gear menu or by right-clicking the bar. The **Catalog** lists every tool by group, with search. Click a star to put a tool on the bar (in two rows it asks whether the tool shows in both modes or only in two rows). Pick a row to read what it does, give it a hotkey, run it, or, for a slider, drag the slider right there.

{% include figure.html slug="keyforge" name="customizer" side="left" alt="The KeyForge Tools window, Bar tab" caption="The Bar tab: drag to reorder what shows on the bar." %}

The **Bar** tab lists the bar from left to right. Drag to reorder, add a separator, or remove an item. The bar updates as you go, anything that doesn't fit moves into the » menu, and **Undo my changes** puts it back the way it was. The same tab has the two-row switch, group labels, text labels, size and colored icons. The **Settings** tab holds the options for the tools.

## Sliders

- **Blend to a pose:** Tween, Blend to Neighbors, Default, Frame (with a reference frame box), Mirror, Buffer, Mirror from Frame and Partial Undo.
- **Shape:** Pull / Push, Scale From (average, default, frame or neighbor key), Smooth / Rough, Ease In / Out, Blend to Ease and Wave.
- **Timing and cycles:** Gap Mender, Bridge to Neighbors, Blend to Cycle and Time Shift (with stagger).
- **World space:** Tween, Neighbors, Frame, Cycle, Align, Copied Xform and Relationship, all keeping hands and feet where they belong.

## Tools

- **Keys and timing:** Smart Key, copy, cut and paste keys and key times, nudge, insert and remove inbetweens, share and snap key times, bake on ones to fours, and simplify.
- **Tangents:** Smart, Clean, Smooth and Contact recipes, every Maya tangent type, blend toward any of them, cycle match and Euler filter.
- **Key colors:** tint keys red, yellow or green, then jump to, play or delete keys by color, plus Auto Tint.
- **Pose and mirror:** copy and paste pose, reset, mirror pose and animation (names like Arm_L, armL, leftArm, or pairs you save) and preferred default poses.
- **World and rig:** copy and paste world transforms and relationships, align, Global Offset, space switching that keeps the world position, temp controls, and temp pivots you rotate controls around. These are keyed and the rig is never touched.
- **Navigate and view:** previous and next key by color, play keys only, play on twos, time bookmarks, visibility modes, isolate, live motion trails with a tick per frame, and Graph Editor and Channel Box helpers.

## Try it first

[KeyForge Lite](/tools/keyforge-lite/) is free and gives you the Tween, Blend to Neighbors and Pull / Push sliders plus Smart Key, Delete Keys, Nudge, Copy / Paste Pose, Reset Pose and Tint.
