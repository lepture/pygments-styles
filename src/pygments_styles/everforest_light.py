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
)

__all__ = ["EverforestLightStyle"]


class Colors:
    # https://github.com/sainnhe/everforest-vscode/blob/master/src/palette/light/foreground.ts
    fg = "#5c6a72"
    red = "#f85552"
    orange = "#f57d26"
    yellow = "#dfa000"
    green = "#8da101"
    aqua = "#35a77c"
    blue = "#3a94c5"
    purple = "#df69ba"
    # https://github.com/sainnhe/everforest-vscode/blob/master/src/palette/light/background/medium.ts
    bg = "#fdf6e3"
    grey0 = "#a4ad9e"
    grey1 = "#939f91"


class EverforestLightStyle(Style):
    """
    Pygments style based on the Everforest VS Code theme.

    - https://github.com/sainnhe/everforest-vscode
    - https://github.com/sainnhe/everforest-vscode/blob/master/themes/everforest-light.json
    """

    name = "everforest-light"
    aliases = ["Everforest Light"]

    background_color = Colors.bg  # editor.background
    highlight_color = "#e6e2cc90"  # editor.hoverHighlightBackground
    line_number_color = "@a4ad9ea0"

    styles = {
        Text: Colors.fg,
        Error: Colors.red,
        Comment: Colors.grey1,
        Comment.Multiline: "italic",
        Comment.Single: "italic",
        Comment.Preproc: Colors.red,
        Comment.PreprocFile: Colors.yellow,
        Keyword: Colors.red,
        Keyword.Type: Colors.blue,
        Keyword.Constant: Colors.purple,
        Keyword.Namespace: Colors.purple,
        Keyword.Declaration: Colors.orange,
        Keyword.Reserved: Colors.orange,
        Operator: Colors.orange,
        Name.Attribute: Colors.yellow,
        Name.Builtin: Colors.green,
        Name.Class: Colors.blue,
        Name.Constant: Colors.purple,
        Name.Decorator: Colors.aqua,
        Name.Function: Colors.green,
        Name.Tag: Colors.orange,
        Name.Label: Colors.aqua,
        Name.Variable.Instance: Colors.fg,
        Name.Variable.Magic: f"italic {Colors.fg}",
        String: Colors.green,
        String.Backtick: Colors.green,
        String.Doc: Colors.yellow,
        String.Double: Colors.yellow,
        String.Single: Colors.yellow,
        String.Escape: Colors.green,
        String.Interpol: Colors.fg,
        Number: Colors.purple,
        Generic.Deleted: Colors.red,
        Generic.Inserted: Colors.green,
        Generic.Emph: "italic",
        Generic.Strong: "bold",
        Generic.Heading: f"bold {Colors.red}",
        Generic.SubHeading: f"bold {Colors.orange}",
        Generic.Output: Colors.yellow,
        Generic.Prompt: Colors.grey0,
        Generic.Error: Colors.red,
        Generic.Traceback: Colors.red,
    }
