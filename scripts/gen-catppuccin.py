import os
import requests

ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

url = (
    "https://raw.githubusercontent.com/catppuccin/palette/refs/heads/main/palette.json"
)

allowed_colors = [
    "rosewater",
    "pink",
    "mauve",
    "red",
    "maroon",
    "peach",
    "yellow",
    "green",
    "teal",
    "sky",
    "blue",
    "text",
    "overlay2",
    "surface1",
    "base",
]

define_imports = """from pygments.style import Style
from pygments.token import (
    Comment,
    Keyword,
    Name,
    String,
    Error,
    Generic,
    Number,
    Operator,
    Punctuation,
    Text,
    Literal,
)
"""


define_colors = """
    background_color = Colors.base
    highlight_color = Colors.surface1

    styles = {
        Text: Colors.text,
        Error: Colors.red,
        Comment: Colors.overlay2,
        Comment.Single: "italic",
        Comment.Multiline: "italic",
        Comment.Preproc: Colors.yellow,
        Comment.PreprocFile: Colors.green,
        Keyword: Colors.mauve,
        Keyword.Constant: Colors.blue,
        Operator: Colors.teal,
        Punctuation: Colors.overlay2,
        Punctuation.Marker: Colors.teal,
        Name.Attribute: Colors.yellow,
        Name.Builtin: f"italic {Colors.peach}",
        Name.Class: Colors.yellow,
        Name.Constant: Colors.blue,
        Name.Decorator: f"italic {Colors.sky}",
        Name.Function: Colors.blue,
        Name.Function.Magic: Colors.sky,
        Name.Tag: Colors.blue,
        Name.Variable: Colors.text,
        Name.Variable.Instance: Colors.rosewater,
        Literal: Colors.green,
        String: Colors.green,
        String.Backtick: Colors.green,
        String.Escape: Colors.pink,
        String.Regex: Colors.teal,
        String.Interpol: Colors.pink,
        String.Other: Colors.teal,
        Number: Colors.peach,
        Generic.Inserted: Colors.green,
        Generic.Deleted: Colors.red,
        Generic.Error: Colors.red,
        Generic.Traceback: Colors.red,
        Generic.Emph: f"italic {Colors.red}",
        Generic.Strong: f"bold {Colors.red}",
        Generic.EmphStrong: f"bold italic {Colors.red}",
        Generic.Heading: Colors.red,
        Generic.Prompt: Colors.teal,
        Generic.Output: Colors.green,
    }
"""


def build_colors(colors):
    lines = []
    for key in colors:
        if key in allowed_colors:
            conf = colors[key]
            hex_color = conf["hex"]
            lines.append(f'    {key} = "{hex_color}"')

    return "class Colors:\n" + "\n".join(lines)


def build():
    resp = requests.get(url)
    data = resp.json()
    for key in data:
        conf = data[key]
        if "colors" in conf:
            filepath = os.path.join(ROOT_PATH, f"src/vs_pygments/catppuccin_{key}.py")

            title = key.title()
            code = define_imports + "\n\n"
            code += build_colors(conf["colors"]) + "\n\n\n"
            code += f"class Catppuccin{title}Style(Style):\n"
            code += '    """\n'
            code += "    Pygments style based on the Catppuccin VS Code theme.\n\n"
            code += "    https://github.com/catppuccin/palette\n"
            code += '    """\n\n'
            code += f'    name = "catppuccin-{key}"\n'
            code += f'    aliases = ["Catppuccin {title}"]\n'
            code += define_colors
            with open(filepath, "w") as f:
                f.write(code)


if __name__ == "__main__":
    build()
