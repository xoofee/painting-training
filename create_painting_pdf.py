from dataclasses import dataclass
from math import cos, radians, sin

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


COLOR_OUT = "painting_enlightenment_50_pages.pdf"
INK_OUT = "painting_enlightenment_50_pages_ink_save.pdf"
W, H = A4

INK = colors.HexColor("#2f3437")
PALE = colors.HexColor("#aeb6bd")
BLUE = colors.HexColor("#83b7e8")
YELLOW = colors.HexColor("#ffd76a")
RED = colors.HexColor("#f27a6d")
GREEN = colors.HexColor("#89c779")
ORANGE = colors.HexColor("#f7a652")
PINK = colors.HexColor("#f5a0bd")
PURPLE = colors.HexColor("#9f8fe8")
BROWN = colors.HexColor("#a97b54")
GRAY = colors.HexColor("#d9dde0")


@dataclass(frozen=True)
class RenderMode:
    name: str
    output: str
    title: str
    ink_save: bool = False


COLOR_MODE = RenderMode("color", COLOR_OUT, "Painting Enlightenment - 50 Pages")
INK_MODE = RenderMode(
    "ink_save",
    INK_OUT,
    "Painting Enlightenment - 50 Pages - Ink Save",
    ink_save=True,
)


def setup(c, mode, page):
    c.setFillColor(colors.white)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setStrokeColor(INK if mode.ink_save else GRAY)
    c.setLineWidth(1.1)
    c.setDash([3, 7] if mode.ink_save else [])
    c.roundRect(30, 34, W - 60, H - 68, 14, fill=0, stroke=1)
    c.setDash([])
    c.setFillColor(colors.HexColor("#8c949b"))
    c.setFont("Helvetica", 8)
    c.drawCentredString(W / 2, 18, str(page))


def line_style(c, mode, guide=False, color=INK, width=4.5):
    if mode.ink_save:
        c.setStrokeColor(PALE if guide else INK)
        c.setDash([3, 7])
    else:
        c.setStrokeColor(PALE if guide else color)
        c.setDash([3, 8] if guide else [])
    c.setLineWidth(width)
    c.setLineCap(1)
    c.setLineJoin(1)


def finish_shape(c):
    c.setDash([])


def fill_color(mode, guide, color):
    if mode.ink_save or guide:
        return None
    return color


def draw_path(c, mode, path, fill, stroke=1):
    c.drawPath(path, fill=1 if fill is not None else 0, stroke=stroke)


def rect(c, mode, x, y, w, h, fill=None, radius=0):
    if fill is not None:
        c.setFillColor(fill)
    if radius:
        c.roundRect(x, y, w, h, radius, fill=1 if fill is not None else 0, stroke=1)
    else:
        c.rect(x, y, w, h, fill=1 if fill is not None else 0, stroke=1)


def ellipse(c, mode, x1, y1, x2, y2, fill=None):
    if fill is not None:
        c.setFillColor(fill)
    c.ellipse(x1, y1, x2, y2, fill=1 if fill is not None else 0, stroke=1)


def circle(c, mode, x, y, r, fill=None):
    if fill is not None:
        c.setFillColor(fill)
    c.circle(x, y, r, fill=1 if fill is not None else 0, stroke=1)


def swatches(c, cols, x=402, y=744):
    for i, col in enumerate(cols):
        c.setFillColor(col)
        c.setStrokeColor(INK)
        c.setLineWidth(1.4)
        c.setDash([])
        c.circle(x + i * 28, y, 9, fill=1, stroke=1)


def star_points(x, y, r):
    pts = []
    for i in range(10):
        rr = r if i % 2 == 0 else r * 0.45
        a = radians(-90 + i * 36)
        pts.append((x + cos(a) * rr, y + sin(a) * rr))
    return pts


def polygon(c, mode, pts, fill=None):
    p = c.beginPath()
    p.moveTo(*pts[0])
    for pt in pts[1:]:
        p.lineTo(*pt)
    p.close()
    if fill is not None:
        c.setFillColor(fill)
    draw_path(c, mode, p, fill)


def warmup_lines(c, mode, x, y, s=1, guide=False, variant=0):
    line_style(c, mode, guide, INK, 4)
    for i in range(4):
        yy = y + (i - 1.5) * 35 * s
        if variant % 4 == 0:
            c.line(x - 54 * s, yy, x + 54 * s, yy)
        elif variant % 4 == 1:
            c.line(x + (i - 1.5) * 30 * s, y - 58 * s, x + (i - 1.5) * 30 * s, y + 58 * s)
        elif variant % 4 == 2:
            c.arc(x - 55 * s, yy - 18 * s, x + 55 * s, yy + 18 * s, 0, 180)
        else:
            p = c.beginPath()
            p.moveTo(x - 58 * s, yy)
            p.curveTo(x - 26 * s, yy + 24 * s, x + 20 * s, yy - 24 * s, x + 58 * s, yy)
            draw_path(c, mode, p, None)
    finish_shape(c)


def line_rows(c, mode, x, y, s=1, guide=False):
    warmup_lines(c, mode, x, y, s, guide, 0)


