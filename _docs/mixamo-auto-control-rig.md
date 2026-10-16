---
layout: doc
title: Mixamo Auto Control Rig for Maya Documentation
description: "Install the Mixamo Auto Control Rig Python 3 update in Maya 2024 to 2027, rig a Mixamo character, import animation and bake it to controls."
date: 2026-10-15
tool: mixamo-auto-control-rig
nosupport: true
---

This is an **unofficial community update** of Mixamo's Auto Control Rig v1.6.0, ported to Python 3. It is not an official Adobe or Mixamo release, and Adobe and Mixamo do not support it. It is free and shared as is, with no support and no warranty. The original credits (Dan Babcock as creator and Paolo Dominici for additional code) and the original "Copyright Mixamo" notice still apply to the original work.

## Requirements

- Maya 2024 or later. Tested in Maya 2024, 2025 and 2027. Maya 2026 uses the same Python as 2025.
- A character autorigged by Mixamo, imported in its original pose or T-pose.

Characters and animations come from [mixamo.com](https://www.mixamo.com/) and are not included.

## Install

1. Unzip the download. Copy the whole `MayaAutoControlRig` folder into your Maya scripts folder, `Documents\maya\scripts`.
2. Restart Maya, then run these lines in the Script Editor (Python tab):

```python
import MayaAutoControlRig
MayaAutoControlRig.UI.Main_UI.MIXAMO_AutoControlRig_UI()
```

To make a shelf button, select the lines and middle-mouse-drag them onto a shelf. The file `Mixamo_Auto_Control_Rig_v_1_6_1.py` in the download holds the same lines.

{% include figure.html slug="mixamo-auto-control-rig" name="window-desc" side="right" alt="Mixamo Auto Control Rig window in Maya" caption="The Rig tab, with the character ready to rig." %}

## How to use

1. Download a character from mixamo.com as an FBX and import it into Maya.
2. In the **Rig** tab, click **Rig Character**.
3. Download an animation from mixamo.com. In the **Animate** tab, click **Import Animation to Control Rig** and pick the file.
4. Edit on the controls. **Bake Animation to Controls** and **Clear Animation Controls** let you move between the imported animation and your own keys.
5. Use the **Export** tab to send the result out, or **Batching** to process many files.

## What you get

{% include figure.html slug="mixamo-auto-control-rig" name="character" side="left" alt="A Mixamo character with the control rig in the Maya viewport" caption="A rigged Mixamo character with its controls." %}

- **FK/IK arms and legs** that follow the animation data with no baking.
- **Keyable `AnimDataMult` attributes** that exaggerate or ignore the animation data.
- **Bake or clear** the controls at any point in time, and the animation is preserved.
- **Facial controls** on FacePlus-compatible characters, with Osipa style controls, eye rotation and aim.
- **Hands and feet** custom attributes, and an optional pelvis ("hula") control.
- **Dynamic joints and chains**, a baked FK skeleton export, and batch import and export tabs.

## More detail

`Mixamo_Auto_Control_Rig_v_1_6_1_DOCUMENTATION.pdf` in the download covers the original tool in more depth. It was written for version 1.6.0, so some screens look slightly different. The changelog lists what changed in 1.6.1, a Python 3 port that works in Maya 2024 to 2027.
