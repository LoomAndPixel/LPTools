---
layout: doc
title: fSpy Importer for Maya Documentation
description: "Install the free fSpy Importer for Maya, import an .fspy project, and get a matched camera, image plane and projection shader."
date: 2026-10-15
tool: fspy-importer-maya
nosupport: true
---

fSpy is free, open-source camera matching software by Per Gantelius. This importer is free and open source too, under GPL-3.0-or-later. It follows his official fSpy importer for Blender.

## Requirements

Maya 2025 or 2027 (Python 3).

## Install

Pick one of the two ways.

**Drag and drop.** The free download on [Gumroad](https://lptools.gumroad.com/l/fspyCameraMaya) comes with `fSpyImporter_drag_and_drop_install.py`. Unzip it and drag that file into a Maya viewport. The importer opens, and its **FSPY** button goes on the LP Tools shelf, with an entry in the LP Tools menu. To remove it, choose LP Tools menu > fSpy Importer > Uninstall.

**By hand, with two lines of Python.**

1. Copy `lp_fspy_importer_maya.py` and `fspy_icon_128.png` into your Maya scripts folder, `Documents\maya\scripts`. The icon is optional and is the logo in the window.
2. Restart Maya, then run this in the Script Editor (Python tab):

```python
import lp_fspy_importer_maya
lp_fspy_importer_maya.show()
```

To make a shelf button, select the lines and middle-mouse-drag them onto a shelf.

**Upgrading from `fspy_maya.py`:** the script was renamed to `lp_fspy_importer_maya.py`. A small `fspy_maya.py` still comes with it so old shelf buttons keep working. Copy both, or update the button to the lines above.

## Import a project

{% include figure.html slug="fspy-importer-maya" name="ui-desc" side="right" alt="fSpy Importer window in Maya" caption="Pick an .fspy project and import." %}

Pick a `.fspy` file in the window and import it. The importer creates:

- **A matched camera** with fSpy's position, rotation and field of view. If you moved the principal point in fSpy, the film offset is set to match.
- **An image plane** showing the photo, pushed far behind the scene so it doesn't hide your geometry.
- **The render resolution** set to the photo's size.
- **A projection shader**, named `<name>_PROJ_mat`, that projects the photo through the camera onto whatever you assign it to. If one with the same name already exists, it is reused and pointed at the new camera.

The photo stored inside the `.fspy` file is saved next to it, as a `.jpg` or `.png`. The whole import is one undo step.

## Options

- **Up axis:** Auto picks fSpy's up axis for you, or choose it yourself.
- **True scale:** if you set a reference distance in fSpy, the camera comes in at real-world scale in your scene's units.
- **Lock camera:** locks the transform and lens so the match can't be nudged by accident.

## Without the window

```python
lp_fspy_importer_maya.import_fspy(r"C:\path\to\shot.fspy")
```

## No fSpy installed?

Camera Match for Maya does the whole match inside Maya and can save `.fspy` files.