def line_columns(c, mode, x, y, s=1, guide=False):
    warmup_lines(c, mode, x, y, s, guide, 1)


def arc_rows(c, mode, x, y, s=1, guide=False):
    warmup_lines(c, mode, x, y, s, guide, 2)


def wave_rows(c, mode, x, y, s=1, guide=False):
    warmup_lines(c, mode, x, y, s, guide, 3)


def flower(c, mode, x, y, s=1, guide=False):
    line_style(c, mode, guide, INK, 4)
    fill = fill_color(mode, guide, GREEN)
    c.line(x, y - 86 * s, x, y - 15 * s)
    ellipse(c, mode, x - 45 * s, y - 62 * s, x - 5 * s, y - 30 * s, fill)
    ellipse(c, mode, x + 6 * s, y - 70 * s, x + 50 * s, y - 38 * s, fill)
    fill = fill_color(mode, guide, PINK)
    for a in range(0, 360, 60):
        px = x + cos(radians(a)) * 27 * s
        py = y + sin(radians(a)) * 27 * s
        ellipse(c, mode, px - 20 * s, py - 14 * s, px + 20 * s, py + 14 * s, fill)
    circle(c, mode, x, y, 15 * s, fill_color(mode, guide, YELLOW))
    finish_shape(c)


def rocket(c, mode, x, y, s=1, guide=False):
    line_style(c, mode, guide, INK, 4.5)
    p = c.beginPath()
    p.moveTo(x, y + 85 * s)
    p.curveTo(x - 36 * s, y + 42 * s, x - 33 * s, y - 40 * s, x, y - 68 * s)
    p.curveTo(x + 33 * s, y - 40 * s, x + 36 * s, y + 42 * s, x, y + 85 * s)
    p.close()
    draw_path(c, mode, p, fill_color(mode, guide, BLUE))
    circle(c, mode, x, y + 20 * s, 15 * s, None)
    polygon(c, mode, [(x - 25 * s, y - 35 * s), (x - 56 * s, y - 74 * s), (x - 22 * s, y - 64 * s)], fill_color(mode, guide, RED))
    polygon(c, mode, [(x + 25 * s, y - 35 * s), (x + 56 * s, y - 74 * s), (x + 22 * s, y - 64 * s)], fill_color(mode, guide, RED))
    polygon(c, mode, [(x - 17 * s, y - 67 * s), (x, y - 108 * s), (x + 17 * s, y - 67 * s)], fill_color(mode, guide, ORANGE))
    finish_shape(c)


def sun_cloud(c, mode, x, y, s=1, guide=False):
    line_style(c, mode, guide, INK, 4)
    for a in range(0, 360, 30):
        c.line(x + cos(radians(a)) * 42 * s, y + sin(radians(a)) * 42 * s,
               x + cos(radians(a)) * 64 * s, y + sin(radians(a)) * 64 * s)
    circle(c, mode, x, y, 33 * s, fill_color(mode, guide, YELLOW))
    circle(c, mode, x + 70 * s, y - 26 * s, 22 * s, None)
    circle(c, mode, x + 100 * s, y - 18 * s, 29 * s, None)
    circle(c, mode, x + 134 * s, y - 27 * s, 20 * s, None)
    c.line(x + 52 * s, y - 46 * s, x + 154 * s, y - 46 * s)
    finish_shape(c)


def fish(c, mode, x, y, s=1, guide=False):
    line_style(c, mode, guide, INK, 4)
    ellipse(c, mode, x - 68 * s, y - 36 * s, x + 68 * s, y + 36 * s, fill_color(mode, guide, ORANGE))
    polygon(c, mode, [(x - 68 * s, y), (x - 118 * s, y + 42 * s), (x - 118 * s, y - 42 * s)], fill_color(mode, guide, PINK))
    circle(c, mode, x + 35 * s, y + 11 * s, 8 * s, None)
    c.arc(x + 38 * s, y - 22 * s, x + 62 * s, y + 2 * s, 200, 95)
    finish_shape(c)


def house(c, mode, x, y, s=1, guide=False):
    line_style(c, mode, guide, INK, 4)
    rect(c, mode, x - 68 * s, y - 70 * s, 136 * s, 104 * s, fill_color(mode, guide, colors.HexColor("#f4d58d")))
    polygon(c, mode, [(x - 86 * s, y + 34 * s), (x, y + 102 * s), (x + 86 * s, y + 34 * s)], fill_color(mode, guide, RED))
    rect(c, mode, x - 48 * s, y - 24 * s, 34 * s, 34 * s, fill_color(mode, guide, BLUE))
    rect(c, mode, x + 20 * s, y - 24 * s, 34 * s, 34 * s, fill_color(mode, guide, BLUE))
    rect(c, mode, x - 17 * s, y - 70 * s, 34 * s, 54 * s, fill_color(mode, guide, BROWN))
    finish_shape(c)


