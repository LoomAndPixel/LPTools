---
layout: doc
title: Repack Documentation, PBR Texture Packer for Windows
description: "Get started with Repack: drop in texture folders, pick a preset for Unreal, Unity, Godot or glTF, check the 3D preview and export packed ORM and Mask Maps."
date: 2026-10-18
tool: repack
---

## Requirements

Windows 10 or 11, 64-bit. A graphics card with OpenGL 3.0 shows the 3D view. If yours doesn't, Repack offers a software mode that restarts the app and works on any machine. No Python or other software needs installing.

## Install and update

There are two downloads. Use whichever you like.

**Installer (recommended):** run `Repack-0.9.3-setup.exe` and follow the steps. By default it installs for your own user account only, into `AppData\Local\Programs\LP Tools\Repack`, so Windows doesn't ask for an administrator password. The first page also lets you install for all users instead, into `C:\Program Files\LP Tools\Repack`, which does ask for administrator rights. It adds Repack to an LP Tools folder in the Start menu and can add a desktop shortcut. To update, run the new installer: it replaces the old version. To remove Repack, use Windows Settings, Apps: it asks whether to delete your presets and settings too, and the default is to keep them.

**Portable zip:** unzip `Repack-0.9.3-portable.zip` anywhere you like, for example into `C:\Tools`. It makes one folder called `Repack`: start `Repack.exe` inside it. Nothing is installed. To update, unzip the new download over the old folder. To remove Repack, delete the folder.

Both keep your presets and settings in `Documents\LP_Tools\Data\Repack`, so updating or removing Repack never touches them. Your license also stays on the computer when you remove Repack, so installing it again doesn't use another seat.

**If Windows says "Windows protected your PC":** this beta is not code signed yet, so SmartScreen may show this box the first time. Click **More info**, then **Run anyway**. You can also right click the zip, choose Properties, tick **Unblock**, and unzip afterwards. Repack never uploads your files. It goes online only to check your license key (when you enter it, then about once a month, sending just the key) and, optionally, once a day to look for a newer version. **Help > Check for updates automatically** turns off the second one.

## Activating

Without a license key Repack runs as a demo: you can load textures, use the graph, the 3D view and the checks, but **Export** and the watch folder are locked (the bundled sample can still export). A strip at the top shows **Unlicensed**; click it, or use **Help > Enter license key...**, and paste the key from your Gumroad receipt email, then press **Activate**. An Individual license works on 3 computers and a Studio license on 10. Reinstalling on the same computer doesn't use another one. **Help > About Repack** shows who it is licensed to. Repack checks the key again about once a month in the background. If you are offline it keeps working, and it only goes back to demo mode if Gumroad says the key was refunded or is not valid. For a new computer, or to reset your count, email support@lptools.store.

**Where the license is kept:** on your computer, in `%LOCALAPPDATA%\LP_Tools\Repack`. Removing or reinstalling Repack leaves it there on purpose, so a reinstall doesn't use another of your computers. Deleting that folder doesn't free the computer on our side: email support@lptools.store and we'll free it. The key is only checked with Gumroad when you activate and about once a month, and only the key is sent.

## Getting started

1. Drag a folder of textures, or the image files themselves, onto the window. You can also use **Folder** or **Files** on the left, or the **A** (folder) and **S** (files) keys. New here? **Try a sample** on the start card loads a small rock material so you can see how it works.
2. Repack groups the files into material sets and works out what each file is from its name. The list on the left shows one row per set, and the files of the selected set sit below it.
3. Pick a preset on the right, for example **Unreal Engine**.
4. Look at the graph in the middle: every file is a node, wired into the outputs the preset writes. The 3D view shows the material on a sphere.
5. Press **Export** (or **E**). Repack writes one folder per set.

Nothing is written until you press Export, and your source textures are never overwritten.

## Map names it recognises

Repack reads the end of the file name and skips resolution and file-type parts such as `2k` or `jpg`.

