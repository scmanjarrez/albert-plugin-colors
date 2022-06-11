# __init__ - Albert launcher python plugin (colors)

# Copyright (C) 2021-2022 scmanjarrez

# This file is part of albert-plugin-colors.

# albert-plugin-colors is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# albert-plugin-colors is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with GNU Emacs.  If not, see <https://www.gnu.org/licenses/>.

"""
Synopsis: <col|c> <hex|rgb>
"""
import albert
import os
import re


__title__ = "colors"
__version__ = "0.4.2"
__triggers__ = ["col ", "c "]
__authors__ = "scmanjarrez"

CWD = os.path.dirname(__file__)
ICON = f"{CWD}/icon.svg"
TEMPLATE = f"{CWD}/template_color.svg"
TMP = "/tmp/.albert_colors"
HEX = re.compile(r'#([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})', re.IGNORECASE)
RGB = re.compile(r'\(*(\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3})\)*|'
                 r'(\d{1,3})\s(\d{1,3})\s(\d{1,3})')


def initialize():
    if not os.path.isdir(TMP):
        try:
            os.mkdir(TMP)
        except OSError:
            print(f"Error creating {TMP} directory.")


def finalize():
    pass


def parse_line(line):
    col = None
    hex = True
    match = HEX.match(line)
    if match:
        col = (match.group(1), match.group(2), match.group(3))
    else:
        hex = False
        match = RGB.match(line)
        if match:
            col = (match.group(1), match.group(2), match.group(3))
            if match.group(1) is None:
                col = (match.group(4), match.group(5), match.group(6))
    if col is not None:
        if hex:
            hexcol = f"{col[0]}{col[1]}{col[2]}"
            rgbcol = (f"({int(col[0], 16)}, "
                      f"{int(col[1], 16)}, "
                      f"{int(col[2], 16)})")
        else:
            hexcol = f"{int(col[0]):02x}{int(col[1]):02x}{int(col[2]):02x}"
            rgbcol = (f"({int(col[0])}, "
                      f"{int(col[1])}, "
                      f"{int(col[2])})")
        return hexcol, rgbcol
    else:
        return col, col


def create_color_file(svg, color):
    newsvg = re.sub(r'fill:.*?;', f'fill:#{color};', svg)
    if not os.path.isfile(f"{TMP}/{color}.svg"):
        with open(f"{TMP}/{color}.svg", 'w') as cf:
            cf.write(newsvg)


def handleQuery(query):
    if not query.isTriggered:
        return

    results = []

    if not query.string:
        item = albert.Item()
        item.icon = ICON
        item.text = "Colors plugin"
        item.subtext = "Allowed formats: #rrggbb, (r,g,b) or r,g,b or r g b."
        results.append(item)
    else:
        with open(TEMPLATE, 'r') as cf:
            svg = cf.read()
        hexcol, rgbcol = parse_line(query.string)
        if hexcol is not None:
            create_color_file(svg, hexcol)
            item = albert.Item()
            item.icon = f"{TMP}/{hexcol}.svg"
            item.text = f"hex: {hexcol} | rgb: {rgbcol}"
            item.actions = [
                albert.ClipAction("Copy HEX (lower case) to clipboard",
                                  f"#{hexcol}"),
                albert.ClipAction("Copy HEX (upper case) to clipboard",
                                  f"#{hexcol.upper()}"),
                albert.ClipAction("Copy RGB to clipboard", rgbcol)
            ]
            results.append(item)
    return results