def tree(c, mode, x, y, s=1, guide=False):
    line_style(c, mode, guide, INK, 4)
    rect(c, mode, x - 18 * s, y - 86 * s, 36 * s, 82 * s, fill_color(mode, guide, BROWN), 12 * s)
    circle(c, mode, x - 35 * s, y + 18 * s, 40 * s, fill_color(mode, guide, GREEN))
    circle(c, mode, x + 34 * s, y + 20 * s, 43 * s, fill_color(mode, guide, GREEN))
    circle(c, mode, x, y + 62 * s, 48 * s, fill_color(mode, guide, GREEN))
    finish_shape(c)


def car(c, mode, x, y, s=1, guide=False):
    line_style(c, mode, guide, INK, 4)
    rect(c, mode, x - 100 * s, y - 34 * s, 200 * s, 60 * s, fill_color(mode, guide, RED), 24 * s)
    polygon(c, mode, [(x - 48 * s, y + 26 * s), (x - 18 * s, y + 68 * s), (x + 48 * s, y + 68 * s), (x + 78 * s, y + 26 * s)], fill_color(mode, guide, RED))
    c.line(x + 12 * s, y + 64 * s, x + 12 * s, y + 30 * s)
    circle(c, mode, x - 58 * s, y - 34 * s, 19 * s, None)
    circle(c, mode, x + 58 * s, y - 34 * s, 19 * s, None)
    finish_shape(c)


def animal(c, mode, x, y, s=1, guide=False):
    line_style(c, mode, guide, INK, 4)
    circle(c, mode, x, y, 62 * s, fill_color(mode, guide, colors.HexColor("#f5c38a")))
    polygon(c, mode, [(x - 46 * s, y + 40 * s), (x - 68 * s, y + 100 * s), (x - 14 * s, y + 64 * s)], None)
    polygon(c, mode, [(x + 46 * s, y + 40 * s), (x + 68 * s, y + 100 * s), (x + 14 * s, y + 64 * s)], None)
    circle(c, mode, x - 24 * s, y + 15 * s, 8 * s, None)
    circle(c, mode, x + 24 * s, y + 15 * s, 8 * s, None)
    circle(c, mode, x, y - 11 * s, 8 * s, fill_color(mode, guide, PINK))
    c.arc(x - 26 * s, y - 39 * s, x, y - 10 * s, 205, 120)
    c.arc(x, y - 39 * s, x + 26 * s, y - 10 * s, 215, 120)
    finish_shape(c)


def rainbow(c, mode, x, y, s=1, guide=False):
    arcs = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]
    for i, clr in enumerate(arcs):
        line_style(c, mode, guide, clr, 9 if not mode.ink_save and not guide else 4)
        r = (108 - i * 14) * s
        c.arc(x - r, y - r, x + r, y + r, 0, 180)
    finish_shape(c)


def balloon(c, mode, x, y, s=1, guide=False):
    line_style(c, mode, guide, INK, 4)
    circle(c, mode, x, y + 30 * s, 42 * s, fill_color(mode, guide, PURPLE))
    polygon(c, mode, [(x - 10 * s, y - 9 * s), (x + 10 * s, y - 9 * s), (x, y - 25 * s)], None)
    p = c.beginPath()
    p.moveTo(x, y - 25 * s)
    p.curveTo(x - 20 * s, y - 65 * s, x + 20 * s, y - 90 * s, x, y - 125 * s)
    draw_path(c, mode, p, None)
    finish_shape(c)


def boat(c, mode, x, y, s=1, guide=False):
    line_style(c, mode, guide, INK, 4)
    polygon(c, mode, [(x - 90 * s, y - 18 * s), (x + 90 * s, y - 18 * s), (x + 55 * s, y - 58 * s), (x - 55 * s, y - 58 * s)], fill_color(mode, guide, BROWN))
    c.line(x, y - 18 * s, x, y + 90 * s)
    polygon(c, mode, [(x, y + 82 * s), (x, y - 8 * s), (x + 62 * s, y - 8 * s)], fill_color(mode, guide, BLUE))
    polygon(c, mode, [(x - 4 * s, y + 72 * s), (x - 4 * s, y - 8 * s), (x - 58 * s, y - 8 * s)], fill_color(mode, guide, YELLOW))
    finish_shape(c)


def butterfly(c, mode, x, y, s=1, guide=False):
    line_style(c, mode, guide, INK, 4)
    ellipse(c, mode, x - 76 * s, y + 4 * s, x - 8 * s, y + 70 * s, fill_color(mode, guide, PINK))
    ellipse(c, mode, x + 8 * s, y + 4 * s, x + 76 * s, y + 70 * s, fill_color(mode, guide, PINK))
    ellipse(c, mode, x - 70 * s, y - 58 * s, x - 8 * s, y + 8 * s, fill_color(mode, guide, PURPLE))
    ellipse(c, mode, x + 8 * s, y - 58 * s, x + 70 * s, y + 8 * s, fill_color(mode, guide, PURPLE))
    ellipse(c, mode, x - 9 * s, y - 52 * s, x + 9 * s, y + 62 * s, fill_color(mode, guide, BROWN))
    c.arc(x - 28 * s, y + 52 * s, x, y + 92 * s, 15, 125)
    c.arc(x, y + 52 * s, x + 28 * s, y + 92 * s, 40, 125)
    finish_shape(c)


