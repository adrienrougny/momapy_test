from momapy.rendering import render_map
from momapy.core import MapLayout, TextLayout, Map, HAlignment, VAlignment
from momapy.shapes import Rectangle
from momapy.geometry import Point
from momapy.coloring import colors

w = 150
h = 100
t = TextLayout(
    text="ABCD EFGHIJKL MNOPQRSTUVWXYZ",
    position=Point(100, 100),
    font_description="Arial 8",
    width=w,
    height=h,
    horizontal_alignment=HAlignment.RIGHT,
    vertical_alignment=VAlignment.BOTTOM,
)
b = t.ink_bbox()
r1 = Rectangle(
    position=b.position,
    width=b.width,
    height=b.height,
    stroke=colors.red,
    stroke_width=0.4,
)
r2 = Rectangle(
    position=t.position, width=w, height=h, stroke=colors.blue, stroke_width=0.4
)
l = MapLayout(
    position=Point(100, 100), width=200, height=200, layout_elements=(t, r1, r2)
)
m = Map(layout=l)
render_map(m, "textlayout.pdf")
