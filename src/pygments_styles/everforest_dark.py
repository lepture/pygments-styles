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

__all__ = ["EverforestDarkStyle"]


class Colors:
    # https://github.com/sainnhe/everforest-vscode/blob/master/src/palette/dark/foreground.ts
    fg = "#d3c6aa"
    red = "#e67e80"
    orange = "#e69875"
    yellow = "#dbbc7f"
    green = "#a7c080"
    aqua = "#83c092"
    blue = "#7fbbb3"
    purple = "#d699b6"
    # https://github.com/sainnhe/everforest-vscode/blob/master/src/palette/dark/background/medium.ts
    bg = "#2d353b"
    grey0 = "#7f897d"
    grey1 = "#859289"


class EverforestDarkStyle(Style):
    """
    Pygments style based on the Everforest VS Code theme.

    - https://github.com/sainnhe/everforest-vscode
    - https://github.com/sainnhe/everforest-vscode/blob/master/themes/everforest-dark.json
    """

    name = "everforest-dark"
    aliases = ["Everforest Dark"]

    background_color = Colors.bg  # editor.background
    highlight_color = "#475258b0"  # editor.hoverHighlightBackground
    line_number_color = "#7f897da0"

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
