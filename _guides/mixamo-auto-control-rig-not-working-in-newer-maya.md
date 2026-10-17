---
layout: guide
title: Mixamo Auto Control Rig Not Working in Maya 2022 and Later
seo_title: Mixamo Auto Control Rig Not Working in Maya
crumb: Mixamo Auto Control Rig not working in newer Maya
description: "Why the old Mixamo Auto Control Rig script fails in newer versions of Maya, and a free Python 3 update that works in Maya 2024, 2025 and 2027."
date: 2026-10-15
tool: mixamo-auto-control-rig
faq:
- q: Why does Mixamo Auto Control Rig not work in newer Maya?
  a: "The original script was written for Python 2. Maya 2022 made Python 3 the default, so the old script stops loading with syntax and import errors."
- q: "What does \"No module named 'Utils'\" mean in Mixamo Auto Control Rig?"
  a: "It is the original Python 2 script failing in Python 3. Version 1.6.0 imports its own modules the Python 2 way, which Python 3 does not allow, so Maya 2022 and later stop on the first line. A Python 3 port fixes it."
- q: Did Adobe drop Maya support for Mixamo?
  a: "Adobe no longer maintains the Maya Auto Control Rig script and has not updated it for Python 3. Adobe has not made a clear public announcement, and the Mixamo website itself still works for downloading characters and animations as FBX."
- q: Is there a Mixamo Auto Control Rig for Maya 2024, 2025 or 2027?
  a: "Yes. An unofficial Python 3 port of version 1.6.0 works in Maya 2024, 2025 and 2027. It is free and is not an official Adobe or Mixamo release."
---

If you ran the old Mixamo Auto Control Rig script in a recent Maya and watched the Script Editor fill up with red, it's not your character and it's not you. It's Python 2.

## Why it stopped working

Mixamo's Auto Control Rig was written for **Python 2**. Starting with Maya 2022, **Python 3 is the default**, and the old code uses Python 2 syntax and modules that no longer exist there. The result is syntax errors or import errors the moment you load it. The script was never updated, so there was no official fix.

## The error you'll see

Run the original v1.6.0 shelf script in Maya 2022 or later and it stops on its very first import:

```
ModuleNotFoundError: No module named 'Utils'
```

The package imports its own modules the Python 2 way (`import Utils`), which Python 3 no longer allows. Fix those imports and the next wall is this one, in five of its files:

```
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
```

That's Python 2's old `print "..."` statement. Neither error has anything to do with your character, your scene or your Maya install. I ran the original in Maya 2025 to confirm them.

## Why there is no official fix

Adobe, which owns Mixamo, has dropped support for the Maya script. It is not a bug waiting for a patch. Adobe stopped maintaining the Maya rigging tools after it retired Fuse in 2020, and the Auto Control Rig has not been updated since. Adobe has not published a clear announcement about this, so what I know comes from Adobe's own community threads, where users report the Maya script no longer being maintained, and from the fact that it never got a Python 3 update.

The Mixamo website itself still works. You can still download characters and animations as FBX files. What is missing is the Maya side of it, which is the part this update brings back.

## The fix

A community compatibility update ports the script to Python 3. It keeps the original tool's behavior and is **free**. It is not an official Adobe or Mixamo release, and Adobe and Mixamo do not support it.

- Built from the original Auto Control Rig v1.6.0.
- Works in **Maya 2024, 2025 and 2027**. Maya 2026 uses the same Python as 2025.
- Original authors credited. See the tool page for the credits and the no-rights note.

{% include figure.html slug="mixamo-auto-control-rig" name="window-desc" alt="Mixamo Auto Control Rig window in Maya" caption="The Rig, Animate and Batcher tabs, now running in current Maya." %}

## What it does

Once it runs, it builds a control rig on a character autorigged by Mixamo, so you can edit Mixamo motions or keyframe your own animation. It adds FK/IK arms and legs, keyable animation multipliers, bake and clear controls, facial controls on compatible characters, and batch import and export tabs.

## Getting it

See [Mixamo Auto Control Rig for Maya](/tools/mixamo-auto-control-rig/) for the full feature list and download. You will need a character from [mixamo.com](https://www.mixamo.com/), downloaded as an FBX. Characters and animations are not included.

## If you are on Maya 2022 or 2023

The update has been tested in Maya 2024, 2025 and 2027. I haven't tested it in 2022 or 2023, so I can't promise it works there.
