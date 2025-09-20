from pygments.style import Style
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


class Colors:
    rosewater = "#f4dbd6"
    pink = "#f5bde6"
    mauve = "#c6a0f6"
    red = "#ed8796"
    maroon = "#ee99a0"
    peach = "#f5a97f"
    yellow = "#eed49f"
    green = "#a6da95"
    teal = "#8bd5ca"
    sky = "#91d7e3"
    blue = "#8aadf4"
    text = "#cad3f5"
    overlay2 = "#939ab7"
    surface1 = "#494d64"
    base = "#24273a"


class CatppuccinMacchiatoStyle(Style):
    """
    Pygments style based on the Catppuccin VS Code theme.

    https://github.com/catppuccin/palette
    """

    name = "catppuccin-macchiato"
    aliases = ["Catppuccin Macchiato"]

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