def simple_star(c, mode, x, y, s=1, guide=False):
    line_style(c, mode, guide, INK, 4)
    polygon(c, mode, star_points(x, y, 52 * s), fill_color(mode, guide, YELLOW))
    finish_shape(c)


def mushroom(c, mode, x, y, s=1, guide=False):
    line_style(c, mode, guide, INK, 4)
    p = c.beginPath()
    p.moveTo(x - 72 * s, y)
    p.curveTo(x - 55 * s, y + 70 * s, x + 55 * s, y + 70 * s, x + 72 * s, y)
    p.close()
    draw_path(c, mode, p, fill_color(mode, guide, RED))
    rect(c, mode, x - 28 * s, y - 72 * s, 56 * s, 72 * s, fill_color(mode, guide, colors.HexColor("#f4d58d")), 18 * s)
    for dx in [-35, 0, 35]:
        circle(c, mode, x + dx * s, y + 25 * s, 9 * s, None)
    finish_shape(c)


def fruit(c, mode, x, y, s=1, guide=False):
    line_style(c, mode, guide, INK, 4)
    circle(c, mode, x - 16 * s, y, 38 * s, fill_color(mode, guide, RED))
    circle(c, mode, x + 16 * s, y, 38 * s, fill_color(mode, guide, RED))
    c.line(x, y + 38 * s, x + 18 * s, y + 72 * s)
    ellipse(c, mode, x + 18 * s, y + 50 * s, x + 58 * s, y + 76 * s, fill_color(mode, guide, GREEN))
    finish_shape(c)


def umbrella(c, mode, x, y, s=1, guide=False):
    line_style(c, mode, guide, INK, 4)
    p = c.beginPath()
    p.moveTo(x - 92 * s, y + 10 * s)
    p.curveTo(x - 55 * s, y + 82 * s, x + 55 * s, y + 82 * s, x + 92 * s, y + 10 * s)
    p.curveTo(x + 55 * s, y + 28 * s, x + 30 * s, y - 10 * s, x, y + 10 * s)
    p.curveTo(x - 30 * s, y - 10 * s, x - 55 * s, y + 28 * s, x - 92 * s, y + 10 * s)
    p.close()
    draw_path(c, mode, p, fill_color(mode, guide, BLUE))
    c.line(x, y + 10 * s, x, y - 84 * s)
    c.arc(x - 2 * s, y - 110 * s, x + 42 * s, y - 66 * s, 180, 180)
    finish_shape(c)


def bird(c, mode, x, y, s=1, guide=False):
    line_style(c, mode, guide, INK, 4)
    ellipse(c, mode, x - 58 * s, y - 32 * s, x + 50 * s, y + 38 * s, fill_color(mode, guide, BLUE))
    circle(c, mode, x + 48 * s, y + 20 * s, 28 * s, fill_color(mode, guide, BLUE))
    polygon(c, mode, [(x + 75 * s, y + 22 * s), (x + 112 * s, y + 35 * s), (x + 78 * s, y + 5 * s)], fill_color(mode, guide, ORANGE))
    polygon(c, mode, [(x - 48 * s, y), (x - 100 * s, y + 34 * s), (x - 92 * s, y - 28 * s)], fill_color(mode, guide, PURPLE))
    circle(c, mode, x + 58 * s, y + 28 * s, 5 * s, None)
    finish_shape(c)


def cupcake(c, mode, x, y, s=1, guide=False):
    line_style(c, mode, guide, INK, 4)
    polygon(c, mode, [(x - 55 * s, y - 25 * s), (x + 55 * s, y - 25 * s), (x + 38 * s, y - 95 * s), (x - 38 * s, y - 95 * s)], fill_color(mode, guide, YELLOW))
    for dx in [-36, 0, 36]:
        circle(c, mode, x + dx * s, y + 15 * s, 30 * s, fill_color(mode, guide, PINK))
    circle(c, mode, x, y + 50 * s, 26 * s, fill_color(mode, guide, PINK))
    circle(c, mode, x, y + 85 * s, 7 * s, fill_color(mode, guide, RED))
    finish_shape(c)


def leaf(c, mode, x, y, s=1, guide=False):
    line_style(c, mode, guide, INK, 4)
    p = c.beginPath()
    p.moveTo(x - 80 * s, y - 10 * s)
    p.curveTo(x - 20 * s, y + 72 * s, x + 72 * s, y + 42 * s, x + 88 * s, y - 42 * s)
    p.curveTo(x + 20 * s, y - 28 * s, x - 35 * s, y - 55 * s, x - 80 * s, y - 10 * s)
    p.close()
    draw_path(c, mode, p, fill_color(mode, guide, GREEN))
    c.line(x - 70 * s, y - 10 * s, x + 72 * s, y - 35 * s)
    finish_shape(c)


def kite(c, mode, x, y, s=1, guide=False):
    line_style(c, mode, guide, INK, 4)
    polygon(c, mode, [(x, y + 82 * s), (x + 56 * s, y + 18 * s), (x, y - 84 * s), (x - 56 * s, y + 18 * s)], fill_color(mode, guide, ORANGE))
    c.line(x, y + 82 * s, x, y - 84 * s)
    c.line(x - 56 * s, y + 18 * s, x + 56 * s, y + 18 * s)
    p = c.beginPath()
    p.moveTo(x, y - 84 * s)
    p.curveTo(x - 22 * s, y - 124 * s, x + 32 * s, y - 144 * s, x + 4 * s, y - 184 * s)
    draw_path(c, mode, p, None)
    finish_shape(c)


