from math import cos, radians, sin

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


OUT = "painting_enlightenment_10_pages.pdf"
W, H = A4

INK = colors.HexColor("#2f3437")
PALE = colors.HexColor("#b9c0c6")
PALE_FILL = colors.HexColor("#f7f8f8")
BLUE = colors.HexColor("#83b7e8")
YELLOW = colors.HexColor("#ffd76a")
RED = colors.HexColor("#f27a6d")
GREEN = colors.HexColor("#89c779")
ORANGE = colors.HexColor("#f7a652")
PINK = colors.HexColor("#f5a0bd")
PURPLE = colors.HexColor("#9f8fe8")
BROWN = colors.HexColor("#a97b54")


def setup(c, page):
    c.setFillColor(colors.white)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setStrokeColor(colors.HexColor("#d9dde0"))
    c.setLineWidth(1.2)
    c.roundRect(32, 34, W - 64, H - 68, 16, fill=0, stroke=1)
    c.setFillColor(colors.HexColor("#9aa1a8"))
    c.setFont("Helvetica", 9)
    c.drawCentredString(W / 2, 18, str(page))


def line_style(c, color=INK, width=5, dash=None):
    c.setStrokeColor(color)
    c.setLineWidth(width)
    c.setLineCap(1)
    c.setLineJoin(1)
    c.setDash(dash or [])


def fill_style(c, fill, stroke=INK, width=5):
    c.setFillColor(fill)
    line_style(c, stroke, width)


def guide(c, width=4):
    line_style(c, PALE, width, [3, 9])


def practice_box(c, y=78, h=185):
    c.setFillColor(PALE_FILL)
    c.setStrokeColor(colors.HexColor("#d9dde0"))
    c.setLineWidth(1.2)
    c.setDash([5, 7])
    c.roundRect(56, y, W - 112, h, 20, fill=1, stroke=1)
    c.setDash([])


def swatches(c, cols, x=412, y=724):
    for i, col in enumerate(cols):
        c.setFillColor(col)
        c.setStrokeColor(INK)
        c.setLineWidth(1.5)
        c.circle(x + i * 30, y, 10, fill=1, stroke=1)


def star(c, x, y, r=7, fill=YELLOW, stroke=INK):
    pts = []
    for i in range(10):
        rr = r if i % 2 == 0 else r * 0.45
        a = radians(-90 + i * 36)
        pts.append((x + cos(a) * rr, y + sin(a) * rr))
    p = c.beginPath()
    p.moveTo(*pts[0])
    for pt in pts[1:]:
        p.lineTo(*pt)
    p.close()
    fill_style(c, fill, stroke, 1.5)
    c.drawPath(p, fill=1, stroke=1)


def flower(c, x, y, s=1.0, pale=False, colored=True):
    col = PALE if pale else INK
    petal_fill = colors.white if pale or not colored else PINK
    center_fill = colors.white if pale or not colored else YELLOW
    stem_fill = colors.white if pale or not colored else GREEN
    if pale:
        guide(c)
    else:
        line_style(c, col, 5)
    c.line(x, y - 100 * s, x, y - 15 * s)
    fill_style(c, stem_fill, col, 4)
    c.ellipse(x - 50 * s, y - 70 * s, x - 5 * s, y - 35 * s, fill=1, stroke=1)
    c.ellipse(x + 5 * s, y - 80 * s, x + 55 * s, y - 43 * s, fill=1, stroke=1)
    fill_style(c, petal_fill, col, 4)
    for a in range(0, 360, 60):
        px = x + cos(radians(a)) * 32 * s
        py = y + sin(radians(a)) * 32 * s
        c.ellipse(px - 22 * s, py - 16 * s, px + 22 * s, py + 16 * s, fill=1, stroke=1)
    fill_style(c, center_fill, col, 4)
    c.circle(x, y, 17 * s, fill=1, stroke=1)
    c.setDash([])


def rocket(c, x, y, s=1.0, pale=False, colored=True):
    col = PALE if pale else INK
    body_fill = colors.white if pale or not colored else BLUE
    if pale:
        guide(c)
    else:
        line_style(c, col, 5)
    fill_style(c, body_fill, col, 5)
    p = c.beginPath()
    p.moveTo(x, y + 95 * s)
    p.curveTo(x - 42 * s, y + 50 * s, x - 38 * s, y - 45 * s, x, y - 78 * s)
    p.curveTo(x + 38 * s, y - 45 * s, x + 42 * s, y + 50 * s, x, y + 95 * s)
    p.close()
    c.drawPath(p, fill=1, stroke=1)
    fill_style(c, colors.white, col, 4)
    c.circle(x, y + 24 * s, 18 * s, fill=1, stroke=1)
    fill_style(c, colors.white if pale or not colored else RED, col, 4)
    c.line(x - 28 * s, y - 40 * s, x - 62 * s, y - 82 * s)
    c.line(x - 62 * s, y - 82 * s, x - 26 * s, y - 72 * s)
    c.line(x + 28 * s, y - 40 * s, x + 62 * s, y - 82 * s)
    c.line(x + 62 * s, y - 82 * s, x + 26 * s, y - 72 * s)
    fill_style(c, colors.white if pale or not colored else ORANGE, col, 4)
    c.line(x - 18 * s, y - 78 * s, x, y - 124 * s)
    c.line(x, y - 124 * s, x + 18 * s, y - 78 * s)
    c.setDash([])