| Map | Names |
|---|---|
| Base color | diff, diffuse, albedo, basecolor, col, color |
| Normal | nor, normal, nrm, norm (add `gl` or `dx` to say which kind) |
| Roughness | rough, roughness, rgh |
| Gloss | gloss, glossiness, smoothness |
| Metallic | metal, metallic, metalness |
| Ambient occlusion | ao, occlusion, ambientocclusion |
| Height | disp, height, displacement, bump |
| Opacity | opacity, alpha, transparency |
| Emissive | emissive, emission, emit, glow |
| Specular | spec, specular, refl |
| Subsurface | sss, subsurface, scatter, translucency |
| Packed maps | ORM, ARM, RMA, MaskMap and the Unity metallic and specular smoothness maps |
| Short suffixes | `_D`, `_N`, `_R`, `_M`, `_E` |

If a file is wrong or unknown, change its kind in the dropdown on its row. Set the **Normal** (GL or DX) and **Metal / Roughness** or **Specular / Gloss** options above the file rows to say how your source maps were authored. You can undo and redo these edits with Ctrl+Z and Ctrl+Y.

## Presets and the channel matrix

Presets built in: Unreal Engine, Unity URP, Unity Built-in, Unity URP (Specular), Unity Standard (Specular), Godot, glTF, Separate maps with a GL normal, Separate maps with a DX normal, and **Convert only**. A preset is a list of output files, and each output has a channel matrix: which source goes into R, G, B and A, with an Invert box per channel. Change it and the graph follows, and the other way round.

- **Normal maps:** Repack flips the green channel between DirectX and OpenGL for you, based on what you said the source is and what the preset wants.
- **Roughness and gloss, metal and specular:** converted as needed, so a specular and gloss set can feed a metal and roughness preset.
- **Save as...** stores your changed preset under a new name. **More...** exports to several presets at once.
- **Convert only** keeps every file as is and only changes format, size or bit depth.

**Unused files.** Files the preset doesn't read, such as the height map for Unreal or an SSS map, are exported as they are by default, under their own names (converted to the format, size and bit depth you chose). The checkbox **Also export unused files as is** under the preset controls it. When it is checked, each unused file has its own Write node in the graph. If you delete one of those nodes, only that file is left out for that material, and the box shows a dash (partly checked). Ctrl+Z brings the node back, and clicking the box puts every unused file back. Unchecking the box skips them all. With Convert only the box is locked on, because every file is already converted.

## The graph

Each source file is a Read node with pins for its channels. Wires run to the pins of the output nodes. Drag from a pin to wire it, right click a wire to unplug it, and right click an empty spot for every node you can add (a Write node, or Levels, Clamp, Threshold, Renormalize, Resize and Invert, each followed by the channel or output it goes on; on a roughness or gloss channel the Invert node adds a line saying Rough to Gloss or Gloss to Rough), and right click a wire or a Write node to add an operation there or rename it. Conversions the preset needs also appear on their own when a file and an output disagree (roughness and gloss, metal and specular), so most of the time you never add them yourself. The wheel zooms, the middle mouse button pans, **Fit** (F) frames everything and **Tidy** lays the nodes out again. Click a node to compare before and after at the bottom. Files the preset doesn't use get a Write node of their own, wired straight from their Read node, so you can see they are exported. Delete that node to leave the file out, or right click its Read node and choose **Add Write node** to bring it back.

## The 3D view

The 3D view shows the material on a sphere, a cube, a plane or a draped cloth. Drag to orbit and use the wheel to zoom.

- **Sources / Export:** Sources shows your files as they are. Export shows what the preset will write, decoded the way the target engine reads it, so a wrong channel or a flipped normal shows up before you export.
- **Environment:** Small studio, Outdoor sky or Indoor room, with an exposure box. **More** has the Displace amount, the mid level, the mesh density, Preview height and more.
- **Displace:** the sphere and the cloth really move with the height map. Export mode only shows height when the preset exports it, or when you turn on **Preview height**.
- **Lit** can be switched to show one map raw, such as roughness.