def bus(c, mode, x, y, s=1, guide=False):
    line_style(c, mode, guide, INK, 4)
    rect(c, mode, x - 110 * s, y - 42 * s, 220 * s, 86 * s, fill_color(mode, guide, YELLOW), 14 * s)
    for dx in [-64, -18, 28, 74]:
        rect(c, mode, x + dx * s, y + 2 * s, 34 * s, 25 * s, None)
    circle(c, mode, x - 68 * s, y - 42 * s, 17 * s, None)
    circle(c, mode, x + 68 * s, y - 42 * s, 17 * s, None)
    finish_shape(c)


def train(c, mode, x, y, s=1, guide=False):
    line_style(c, mode, guide, INK, 4)
    rect(c, mode, x - 108 * s, y - 45 * s, 92 * s, 64 * s, fill_color(mode, guide, BLUE), 8 * s)
    rect(c, mode, x - 10 * s, y - 45 * s, 110 * s, 78 * s, fill_color(mode, guide, RED), 8 * s)
    rect(c, mode, x + 16 * s, y + 33 * s, 48 * s, 36 * s, fill_color(mode, guide, RED), 8 * s)
    for dx in [-72, -20, 36, 80]:
        circle(c, mode, x + dx * s, y - 48 * s, 15 * s, None)
    finish_shape(c)


def castle(c, mode, x, y, s=1, guide=False):
    line_style(c, mode, guide, INK, 4)
    rect(c, mode, x - 84 * s, y - 70 * s, 168 * s, 110 * s, fill_color(mode, guide, colors.HexColor("#d6c3f5")))
    for dx in [-64, 0, 64]:
        rect(c, mode, x + dx * s - 18 * s, y + 40 * s, 36 * s, 42 * s, fill_color(mode, guide, colors.HexColor("#d6c3f5")))
        polygon(c, mode, [(x + dx * s - 25 * s, y + 82 * s), (x + dx * s, y + 118 * s), (x + dx * s + 25 * s, y + 82 * s)], fill_color(mode, guide, PURPLE))
    rect(c, mode, x - 18 * s, y - 70 * s, 36 * s, 50 * s, None, 14 * s)
    finish_shape(c)


def snowman(c, mode, x, y, s=1, guide=False):
    line_style(c, mode, guide, INK, 4)
    circle(c, mode, x, y - 50 * s, 45 * s, None)
    circle(c, mode, x, y + 20 * s, 34 * s, None)
    circle(c, mode, x - 12 * s, y + 28 * s, 4 * s, None)
    circle(c, mode, x + 12 * s, y + 28 * s, 4 * s, None)
    polygon(c, mode, [(x, y + 15 * s), (x + 34 * s, y + 8 * s), (x, y)], fill_color(mode, guide, ORANGE))
    rect(c, mode, x - 38 * s, y + 54 * s, 76 * s, 10 * s, None)
    rect(c, mode, x - 24 * s, y + 64 * s, 48 * s, 36 * s, None)
    finish_shape(c)


def icecream(c, mode, x, y, s=1, guide=False):
    line_style(c, mode, guide, INK, 4)
    polygon(c, mode, [(x - 42 * s, y - 12 * s), (x + 42 * s, y - 12 * s), (x, y - 112 * s)], fill_color(mode, guide, colors.HexColor("#d59b5f")))
    circle(c, mode, x, y + 34 * s, 42 * s, fill_color(mode, guide, PINK))
    circle(c, mode, x - 33 * s, y + 4 * s, 30 * s, fill_color(mode, guide, YELLOW))
    circle(c, mode, x + 33 * s, y + 4 * s, 30 * s, fill_color(mode, guide, BLUE))
    finish_shape(c)


def snail(c, mode, x, y, s=1, guide=False):
    line_style(c, mode, guide, INK, 4)
    ellipse(c, mode, x - 82 * s, y - 44 * s, x + 44 * s, y + 32 * s, fill_color(mode, guide, GREEN))
    circle(c, mode, x - 18 * s, y + 18 * s, 42 * s, fill_color(mode, guide, ORANGE))
    c.arc(x - 42 * s, y - 5 * s, x + 12 * s, y + 48 * s, 0, 300)
    circle(c, mode, x + 62 * s, y + 10 * s, 26 * s, fill_color(mode, guide, GREEN))
    c.line(x + 48 * s, y + 32 * s, x + 32 * s, y + 66 * s)
    c.line(x + 70 * s, y + 32 * s, x + 86 * s, y + 66 * s)
    finish_shape(c)