def sun_cloud(c, x, y, s=1.0, pale=False):
    col = PALE if pale else INK
    fill_style(c, colors.white if pale else YELLOW, col, 5)
    if pale:
        guide(c)
    for a in range(0, 360, 30):
        c.line(x + cos(radians(a)) * 48 * s, y + sin(radians(a)) * 48 * s,
               x + cos(radians(a)) * 74 * s, y + sin(radians(a)) * 74 * s)
    c.circle(x, y, 38 * s, fill=1, stroke=1)
    fill_style(c, colors.white, col, 5)
    c.circle(x + 82 * s, y - 30 * s, 24 * s, fill=1, stroke=1)
    c.circle(x + 116 * s, y - 22 * s, 32 * s, fill=1, stroke=1)
    c.circle(x + 154 * s, y - 32 * s, 22 * s, fill=1, stroke=1)
    c.line(x + 60 * s, y - 52 * s, x + 178 * s, y - 52 * s)
    c.setDash([])


def fish(c, x, y, s=1.0, pale=False):
    col = PALE if pale else INK
    fill_style(c, colors.white if pale else ORANGE, col, 5)
    if pale:
        guide(c)
    c.ellipse(x - 78 * s, y - 42 * s, x + 78 * s, y + 42 * s, fill=1, stroke=1)
    fill_style(c, colors.white if pale else PINK, col, 5)
    p = c.beginPath()
    p.moveTo(x - 78 * s, y)
    p.lineTo(x - 132 * s, y + 48 * s)
    p.lineTo(x - 132 * s, y - 48 * s)
    p.close()
    c.drawPath(p, fill=1, stroke=1)
    fill_style(c, colors.white, col, 3)
    c.circle(x + 38 * s, y + 12 * s, 9 * s, fill=1, stroke=1)
    line_style(c, col, 3)
    c.arc(x + 42 * s, y - 24 * s, x + 68 * s, y + 2 * s, 200, 95)
    c.setDash([])


def house(c, x, y, s=1.0, pale=False):
    col = PALE if pale else INK
    fill_style(c, colors.white if pale else colors.HexColor("#f4d58d"), col, 5)
    if pale:
        guide(c)
    c.rect(x - 78 * s, y - 80 * s, 156 * s, 118 * s, fill=1, stroke=1)
    fill_style(c, colors.white if pale else RED, col, 5)
    p = c.beginPath()
    p.moveTo(x - 98 * s, y + 38 * s)
    p.lineTo(x, y + 118 * s)
    p.lineTo(x + 98 * s, y + 38 * s)
    p.close()
    c.drawPath(p, fill=1, stroke=1)
    fill_style(c, colors.white if pale else BLUE, col, 4)
    c.rect(x - 54 * s, y - 30 * s, 38 * s, 38 * s, fill=1, stroke=1)
    c.rect(x + 22 * s, y - 30 * s, 38 * s, 38 * s, fill=1, stroke=1)
    fill_style(c, colors.white if pale else BROWN, col, 4)
    c.rect(x - 20 * s, y - 80 * s, 40 * s, 62 * s, fill=1, stroke=1)
    c.setDash([])


def tree(c, x, y, s=1.0, pale=False):
    col = PALE if pale else INK
    fill_style(c, colors.white if pale else BROWN, col, 5)
    if pale:
        guide(c)
    c.roundRect(x - 22 * s, y - 112 * s, 44 * s, 105 * s, 14 * s, fill=1, stroke=1)
    fill_style(c, colors.white if pale else GREEN, col, 5)
    c.circle(x - 42 * s, y + 18 * s, 46 * s, fill=1, stroke=1)
    c.circle(x + 38 * s, y + 22 * s, 50 * s, fill=1, stroke=1)
    c.circle(x, y + 70 * s, 56 * s, fill=1, stroke=1)
    c.setDash([])


def car(c, x, y, s=1.0, pale=False):
    col = PALE if pale else INK
    fill_style(c, colors.white if pale else RED, col, 5)
    if pale:
        guide(c)
    c.roundRect(x - 116 * s, y - 40 * s, 232 * s, 68 * s, 28 * s, fill=1, stroke=1)
    p = c.beginPath()
    p.moveTo(x - 55 * s, y + 28 * s)
    p.lineTo(x - 22 * s, y + 76 * s)
    p.lineTo(x + 55 * s, y + 76 * s)
    p.lineTo(x + 88 * s, y + 28 * s)
    p.close()
    c.drawPath(p, fill=1, stroke=1)
    fill_style(c, colors.white if pale else colors.HexColor("#eef8ff"), col, 4)
    c.line(x + 16 * s, y + 72 * s, x + 16 * s, y + 32 * s)
    fill_style(c, colors.white, col, 5)
    c.circle(x - 66 * s, y - 40 * s, 22 * s, fill=1, stroke=1)
    c.circle(x + 66 * s, y - 40 * s, 22 * s, fill=1, stroke=1)
    c.setDash([])


