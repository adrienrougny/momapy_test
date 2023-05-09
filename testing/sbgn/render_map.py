#!python

import sys

import momapy.sbgn.io
import momapy.rendering
import momapy.rendering.skia
import momapy.coloring
import momapy.sbgn.styling

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if len(sys.argv) > 3:
        style_sheets = sys.argv[3].split(",")
        style_sheets = [
            getattr(momapy.sbgn.styling, style_sheet.strip(" "))
            for style_sheet in style_sheets
        ]
    else:
        style_sheets = None

    m = momapy.sbgn.io.read_file(
        input_file,
        return_builder=True,
        style_sheet=style_sheets,
        tidy=True,
    )
    momapy.rendering.render_map(m, output_file, format_="pdf", renderer="skia")
