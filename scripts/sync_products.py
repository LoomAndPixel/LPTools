"""Sync Gumroad product data and tool art into the site (dev-only, not published).

Writes _data/gumroad.json and WebP copies of each tool's thumbnail and cover
into assets/img/tools/. Run from anywhere: python scripts/sync_products.py
"""
import json, subprocess, sys
from pathlib import Path
from PIL import Image

SITE = Path(__file__).resolve().parent.parent
MAYA = Path(r"D:\GitHub_Repo\Tools\Maya")
FSPY = Path(r"D:\GitHub_Repo\Tools\fSpy\fspy-maya")

# slug -> folder holding <prefix>_thumbnail.png / <prefix>_cover.png
ART = {
    "modifier-stack": (MAYA / "modifier_stack" / "art", "modifier_stack"),
    "mixamo-auto-control-rig": (MAYA / "Mixamo_Auto_Control_Rig" / "art", "mixamo_auto_control_rig"),
    "keyforge": (MAYA / "keyforge" / "art", "keyforge"),
    "keyforge-lite": (MAYA / "keyforge" / "art", "keyforge_lite"),
    "roll-anything": (MAYA / "roll_anything" / "art", "roll_anything"),
    "glb-bridge": (MAYA / "glb_bridge" / "art", "glb_bridge"),
    "camera-toolkit": (MAYA / "camera_toolkit" / "art", "camera_toolkit"),
    "material-generator": (MAYA / "material_generator" / "art", "material_generator"),
    "fspy-importer-maya": (FSPY, "fspy_maya"),
}
SIZES = {"thumbnail": 600, "cover": 1280}


def sync_data():
    out = subprocess.run("gumroad products list --all --json", shell=True,
                         capture_output=True, text=True, encoding="utf-8", check=True).stdout
    products = [p for p in json.loads(out)["products"] if p.get("published")]
    keep = ("name", "custom_permalink", "short_url", "tags")
    slim = {p["custom_permalink"]: {k: p.get(k) for k in keep} for p in products}
    (SITE / "_data" / "gumroad.json").write_text(json.dumps(slim, indent=1), encoding="utf-8")
    return len(slim)


SKIP = {"icon", "thumbnail", "cover"}


def sync_extras(slug, folder, prefix, sizes):
    """Copy extra shots (<prefix>_ui.png, <prefix>_ui_desc.png, ...) as <slug>-<name>.webp, never upscaled."""
    n = 0
    for src in sorted(folder.glob(f"{prefix}_*.png")):
        name = src.stem[len(prefix) + 1:].replace("_", "-")
        if name in SKIP or src.stem in {f"{prefix}_{k}" for k in SKIP}:
            continue
        im = Image.open(src).convert("RGBA" if "A" in Image.open(src).getbands() else "RGB")
        if im.width > 1280:
            im = im.resize((1280, round(im.height * 1280 / im.width)), Image.LANCZOS)
        out = f"{slug}-{name}.webp"
        im.save(SITE / "assets" / "img" / "tools" / out, "WEBP", quality=90)
        sizes[out] = [im.width, im.height]
        n += 1
    return n


def sync_images():
    n = 0
    sizes = {}
    for slug, (folder, prefix) in ART.items():
        for kind, width in SIZES.items():
            src = folder / f"{prefix}_{kind}.png"
            if not src.exists():
                print(f"missing: {src}")
                continue
            im = Image.open(src).convert("RGB")
            if im.width > width:
                im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
            im.save(SITE / "assets" / "img" / "tools" / f"{slug}-{kind}.webp", "WEBP", quality=82)
            n += 1
        n += sync_extras(slug, folder, prefix, sizes)
    (SITE / "_data" / "images.json").write_text(json.dumps(sizes, indent=1), encoding="utf-8")
    return n


if __name__ == "__main__":
    try:
        print(f"sync_products: {sync_data()} products, {sync_images()} images")
    except Exception as e:
        sys.exit(f"sync_products failed: {e}")