def animal(c, x, y, s=1.0, pale=False):
    col = PALE if pale else INK
    fill_style(c, colors.white if pale else colors.HexColor("#f5c38a"), col, 5)
    if pale:
        guide(c)
    c.circle(x, y, 72 * s, fill=1, stroke=1)
    p = c.beginPath()
    p.moveTo(x - 54 * s, y + 48 * s)
    p.lineTo(x - 76 * s, y + 116 * s)
    p.lineTo(x - 18 * s, y + 76 * s)
    p.close()
    c.drawPath(p, fill=1, stroke=1)
    p = c.beginPath()
    p.moveTo(x + 54 * s, y + 48 * s)
    p.lineTo(x + 76 * s, y + 116 * s)
    p.lineTo(x + 18 * s, y + 76 * s)
    p.close()
    c.drawPath(p, fill=1, stroke=1)
    fill_style(c, colors.white, col, 3)
    c.circle(x - 28 * s, y + 18 * s, 9 * s, fill=1, stroke=1)
    c.circle(x + 28 * s, y + 18 * s, 9 * s, fill=1, stroke=1)
    fill_style(c, colors.white if pale else PINK, col, 3)
    c.circle(x, y - 12 * s, 9 * s, fill=1, stroke=1)
    line_style(c, col, 3)
    c.arc(x - 30 * s, y - 44 * s, x, y - 12 * s, 205, 120)
    c.arc(x, y - 44 * s, x + 30 * s, y - 12 * s, 215, 120)
    c.setDash([])


def rainbow(c, x, y, s=1.0, pale=False):
    col = PALE if pale else INK
    colors_arc = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]
    if pale:
        guide(c, 9)
        for r in range(130, 58, -14):
            c.arc(x - r * s, y - r * s, x + r * s, y + r * s, 0, 180)
    else:
        for i, clr in enumerate(colors_arc):
            line_style(c, clr, 11)
            r = (132 - i * 16) * s
            c.arc(x - r, y - r, x + r, y + r, 0, 180)
        line_style(c, INK, 2)
        c.arc(x - 134 * s, y - 134 * s, x + 134 * s, y + 134 * s, 0, 180)
        c.arc(x - 46 * s, y - 46 * s, x + 46 * s, y + 46 * s, 0, 180)
    c.setDash([])


def warmup_page(c):
    setup(c, 1)
    swatches(c, [RED, YELLOW, GREEN, BLUE])
    xs = [90, 185, 280, 375, 470]
    ys = [680, 590, 500, 410]
    for row, y in enumerate(ys):
        for i, x in enumerate(xs):
            guide(c, 5)
            if row == 0:
                c.line(x - 24, y, x + 24, y)
            elif row == 1:
                c.line(x, y - 24, x, y + 24)
            elif row == 2:
                c.arc(x - 28, y - 22, x + 28, y + 22, 0, 180)
            else:
                p = c.beginPath()
                p.moveTo(x - 30, y)
                p.curveTo(x - 12, y + 30, x + 10, y - 30, x + 30, y)
                c.drawPath(p, fill=0, stroke=1)
    practice_box(c, 78, 250)


def object_page(c, page, drawer, colors_for_swatches):
    setup(c, page)
    swatches(c, colors_for_swatches)
    drawer(c, W / 2, 630, 1.0, False)
    drawer(c, W / 2, 405, 0.82, True)
    practice_box(c, 70, 220)


def page10(c):
    setup(c, 10)
    swatches(c, [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE], x=382)
    rainbow(c, W / 2, 575, 0.92, False)
    rainbow(c, W / 2, 380, 0.72, True)
    practice_box(c, 62, 235)
    for x, y in [(90, 740), (505, 675), (92, 315), (505, 290)]:
        star(c, x, y, 10)


def build():
    c = canvas.Canvas(OUT, pagesize=A4)
    c.setTitle("Painting Enlightenment - 10 Pages")
    warmup_page(c)
    c.showPage()
    object_page(c, 2, rocket, [BLUE, RED, ORANGE, YELLOW])
    c.showPage()
    object_page(c, 3, flower, [PINK, YELLOW, GREEN, BLUE])
    c.showPage()
    object_page(c, 4, sun_cloud, [YELLOW, BLUE, colors.white])
    c.showPage()
    object_page(c, 5, fish, [ORANGE, PINK, BLUE])
    c.showPage()
    object_page(c, 6, house, [RED, YELLOW, BLUE, BROWN])
    c.showPage()
    object_page(c, 7, tree, [GREEN, BROWN, YELLOW])
    c.showPage()
    object_page(c, 8, car, [RED, BLUE, colors.white])
    c.showPage()
    object_page(c, 9, animal, [ORANGE, PINK, BROWN])
    c.showPage()
    page10(c)
    c.save()


if __name__ == "__main__":
    build()
