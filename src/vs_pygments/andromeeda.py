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
    Text,
    Literal,
)


class Colors:
    foreground = "#D5CED9"
    background = "#23262E"
    highlight = "#373941"
    error = "#FC644D"
    comment = "#87888F"  # A0A1A7cc on #23262E

    cyan = "#00e8c6"
    orange = "#f39c12"
    yellow = "#FFE66D"
    pink = "#ff00aa"
    hot_pink = "#f92672"
    purple = "#c74ded"
    blue = "#7cb7ff"
    red = "#ee5d43"
    green = "#96E072"


class AndromeedaStyle(Style):
    """
    Pygments style based on the Andromeeda VS Code theme.

    https://github.com/EliverLara/Andromeda
    """

    name = "andromeeda"
    aliases = ["Andromeeda"]

    background_color = Colors.background
    highlight_color = Colors.highlight

    styles = {
        Text: Colors.foreground,
        Error: Colors.error,
        Comment: Colors.comment,
        Comment.Preproc: Colors.purple,
        Comment.PreprocFile: Colors.green,
        Keyword: Colors.purple,
        Operator: Colors.red,
        Name: Colors.cyan,
        Name.Attribute: Colors.orange,
        Name.Builtin: Colors.yellow,
        Name.Class: Colors.yellow,
        Name.Constant: Colors.orange,
        Name.Decorator: Colors.yellow,
        Name.Entity: Colors.orange,
        Name.Exception: Colors.orange,
        Name.Function: Colors.yellow,
        Name.Tag: Colors.hot_pink,
        Name.Variable: Colors.cyan,
        Name.Other: Colors.foreground,
        Literal: Colors.green,
        String: Colors.green,
        String.Interpol: Colors.red,
        String.Regex: Colors.blue,
        Number: Colors.orange,
        Generic.Deleted: Colors.red,
        Generic.Inserted: Colors.green,
        Generic.Error: Colors.error,
        Generic.Emph: "italic",
        Generic.Strong: "bold",
        Generic.Heading: Colors.hot_pink,
        Generic.Subheading: Colors.pink,
        Generic.Output: Colors.green,
        Generic.Prompt: Colors.comment,
        Generic.Traceback: Colors.error,
    }
