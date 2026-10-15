"""Builds the site icons and the share image (assets/img/og-image.png).

Run: python scripts/make_icons.py
Writes favicon.ico, apple-touch-icon.png, icon-192.png, icon-512.png and og-image.png.
Tool icons for the share image come from the same art folders as sync_products.py.
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from sync_products import ART, SITE

ACCENT = (59, 91, 219)
BG = (20, 20, 26)
FG = (236, 236, 241)
MUTED = (160, 160, 173)
FONTS = Path("C:/Windows/Fonts")
BOLD = str(FONTS / "segoeuib.ttf")
REG = str(FONTS / "segoeui.ttf")
IMG = SITE / "assets" / "img"


def mark(size):
    """Rounded accent square with a white LP monogram."""
    s = size * 4
    im = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, s - 1, s - 1), radius=int(s * 0.22), fill=ACCENT)
    f = ImageFont.truetype(BOLD, int(s * 0.5))
    l, t, r, b = d.textbbox((0, 0), "LP", font=f)
    d.text(((s - (r - l)) / 2 - l, (s - (b - t)) / 2 - t), "LP", font=f, fill="white")
    return im.resize((size, size), Image.LANCZOS)


def icons():
    mark(512).save(IMG / "icon-512.png")
    mark(192).save(IMG / "icon-192.png")
    mark(180).save(IMG / "apple-touch-icon.png")
    mark(256).save(SITE / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])


def og():
    w, h = 1200, 630
    im = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(im)
    d.rectangle((0, 0, 14, h), fill=ACCENT)
    im.paste(mark(120), (72, 72), mark(120))
    d.text((220, 84), "LP Tools", font=ImageFont.truetype(BOLD, 84), fill=FG)
    d.text((72, 236), "Scripts and plugins for Maya", font=ImageFont.truetype(BOLD, 56), fill=FG)
    d.text((72, 306), "and other 3D, animation and VFX apps", font=ImageFont.truetype(REG, 40), fill=MUTED)
    icons_found = []
    for slug, (folder, prefix) in ART.items():
        p = folder / f"{prefix}_icon.png"
        if p.exists():
            icons_found.append(Image.open(p).convert("RGBA"))
    size, gap = 96, 16
    x0 = 72
    y0 = 430
    for i, ic in enumerate(icons_found[:9]):
        ic = ic.resize((size, size), Image.LANCZOS)
        im.paste(ic, (x0 + i * (size + gap), y0), ic)
    d.text((72, 560), "lptools.store", font=ImageFont.truetype(BOLD, 34), fill=ACCENT)
    im.save(IMG / "og-image.png", optimize=True)
    return len(icons_found)


if __name__ == "__main__":
    icons()
    print("icons written; og-image with", og(), "tool icons")
