---
layout: doc
title: Repack Documentation, PBR Texture Packer for Windows
description: "Get started with Repack: drop in texture folders, pick a preset for Unreal, Unity, Godot or glTF, check the 3D preview and export packed ORM and Mask Maps."
date: 2026-10-20
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

1. Drag a folder of textures, or the image files themselves, onto the window. You can also use **Folder** or **Files** on the left, or the **A** (folder) and **S** (files) keys. New here? **Try a sample** on the start card loads five small Poly Haven (CC0) materials so you can see how it works; **File > Samples** loads them one at a time, and **File > Load the blend material sample** sets up a brick wall with moss over it.
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
- **Switching presets keeps your extras.** A Normal blend and any generated maps (with their Write nodes and positions) move with you to the new preset, so you never have to rebuild them. If the new preset has no normal output the blend waits and comes back on a preset that has one.

**Unused files.** Files the preset doesn't read, such as the height map for Unreal or an SSS map, are exported as they are by default, under their own names (converted to the format, size and bit depth you chose). The checkbox **Also export unused files as is** under the preset controls it. When it is checked, each unused file has its own Write node in the graph. If you delete one of those nodes, only that file is left out for that material, and the box shows a dash (partly checked). Ctrl+Z brings the node back, and clicking the box puts every unused file back. Unchecking the box skips them all. With Convert only the box is locked on, because every file is already converted.

## Generated maps

When the preset needs a map your files don't have, a bar above the graph offers to make it: **Normal from Height**, **AO from Height**, **Leave AO white**, a flat roughness or metal, and more. Nothing is made until you click. The new map shows in the graph as a dashed teal node marked "generated", with how good the result is: **good** (a close match to a real map), **fair** (approximate), **fake** (guessed from the colours, fine for stylized work) or **flat** (one value everywhere).

- **From a height map:** normal, curvature and AO are good.
- **From a normal map:** curvature is good. Height and AO are fair, because the broad shape of a surface can't be recovered from its normals.
- **From the base colour only:** normal and height are fake, made from the brightness of the colour.
- **Metal** is never guessed. It is a constant (0 by default) you can change.
- **Double click** a generated node to change what it is made from, its strength and its wrapping (keep Wrap on for tiling textures). **Right click** it to use a real file instead, or remove it. A real file in the set always wins, and your source files are never changed.
- Generated maps stay when you switch presets, and removing one also removes the Write node it came with (unless you added an op or tweak to that node). They are saved in the preset, so batch, the watch folder and the command line make them too (`--generate ao`, or `--no-generate` to switch them off).

## Opening files

The installer adds **Repack this folder** to the right click menu of folders and of a folder's empty background, and **Open in Repack** to image files (on Windows 11 they are under **Show more options**, or hold Shift while you right click). Select several images and they open together in one window. You can also drag a folder or files onto Repack.exe or its shortcut. Loading always works; only Export needs a license key. The portable zip adds nothing to Windows. If you switch between a per user and an all users install, the old menu items stay until that copy is uninstalled.

## The graph

Each source file is a Read node with pins for its channels. Wires run to the pins of the output nodes. Drag from a pin to wire it, right click a wire to unplug it, and right click an empty spot for every node you can add (a Write node, or Levels, Clamp, Threshold, Renormalize, Resize and Invert, each followed by the channel or output it goes on; on a roughness or gloss channel the Invert node adds a line saying Rough to Gloss or Gloss to Rough), and right click a wire or a Write node to add an operation there or rename it. Conversions the preset needs also appear on their own when a file and an output disagree (roughness and gloss, metal and specular), so most of the time you never add them yourself. The wheel zooms, the middle mouse button pans, **Fit** (F) frames everything and **Tidy** lays the nodes out again. Click a node to compare before and after at the bottom. Files the preset doesn't use get a Write node of their own, wired straight from their Read node, so you can see they are exported. Delete that node to leave the file out, or right click its Read node and choose **Add Write node** to bring it back.

**Tweaks.** Right click a pin on a Write node and choose **Tweak** (or double click the pin) to change that one channel: Invert, Black and White points, Gamma and Contrast, with a small before and after histogram. A small amber diamond marks a tweaked pin, and the preview and 3D view follow as you drag. Tweaks belong to the output channel, so rewiring keeps them, and they are saved in your preset. They run before any ops on the channel. Normal maps can't be tweaked, and colour maps are tweaked on their stored (sRGB) values. **Clear tweak** or Reset puts a pin back.

**Metal to Specular.** When a set is metal and roughness but the preset wants specular and gloss (or the other way round), an automatic conversion node appears with two outputs on its right: **Base color** (the albedo) and **Specular** (or **Metal** for the reverse). Each goes to the Write pins that need it.

