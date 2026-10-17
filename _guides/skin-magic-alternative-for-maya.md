---
layout: guide
title: Skin Magic Not Working in Maya 2025? Building a Replacement
seo_title: Skin Magic Alternative for Maya 2025 and 2027
crumb: Skin Magic not working in Maya
description: "Skin Magic stops with \"No module named 'pymel'\" in Maya 2025 and newer. Why, and how I am rebuilding a skin weights tool from scratch."
date: 2026-10-15
faq:
- q: Why does Skin Magic not work in new versions of Maya?
  a: "Its last release was tested up to Maya 2023. In Maya 2025 and 2027 it stops on its first lines with \"ModuleNotFoundError: No module named 'pymel'\", because it is built on PyMEL, which newer versions of Maya no longer install by default."
- q: Is there a Skin Magic alternative for Maya 2025 and 2027?
  a: "I am building one. It is a new tool written from scratch for Python 3, not a patched copy of the old one, and it is not released yet."
- q: Is Skin Weights for Maya available?
  a: "Not yet. It is in development and not listed, and its name is provisional. This page follows its progress."
---

If you rig characters in Maya, you probably know **Skin Magic**. It made editing skin weights quick: select some vertices, see every influence, change the numbers, move on. Then newer versions of Maya came out, and it stopped opening.

Skin Magic itself was based on the skinning tools in **3ds Max**, which use a similar approach: a list of influences for the selected vertices, with numbers you set directly. That workflow is a big part of why Max riggers like it, and why I wanted it back in Maya.

I started to remake it. It is **not released yet**. This page is a look at what I learned, with frames from my development demo.

## The error you'll see

Skin Magic's last release had already moved to Python 3, and it was tested up to Maya 2023. In Maya 2025 and 2027 it stops on line 176, before its window ever opens:

```
ModuleNotFoundError: No module named 'pymel'
```

Skin Magic is built on PyMEL, a Python library that older versions of Maya installed for you. Newer versions make it an optional extra, so the very first import fails. I ran the original in both Maya 2025 and 2027 to confirm it.

## Why not just fix it?

The obvious plan was to install PyMEL and patch whatever broke next. I looked at it and decided against it:

- It had **many problems in current Maya**, not one or two, and each fix exposed another.
- It carried **no license**, so I could not build on its code.

So I treated it as a feature list and nothing more. I wrote the new tool from scratch, using Maya's own modern API with no PyMEL, and designed the parts around how rigging actually feels in Maya today.

## What it does

Select vertices and you see every influence on them, with the weights. From there:

{% include figure.html slug="skin-weights" name="select" alt="Skin Weights window in Maya next to a mannequin arm with selected vertices and a red weight overlay" caption="Select vertices to see each influence and its weight in a list, with the weights drawn as color on the mesh." %}

- **Set, add or scale** weights for the selected influence, with locks so a joint you have finished never changes.
- **Drag a live slider** and watch the mesh deform as you move it.
- **Smooth, copy, paste and normalize** weights, and limit the number of influences per vertex.
- **Mirror** weights across the body.
- **Bind** a mesh without leaving the panel, using closest joint in the hierarchy, closest distance or heat map.
- **Save and load** weights as files.

{% include figure.html slug="skin-weights" name="slider" alt="Skin Weights window with the live slider being dragged while the elbow of the mannequin deforms" caption="The live slider. The mesh updates while you drag, and one undo step lands when you let go." %}

## Things that were harder than they look

### Seeing the result without leaving the tool

Weights are easy to read as numbers and hard to judge as numbers. The panel has a **flex** control that bends the selected joint so you can test a weight and then put the joint back. A bad weight shows up in a second instead of after you go back and forth between a pose and the weight editor.

{% include figure.html slug="skin-weights" name="flex" alt="The mannequin forearm bent at the elbow with the red weight overlay following the bend" caption="Flexing a joint to check the bend without touching the animation." %}

### Weight colors

I did not want to add color sets or any other data to your mesh just to show weights. Skin Weights draws its colors as a **display-only overlay** that is never saved into the scene. It shows one influence as a ramp, or every influence in its own hue, and follows every edit and pose.

{% include figure.html slug="skin-weights" name="colors" alt="Mannequin with each joint's skin weights drawn in a different color across the body" caption="All influences at once, each with its own hue. The overlay updates as the weights and the pose change." %}

Getting that overlay to appear in the viewport and stay out of saved files, without marking your scene as changed, took more work than most of the editing features.

### Weight rules people forget

Every operation has to obey the same rules, or the numbers drift:

- **Locked influences never change**, and the unlocked ones share what is left.
- **Maximum influences** is enforced after every edit.
- When the only unlocked weight on a vertex goes down, the rest goes to the closest unlocked joint instead of vanishing.

### Mirroring

Mirroring weights sounds simple until the left and right joints are not named in a perfect pattern. It works in bind pose and pairs joints by name first, then by mirrored position as a fallback. It also warns you when vertices have no match.

{% include figure.html slug="skin-weights" name="mirror" alt="Mannequin with both arms raised and matching weight colors after mirroring from one arm to the other" caption="Fix one arm, mirror it to the other." %}

### Undo

A live slider writes weights many times a second, and you do not want fifty undo steps for one drag. The preview writes happen without undo, and a single undoable write lands at the end.

## Where it stands

- Version 1.0.0 works in Maya 2025 and 2027, with automated tests passing in both.
- It is not released, there is no date, and nothing is listed yet. The name is provisional too.
- Next up are copying weights between different meshes by closest point and a quick way to select vertices that failed to mirror.
- I still want to try it on a real production rig. A mannequin is a good test but not the same as a full character.
- I deliberately skipped a paint tool and kept this about numbers, selection and speed.

I will update this page as it moves.
