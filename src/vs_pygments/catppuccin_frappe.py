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
    rosewater = "#f2d5cf"
    pink = "#f4b8e4"
    mauve = "#ca9ee6"
    red = "#e78284"
    maroon = "#ea999c"
    peach = "#ef9f76"
    yellow = "#e5c890"
    green = "#a6d189"
    teal = "#81c8be"
    sky = "#99d1db"
    blue = "#8caaee"
    text = "#c6d0f5"
    overlay2 = "#949cbb"
    surface1 = "#51576d"
    base = "#303446"


class CatppuccinFrappeStyle(Style):
    """
    Pygments style based on the Catppuccin VS Code theme.

    https://github.com/catppuccin/palette
    """

    name = "catppuccin-frappe"
    aliases = ["Catppuccin Frappe"]

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