## Blend materials

A blend material lays one material over another by the first one's height map, for example moss that collects in the cracks of a brick wall. It is a row of its own in the materials list, after the sets. Load both materials, right click the brick and choose **Create blend using selected** (with two sets selected, the one you clicked is Material A and the other Material B), or use the blend button under the list for an empty one. Drag a set from the list onto **Material A** or **Material B** in the graph, or click the small arrow on a slot to pick one. **File > Load the blend material sample** makes one from the bundled brick and mossy ground.

{% include figure.html slug="repack" name="blend" alt="A blend material: cobblestone with moss, the three blend nodes, the sliders at the right and the result on a plane" caption="A blend material: Material A, Material B and the Height blend node, with the sliders in a column at the right and the result in 3D." %}

The graph shows three nodes: Material A (the base, its height drives the mask), Material B, and **Height blend**. The controls sit in a column to the right of the graph, and double clicking Height blend opens the same controls plus Material A and B:

- **Material A** and **Material B:** any loaded set (UDIM sets cannot be blended yet).
- **Fill from:** Low areas (the cracks fill first) or High areas (it sits on the peaks, like snow).
- **Coverage** and **Softness:** how much of the surface Material B takes, and how hard the edge is.
- **Use B's height** and **Strength:** B's own bumps push the edge, so it clumps over the border.
- **Tiling:** how many times Material B repeats across A.
- **Breakup, Scale and Reseed:** a soft, seamless noise that varies how much of B shows, so the moss thickens in some places and thins in others instead of following the cracks exactly. Breakup is the amount (0 is off), Scale is the size of the patches, and Reseed picks a different pattern. This hides the repeat of tiled textures.

Both materials go through the preset selected in the main window first (generated maps, workflow, tweaks and ops), then each output is mixed, so a color tweak on the brick shows in the blend. All blends share that one preset. Colors are mixed in linear light and normals as directions. The 3D view shows a blend as exported (it has no source files of its own); switch it to **Blend mask** to see where Material B shows (white). An amber **!** on a slot means that material lacks a map the other has (the default is used); Checks lists each one. Export writes `{A}_{B}_{suffix}` files, for example `brick_4_forest_leaves_02_ORM.png`, for the preset's outputs; type in the name field to change `{A}_{B}`. The files of A and B are never written or changed. Ctrl+Z undoes creating, deleting and each session of the Height blend dialog.

**Blend kits.** **File > Save blend kit** (Ctrl+Shift+S) saves your blends, or only the selected ones, to one `.repackblend` file with the preset they use. Unticked, **Include texture files** keeps the kit small: it points at the texture folders (relative to the kit when they sit under its folder, so a moved project still opens). Ticked, the textures go inside the kit, each file once, so it opens on any computer; embedded textures keep their original licenses. **File > Open blend kit**, **Recent kits**, a double click in Explorer or a drop onto the window adds every blend of the kit to the list and selects the kit's preset. A material that cannot be found shows as a red slot: **File > Locate folder** (or a double click on the slot) points every blend that uses it at its new folder. On the command line, `repack run kit.repackblend [--blend NAME] [--preset ID] [--out DIR]` exports a kit and `repack lint kit.repackblend` checks it.

If the preset has no height output, the blended height is still exported as an extra file (for example `brick_4_moss_Height.png`) while **Also export unused files as is** is on, so a displacement map made by the blend isn't lost.

{% include figure.html slug="repack" name="blend-mask" alt="The Blend mask view on a plane: white where the moss shows" caption="The Blend mask view: white is where Material B shows." %}

## Normal blend

Lay a detail normal map over the base normal, for example fabric or noise over a rock. Assign a file **Detail normal** in its dropdown (or right click an empty spot in the graph and choose **Add normal blend**, which asks for a file from any folder). A **Normal blend** node appears between the base normal and the Write node. Double click it to choose the mode (**RNM** keeps the base surface best, **Whiteout** and **UDN** are simpler and flatter on steep areas), how many times the detail repeats (**Tiling**), its **Strength**, and whether the detail file is GL or DX. The export writes one blended normal file; the detail file isn't exported on its own. Without a detail normal, the blend is skipped. On the command line: `--detail-normal`, `--blend rnm|whiteout|udn|off`, `--detail-tiling` and `--detail-strength`.

The detail normal has its own **Detail normal** Read node: double click it to pick or change the file, from any folder. If the set already has a file named like a detail normal (`detailnormal`, `normaldetail`) it is found and wired to the Detail pin on its own; with none, the node says so. The **Strength** slider is on the Normal blend node itself (0 to 200 percent, 100 in the middle): click the track to jump, drag for a live result, hold Shift for fine steps. The settings dialog has the same slider.

