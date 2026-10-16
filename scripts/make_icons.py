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


INK = (10, 10, 10)
PAPER = (245, 245, 242)
THREAD = [(229, 83, 75), (87, 195, 106), (64, 154, 217)]


def mark(size):
    """Ink rounded square, paper LP in even-line capitals (stroke 12, cap height 100), tricolor base."""
    s = size * 4
    im = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    tile = Image.new("RGBA", (s, s), INK + (255,))
    d = ImageDraw.Draw(tile)
    bar = round(s * 0.12)
    for k, c in enumerate(THREAD):
        d.rectangle((s * k // 3, s - bar, s * (k + 1) // 3, s), fill=c)
    u = s * 0.60 / 142          # one design unit in pixels
    ox = (s - 142 * u) / 2
    oy = (s - bar - 100 * u) / 2
    def box(x0, y0, x1, y1):
        return (ox + x0 * u, oy + y0 * u, ox + x1 * u, oy + y1 * u)
    d.rectangle(box(0, 0, 12, 100), fill=PAPER)            # L stem
    d.rectangle(box(0, 88, 56, 100), fill=PAPER)           # L foot
    d.rectangle(box(76, 0, 88, 100), fill=PAPER)           # P stem
    d.rectangle(box(76, 0, 112, 12), fill=PAPER)           # P top bar
    d.rectangle(box(76, 48, 112, 60), fill=PAPER)          # P bottom bar
    ring = Image.new("L", (s, s), 0)                       # P bowl: right half of a ring
    rd = ImageDraw.Draw(ring)
    rd.ellipse(box(82, 0, 142, 60), fill=255)
    rd.ellipse(box(94, 12, 130, 48), fill=0)
    rd.rectangle((0, 0, ox + 112 * u, s), fill=0)
    tile.paste(PAPER + (255,), (0, 0), ring)
    mask = Image.new("L", (s, s), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, s - 1, s - 1), radius=int(s * 0.22), fill=255)
    im.paste(tile, (0, 0), mask)
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
    for k, c in enumerate(THREAD):
        d.rectangle((0, h * k // 3, 14, h * (k + 1) // 3), fill=c)
    im.paste(mark(120), (72, 72), mark(120))
    d.text((220, 100), "T O O L S", font=ImageFont.truetype(str(FONTS / "segoeuil.ttf"), 84), fill=FG)
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
    d.text((72, 560), "lptools.store", font=ImageFont.truetype(BOLD, 34), fill=FG)
    im.save(IMG / "og-image.png", optimize=True)
    return len(icons_found)


if __name__ == "__main__":
    icons()
    print("icons written; og-image with", og(), "tool icons")