## Output options

Open the **Output** section on the right. Format (PNG, TGA, JPG, TIFF, EXR or DDS), resize (keep, 512 to 8K or nearest power of two), bit depth (auto, 8, 16 or 32, with EXR as half or full float) and a dither switch for 16 to 8 bit. **Renormalize normal maps** cleans up resized normals.

**DDS for games:** choose DDS and Repack compresses each map the way engines expect: base colour and other colour maps as BC7 (sRGB), normal maps as BC5, single channel maps (roughness, metal, AO, height) as BC4, packed maps such as ORM as BC7, and HDR data as BC6H. **Mipmaps** (on by default) writes the full chain of smaller sizes, and **Compression** can switch to smaller BC1 / BC3 files. Bit depth, dither and the EXR option are set by the compression, so they grey out. Sides are rounded up to a multiple of 4, and Repack warns when a size isn't a power of two. DDS is made with Microsoft's free texconv tool, which comes in the download.

**File formats.** Repack reads PNG, JPG, TIFF, TGA, EXR, BMP, HDR and DDS, and writes PNG, TGA, JPG, TIFF, EXR and DDS. Not supported yet: PSD, KTX2 and WebP.

Files and folders are named with templates. The defaults are `{set}_{suffix}` and `{folder}\Repack_{preset}`. Available tokens: `{set}`, `{suffix}`, `{preset}`, `{ext}`, `{res}`, `{folder}` and `{date}`. A live preview shows the result. `{set}` is the name Repack detected for the material. To use another name for one set, type it in the name field above the file rows (clear it to go back to the detected name). Right click an output's Write node in the graph and choose Rename to change its suffix, for example `D` instead of `BaseColor`. To send everything to one place, type a folder in **Output folder**.

## Checks

The Checks panel under the graph points out things that usually cause trouble: mixed sizes, sizes that aren't a power of two, normal maps that aren't unit length or look like the wrong convention, metal maps with too many in-between values, a roughness or occlusion map that is constant or all white, an output with no source, and files whose kind isn't set. Some notes have a fix button.

## Queue, watch folder and UDIM

- **Queue:** exporting adds one job per set and preset. The bar at the bottom shows progress. Open it with **Show queue** to cancel, retry failed jobs or open the output folder. Jobs run on several cores, set by **Workers**.
- **Watch folder:** **File > Watch folder...** converts every new set that appears in a folder with the preset and format you have selected. **Stop watching** ends it.
- **UDIM:** tiles such as `1001` and `1002` are grouped into one set. A tile box lets you pick which tile the graph and 3D view preview, and every tile is exported.

## Shortcuts

| Action | Keys |
|---|---|
| Add folder | A |
| Add files | S |
| Export | E |
| Undo, redo | Ctrl+Z, Ctrl+Y |
| Fit the graph | F |

Window size, panes and options are remembered. **Help > About Repack** shows the version and build date. Third party components and their licenses are listed in `NOTICES.txt` in the download.

## FAQ

**Does Repack change my original textures?** No. It only writes new files into the output folder.

**The 3D view says it needs OpenGL 3.0.** Use the button in the panel to switch to software OpenGL. Repack restarts and the view works on any computer, a little slower.

**A map shows as unassigned.** Its name doesn't say what it is. Pick its kind in the dropdown on its row.

**Does it need internet?** Only briefly: to activate your key, for a check about once a month, and for the optional update check. Everything else works offline.

**A DDS normal map looks red and green in a viewer.** That is expected: BC5 stores only two channels, and Unreal and Unity rebuild the blue one when they load it.

**Where are my presets?** In `Documents\LP_Tools\Data\Repack`. Removing Repack doesn't touch them.

Questions or a problem? Write to me at support@lptools.store.