{% include figure.html slug="repack" name="normal-blend" alt="The Normal blend node with its Base and Detail pins and a Strength slider" caption="The Normal blend node: Base and Detail in, the blended normal out, with Strength on the node." %}

## The 3D view

The 3D view shows the material on a sphere, a cube, a plane or a draped cloth. Drag to orbit and use the wheel to zoom.

- **Sources / Export:** Repack opens on Export. Sources shows your files as they are. Export shows what the preset will write, decoded the way the target engine reads it, so a wrong channel or a flipped normal shows up before you export.
- **Environment:** Small studio, Outdoor sky or Indoor room, with an exposure box. **More** has the Displace amount, the mid level, the mesh density, Preview height and more.
- **Displace:** the sphere and the cloth really move with the height map. Export mode only shows height when the preset exports it, or when you turn on **Preview height**.
- **Lit** can be switched to show one map raw, such as roughness.
- **Keys:** **C** steps through the maps (Lit, Base color, Roughness, Metal, AO, Normal, Height and so on), **Shift+C** goes back, and **M** jumps to the lit material and back to the map you were on.
- **Tile (1x1, 2x2, 3x3):** the button at the bottom right repeats the textures on any shape, so you can look for seams. The Inspector has a Tile chip that does the same for a single map, and the before and after view follows it.

## Output options

Open the **Output** section on the right. Format (PNG, TGA, JPG, TIFF, EXR or DDS), resize (keep, 512 to 8K or nearest power of two), bit depth (auto, 8, 16 or 32, with EXR as half or full float) and a dither switch for 16 to 8 bit. **Renormalize normal maps** cleans up resized normals.

**DDS for games:** choose DDS and Repack compresses each map the way engines expect: base colour and other colour maps as BC7 (sRGB), normal maps as BC5, single channel maps (roughness, metal, AO, height) as BC4, packed maps such as ORM as BC7, and HDR data as BC6H. **Mipmaps** (on by default) writes the full chain of smaller sizes, and **Compression** can switch to smaller BC1 / BC3 files. Bit depth, dither and the EXR option are set by the compression, so they grey out. Sides are rounded up to a multiple of 4, and Repack warns when a size isn't a power of two. DDS is made with Microsoft's free texconv tool, which comes in the download.

**File formats.** Repack reads PNG, JPG, TIFF, TGA, EXR, BMP, HDR and DDS, and writes PNG, TGA, JPG, TIFF, EXR and DDS. Not supported yet: PSD, KTX2 and WebP.

Files and folders are named with templates. The defaults are `{set}_{suffix}` and `{folder}\Repack_{preset}`. Available tokens: `{set}`, `{suffix}`, `{preset}`, `{ext}`, `{res}`, `{folder}` and `{date}`. A live preview shows the result. `{set}` is the name Repack detected for the material. To use another name for one set, type it in the name field above the file rows (clear it to go back to the detected name). Right click an output's Write node in the graph and choose Rename to change its suffix, for example `D` instead of `BaseColor`. To send everything to one place, type a folder in **Output folder**.

## Checks

The Checks panel under the graph points out things that usually cause trouble: mixed sizes, sizes that aren't a power of two, normal maps that aren't unit length or look like the wrong convention, metal maps with too many in-between values, a roughness or occlusion map that is constant or all white, an output with no source, and files whose kind isn't set. A **seam check** tells you, map by map, how visible the edge would be if the texture is tiled (clean, slight or strong), with a **Tile view** button that shows that one map on a plane, tiled 2x2, with displacement off, so you can judge the seam (click it again to put the view back); maps that are unique bakes and not meant to tile can be ignored. Some notes have a fix button, such as **Generate** for a map the preset needs and your files lack.

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
| Next map in 3D, previous map | C, Shift+C |
| Lit material in 3D, and back | M |
| Save blend kit | Ctrl+Shift+S |

Window size, panes and options are remembered. **Help > About Repack** shows the version and build date. Third party components and their licenses are listed in `NOTICES.txt` in the download.

## FAQ

**Does Repack change my original textures?** No. It only writes new files into the output folder.

**The 3D view says it needs OpenGL 3.0.** Use the button in the panel to switch to software OpenGL. Repack restarts and the view works on any computer, a little slower.

**A map shows as unassigned.** Its name doesn't say what it is. Pick its kind in the dropdown on its row.

**Does it need internet?** Only briefly: to activate your key, for a check about once a month, and for the optional update check. Everything else works offline.

**A DDS normal map looks red and green in a viewer.** That is expected: BC5 stores only two channels, and Unreal and Unity rebuild the blue one when they load it.

**Where are my presets?** In `Documents\LP_Tools\Data\Repack`. Removing Repack doesn't touch them.

Questions or a problem? Write to me at support@lptools.store.