def turtle(c, mode, x, y, s=1, guide=False):
    line_style(c, mode, guide, INK, 4)
    ellipse(c, mode, x - 78 * s, y - 42 * s, x + 78 * s, y + 42 * s, fill_color(mode, guide, GREEN))
    circle(c, mode, x + 96 * s, y + 4 * s, 24 * s, fill_color(mode, guide, GREEN))
    for dx, dy in [(-50, -46), (32, -46), (-50, 46), (32, 46)]:
        ellipse(c, mode, x + dx * s - 14 * s, y + dy * s - 10 * s, x + dx * s + 18 * s, y + dy * s + 10 * s, None)
    c.line(x - 44 * s, y, x + 44 * s, y)
    c.line(x, y - 35 * s, x, y + 35 * s)
    finish_shape(c)


def draw_item(c, mode, item):
    func, x, y, s, guide = item
    func(c, mode, x, y, s, guide)


def dense_page(c, mode, page, items, swatch_cols=None):
    setup(c, mode, page)
    if swatch_cols and not mode.ink_save:
        swatches(c, swatch_cols)
    for item in items:
        draw_item(c, mode, item)


def item(func, x, y, s=1, guide=False):
    return (func, x, y, s, guide)


PAGE_DEFS = [
    ("Lines", [item(line_rows, 150, 665, 1, False), item(line_rows, 420, 665, 1, True), item(line_rows, 150, 430, 1, True), item(line_rows, 420, 430, 1, False), item(line_rows, 285, 210, 1.1, True)], [RED, YELLOW, GREEN, BLUE]),
    ("Verticals", [item(line_columns, 150, 650, 1, True), item(line_columns, 420, 650, 1, False), item(line_columns, 150, 400, 1, False), item(line_columns, 420, 400, 1, True), item(simple_star, 285, 190, .85, True)], [YELLOW, BLUE]),
    ("Curves", [item(arc_rows, 150, 645, 1, False), item(arc_rows, 420, 645, 1, True), item(rainbow, 180, 390, .8, False), item(rainbow, 420, 380, .72, True), item(balloon, 285, 185, .75, True)], [RED, ORANGE, YELLOW, GREEN, BLUE]),
    ("Waves", [item(wave_rows, 150, 650, 1, True), item(wave_rows, 420, 650, 1, False), item(fish, 165, 405, .72, True), item(fish, 425, 405, .72, False), item(boat, 285, 190, .72, True)], [ORANGE, PINK, BLUE]),
    ("Circles", [item(balloon, 150, 655, .78, False), item(balloon, 420, 655, .78, True), item(flower, 160, 395, .78, True), item(flower, 420, 395, .78, False), item(snowman, 285, 195, .72, True)], [PINK, YELLOW, GREEN, PURPLE]),
    ("Rocket Fleet", [item(rocket, 140, 650, .8, False), item(rocket, 300, 650, .72, True), item(rocket, 455, 650, .8, False), item(simple_star, 140, 350, .75, True), item(simple_star, 300, 350, .75, False), item(simple_star, 455, 350, .75, True)], [BLUE, RED, ORANGE, YELLOW]),
    ("Rocket Launch", [item(rocket, 165, 630, .95, False), item(rocket, 430, 630, .82, True), item(warmup_lines, 160, 280, .9, True), item(warmup_lines, 430, 280, .9, False)], [BLUE, ORANGE, RED]),
    ("Rocket Stars", [item(rocket, 155, 650, .75, True), item(simple_star, 410, 700, .75, False), item(simple_star, 275, 500, .62, True), item(rocket, 420, 360, .78, False), item(simple_star, 150, 230, .62, True)], [YELLOW, BLUE, RED]),
    ("Flower Pair", [item(flower, 145, 650, .86, False), item(flower, 305, 650, .78, True), item(flower, 465, 650, .86, False), item(leaf, 180, 315, .72, True), item(leaf, 405, 290, .72, False)], [PINK, YELLOW, GREEN]),
    ("Flower Garden", [item(flower, 135, 645, .75, True), item(flower, 285, 660, .86, False), item(flower, 450, 645, .75, True), item(flower, 190, 330, .72, False), item(flower, 395, 330, .72, True)], [PINK, GREEN, YELLOW, BLUE]),
    ("Leaves", [item(leaf, 160, 655, .85, False), item(leaf, 425, 650, .85, True), item(leaf, 160, 390, .78, True), item(leaf, 425, 390, .78, False), item(fruit, 285, 175, .72, True)], [GREEN, RED]),
    ("Sun Cloud", [item(sun_cloud, 120, 665, .75, False), item(sun_cloud, 350, 665, .68, True), item(sun_cloud, 115, 390, .68, True), item(sun_cloud, 355, 390, .75, False), item(rainbow, 285, 185, .68, True)], [YELLOW, BLUE, PURPLE]),
    ("Weather", [item(umbrella, 155, 625, .78, False), item(sun_cloud, 350, 650, .66, True), item(rainbow, 175, 385, .72, False), item(umbrella, 425, 305, .66, True)], [BLUE, YELLOW, RED, PURPLE]),
    ("Rainbows", [item(rainbow, 165, 650, .75, False), item(rainbow, 425, 650, .75, True), item(rainbow, 165, 390, .68, True), item(rainbow, 425, 390, .68, False), item(simple_star, 285, 175, .72, True)], [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]),
    ("Fish Swim", [item(fish, 145, 660, .72, False), item(fish, 420, 650, .72, True), item(fish, 165, 405, .68, True), item(fish, 420, 405, .68, False), item(warmup_lines, 285, 190, .9, True)], [ORANGE, PINK, BLUE]),
    ("Fish Bubbles", [item(fish, 170, 645, .78, False), item(fish, 420, 500, .65, True), item(balloon, 140, 255, .55, True), item(balloon, 300, 260, .55, False), item(balloon, 455, 255, .55, True)], [ORANGE, BLUE, PURPLE]),
    ("Boats", [item(boat, 155, 650, .72, False), item(boat, 425, 650, .72, True), item(boat, 155, 390, .66, True), item(boat, 425, 390, .66, False), item(warmup_lines, 285, 180, .9, True)], [BROWN, BLUE, YELLOW]),
    ("House Row", [item(house, 145, 640, .72, False), item(house, 300, 640, .66, True), item(house, 455, 640, .72, False), item(tree, 180, 315, .62, True), item(tree, 405, 315, .62, False)], [RED, YELLOW, BLUE, BROWN]),
    ("Houses", [item(house, 160, 625, .82, False), item(house, 430, 625, .72, True), item(house, 160, 320, .72, True), item(house, 430, 320, .82, False)], [RED, YELLOW, BLUE, GREEN]),
    ("Castle Shapes", [item(castle, 160, 635, .68, False), item(castle, 425, 635, .68, True), item(house, 160, 305, .72, True), item(castle, 425, 305, .62, False)], [PURPLE, RED, YELLOW]),
    ("Trees", [item(tree, 150, 640, .75, False), item(tree, 305, 640, .68, True), item(tree, 460, 640, .75, False), item(leaf, 170, 315, .7, True), item(leaf, 420, 315, .7, False)], [GREEN, BROWN, YELLOW]),
    ("Fruit Tree", [item(tree, 155, 625, .78, False), item(fruit, 420, 650, .72, True), item(fruit, 160, 320, .68, False), item(tree, 420, 315, .68, True)], [GREEN, BROWN, RED]),
    ("Mushrooms", [item(mushroom, 150, 645, .72, False), item(mushroom, 305, 645, .66, True), item(mushroom, 460, 645, .72, False), item(leaf, 180, 310, .68, True), item(leaf, 405, 310, .68, False)], [RED, GREEN, YELLOW]),
    ("Cars", [item(car, 165, 650, .72, False), item(car, 425, 650, .68, True), item(car, 165, 390, .68, True), item(car, 425, 390, .72, False), item(warmup_lines, 285, 185, .9, True)], [RED, BLUE, YELLOW]),
    ("Bus Ride", [item(bus, 165, 650, .7, False), item(bus, 425, 650, .64, True), item(car, 165, 385, .65, True), item(bus, 425, 385, .64, False)], [YELLOW, RED, BLUE]),
    ("Train", [item(train, 165, 645, .7, False), item(train, 425, 645, .64, True), item(train, 165, 385, .64, True), item(train, 425, 385, .7, False)], [BLUE, RED, YELLOW]),
    ("Animal Faces", [item(animal, 145, 650, .72, False), item(animal, 300, 650, .66, True), item(animal, 455, 650, .72, False), item(animal, 190, 325, .66, True), item(animal, 400, 325, .66, False)], [ORANGE, PINK, BROWN]),
    ("Birds", [item(bird, 155, 650, .68, False), item(bird, 425, 640, .62, True), item(bird, 155, 375, .62, True), item(bird, 425, 375, .68, False), item(warmup_lines, 285, 175, .82, True)], [BLUE, ORANGE, PURPLE]),
    ("Butterflies", [item(butterfly, 150, 650, .65, False), item(butterfly, 425, 650, .6, True), item(butterfly, 150, 380, .6, True), item(butterfly, 425, 380, .65, False)], [PINK, PURPLE, BROWN]),
    ("Snails", [item(snail, 165, 650, .68, False), item(snail, 425, 650, .62, True), item(snail, 165, 380, .62, True), item(snail, 425, 380, .68, False)], [GREEN, ORANGE, YELLOW]),
    ("Turtles", [item(turtle, 165, 650, .68, False), item(turtle, 425, 650, .62, True), item(turtle, 165, 385, .62, True), item(turtle, 425, 385, .68, False)], [GREEN, BLUE]),
    ("Balloons", [item(balloon, 130, 650, .7, False), item(balloon, 285, 650, .64, True), item(balloon, 440, 650, .7, False), item(balloon, 190, 330, .62, True), item(balloon, 400, 330, .62, False)], [PURPLE, RED, YELLOW, BLUE]),
    ("Kites", [item(kite, 150, 645, .62, False), item(kite, 425, 645, .58, True), item(kite, 150, 350, .55, True), item(kite, 425, 350, .62, False)], [ORANGE, BLUE, RED]),
    ("Stars", [item(simple_star, 130, 665, .65, False), item(simple_star, 285, 665, .58, True), item(simple_star, 440, 665, .65, False), item(simple_star, 190, 380, .58, True), item(simple_star, 395, 380, .58, False), item(rainbow, 285, 175, .62, True)], [YELLOW, PURPLE, BLUE]),
    ("Cupcakes", [item(cupcake, 155, 640, .68, False), item(cupcake, 425, 640, .62, True), item(cupcake, 155, 360, .62, True), item(cupcake, 425, 360, .68, False)], [PINK, YELLOW, RED, BLUE]),
    ("Fruit", [item(fruit, 145, 645, .72, False), item(fruit, 300, 645, .64, True), item(fruit, 455, 645, .72, False), item(fruit, 190, 335, .64, True), item(fruit, 400, 335, .64, False)], [RED, GREEN, YELLOW]),
    ("Umbrellas", [item(umbrella, 155, 640, .66, False), item(umbrella, 425, 640, .6, True), item(umbrella, 155, 360, .6, True), item(umbrella, 425, 360, .66, False)], [BLUE, PURPLE, YELLOW]),
    ("Snowmen", [item(snowman, 150, 645, .68, False), item(snowman, 305, 645, .62, True), item(snowman, 460, 645, .68, False), item(simple_star, 190, 315, .56, True), item(simple_star, 400, 315, .56, False)], [ORANGE, BLUE, YELLOW]),
    ("Ice Cream", [item(icecream, 155, 640, .7, False), item(icecream, 425, 640, .64, True), item(cupcake, 155, 360, .58, True), item(icecream, 425, 360, .64, False)], [PINK, YELLOW, BLUE]),
    ("Shape Homes", [item(house, 150, 650, .66, True), item(castle, 425, 650, .62, False), item(bus, 160, 360, .62, False), item(train, 425, 360, .58, True)], [RED, YELLOW, BLUE, PURPLE]),
    ("Garden Mix", [item(flower, 135, 650, .64, False), item(mushroom, 300, 650, .58, True), item(tree, 455, 640, .62, False), item(leaf, 170, 330, .62, True), item(fruit, 405, 330, .62, False)], [GREEN, PINK, RED, YELLOW]),
    ("Sky Mix", [item(sun_cloud, 105, 660, .58, False), item(balloon, 395, 650, .62, True), item(kite, 160, 360, .52, False), item(rainbow, 420, 350, .62, True), item(simple_star, 285, 180, .55, False)], [YELLOW, BLUE, PURPLE, ORANGE]),
    ("Water Mix", [item(fish, 145, 650, .62, False), item(boat, 425, 650, .6, True), item(turtle, 160, 385, .6, True), item(snail, 425, 385, .6, False)], [BLUE, GREEN, ORANGE, BROWN]),
    ("Wheels", [item(car, 160, 655, .62, False), item(bus, 425, 655, .58, True), item(train, 160, 390, .58, False), item(car, 425, 390, .58, True), item(warmup_lines, 285, 180, .8, True)], [RED, YELLOW, BLUE]),
    ("Faces Friends", [item(animal, 150, 650, .65, False), item(bird, 430, 650, .58, True), item(butterfly, 150, 370, .58, False), item(snail, 425, 370, .58, True)], [ORANGE, BLUE, PINK, GREEN]),
    ("Picnic", [item(cupcake, 150, 650, .6, False), item(fruit, 300, 650, .6, True), item(icecream, 455, 650, .6, False), item(balloon, 190, 335, .56, True), item(simple_star, 400, 335, .56, False)], [PINK, RED, YELLOW, PURPLE]),
    ("Little Town", [item(house, 130, 650, .58, False), item(tree, 285, 650, .56, True), item(castle, 450, 650, .54, False), item(car, 165, 350, .56, True), item(bus, 425, 350, .56, False)], [RED, GREEN, YELLOW, PURPLE]),
    ("Nature Friends", [item(tree, 140, 650, .58, False), item(bird, 420, 650, .56, True), item(flower, 150, 360, .58, True), item(butterfly, 425, 360, .56, False), item(leaf, 285, 180, .58, True)], [GREEN, BLUE, PINK, YELLOW]),
    ("Adventure", [item(rocket, 145, 650, .58, False), item(boat, 420, 650, .56, True), item(train, 165, 365, .56, False), item(kite, 425, 350, .5, True), item(simple_star, 285, 185, .52, False)], [BLUE, RED, ORANGE, YELLOW]),
    ("Celebration", [item(balloon, 125, 650, .58, False), item(simple_star, 285, 690, .55, True), item(cupcake, 450, 650, .58, False), item(rainbow, 165, 360, .58, True), item(flower, 425, 350, .56, False)], [PURPLE, YELLOW, PINK, RED, BLUE]),
]


def build_pdf(mode):
    c = canvas.Canvas(mode.output, pagesize=A4)
    c.setTitle(mode.title)
    for page, (_, items, swatch_cols) in enumerate(PAGE_DEFS, start=1):
        dense_page(c, mode, page, items, swatch_cols)
        if page < len(PAGE_DEFS):
            c.showPage()
    c.save()


def build():
    if len(PAGE_DEFS) != 50:
        raise ValueError(f"Expected 50 pages, found {len(PAGE_DEFS)}")
    build_pdf(COLOR_MODE)
    build_pdf(INK_MODE)


if __name__ == "__main__":
    build()
