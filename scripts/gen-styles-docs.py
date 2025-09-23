import re
import os
import typing as t
import inspect
from pygments.style import Style
from pygments.styles import get_style_by_name

ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def luminance(rgb: t.Tuple[int, int, int]):
    r, g, b = [c/255.0 for c in rgb]
    def adjust(c):
        return c/12.92 if c <= 0.03928 else ((c+0.055)/1.055)**2.4
    return 0.2126*adjust(r) + 0.7152*adjust(g) + 0.0722*adjust(b)


def contrast_ratio(c1: t.Tuple[int, int, int], c2: t.Tuple[int, int, int]):
    L1, L2 = luminance(c1), luminance(c2)
    if L1 < L2:
        L1, L2 = L2, L1
    return (L1 + 0.05) / (L2 + 0.05)


def hex_to_rgb(value: str):
    value = value.lstrip("#")
    lv = len(value)
    return tuple(int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3))


def build_style_table(style: Style):
    background = hex_to_rgb(style.background_color)
    rows = []

    for token, styledef in style.styles.items():
        if styledef:
            m = re.search(r"#([0-9a-fA-F]{6})", styledef)
            if m:
                fg = hex_to_rgb(m.group(0))
                ratio = contrast_ratio(fg, background)
                result = "✅ PASS" if ratio >= 4.5 else "⚠️ FAIL"
                token_name = str(token).replace('Token.', '')
                rows.append([token_name, m.group(0), f"{ratio:.2f}", result])

    headers = ["Token Type", "Color", "Contrast", "Result"]
    # Column widths
    widths = [max(len(str(r[i])) for r in rows + [headers]) for i in range(len(headers))]

    def fmt_row(row):
        return "  ".join(str(row[i]).ljust(widths[i]) for i in range(len(headers))).strip()

    sep = "  ".join("=" * w for w in widths)

    table = []
    table.append(sep)
    table.append(fmt_row(headers))
    table.append(sep)
    for row in rows:
        table.append(fmt_row(row))
    table.append(sep)
    return "\n".join(table)


def build_doc(style_name: str):
    text = (
        ":layout: preview\n"
        f":style: {style_name}\n\n"
        f"{style_name}\n" + "=" * len(style_name) + "\n\n"
    )

    style = get_style_by_name(style_name)
    text += inspect.cleandoc(style.__doc__)
    text += (
        "\n\nAccessibility\n-------------\n\n"
        "Contrast ratio based on background: ``" + style.background_color + "``.\n\n"
    )
    text += build_style_table(style)
    text += "\n\nSamples\n-------\n\n"
    text += (
        ".. raw:: html\n"
        "    :class: samples\n"
        "    :file: ../_templates/preview.html\n"
    )
    return text


def build():
    filenames = sorted(os.listdir(os.path.join(ROOT_PATH, "src/pygments_styles")))
    for name in filenames:
        if name.endswith('.py') and not name.startswith('__'):
            style = name.replace('_', '-').replace('.py', '')
            output = os.path.join(ROOT_PATH, f'docs/styles/{style}.rst')
            with open(output, 'w') as f:
                content = build_doc(style)
                f.write(content)


if __name__ == "__main__":
    build()
