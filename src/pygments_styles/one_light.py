from pygments.style import Style
from pygments.token import (
    Comment,
    Escape,
    Keyword,
    Name,
    String,
    Literal,
    Error,
    Generic,
    Number,
    Operator,
    Text,
)


class Colors:
    foreground = "#383A42"
    background = "#FAFAFA"
    highlight = "#E5E5E6"
    comment = "#A0A1A7"
    error = "#CA1243"

    gray = "#9D9D9F"
    blue = "#4078F2"
    cyan = "#0184BC"
    green = "#50A14F"
    red = "#E45649"
    orange = "#986801"
    purple = "#A626A4"
    yellow = "#C18401"


class OneLightStyle(Style):
    """
    Pygments style based on the One Light VS Code theme.

    https://github.com/akamud/vscode-theme-onelight
    """

    name = "one-light"

    background_color = Colors.background
    highlight_color = Colors.highlight
    line_number_color = Colors.gray

    styles = {
        Text: Colors.foreground,
        # Whitespace: ,
        Escape: Colors.cyan,
        Error: Colors.error,
        # Other: ,
        Keyword: Colors.purple,
        Keyword.Constant: Colors.orange,
        # Keyword.Declaration: ,
        # Keyword.Namespace: ,
        Keyword.Pseudo: Colors.blue,
        # Keyword.Reserved: ,
        Keyword.Type: Colors.orange,
        # Name: Colors.foreground,
        Name.Attribute: Colors.orange,
        Name.Builtin: Colors.cyan,
        Name.Builtin.Pseudo: Colors.yellow,
        Name.Class: Colors.yellow,
        Name.Constant: Colors.yellow,
        Name.Decorator: Colors.cyan,
        # Name.Entity: Colors.blue,
        Name.Exception: Colors.cyan,
        Name.Function: Colors.blue,
        # Name.Function.Magic: Colors.blue,
        # Name.Property: Colors.blue,
        Name.Label: Colors.blue,
        # Name.Namespace: Colors.foreground,
        # Name.Other: Colors.yellow,
        Name.Tag: Colors.red,
        Name.Variable: Colors.red,
        # Name.Variable.Class: Colors.orange,
        # Name.Variable.Global: ,
        # Name.Variable.Instance: ,
        # Name.Variable.Magic: ,
        Literal: Colors.green,
        # Literal.Date: ,
        String: Colors.green,
        String.Affix: Colors.purple,
        String.Backtick: Colors.green,
        # String.Char: ,
        # String.Delimiter: ,
        # String.Doc: ,
        # String.Double: ,
        String.Escape: Colors.cyan,
        # String.Heredoc: ,
        String.Interpol: Colors.orange,
        # String.Other: ,
        String.Regex: Colors.red,
        # String.Single: ,
        String.Symbol: Colors.cyan,
        Number: Colors.orange,
        # Number.Bin: ,
        # Number.Float: ,
        # Number.Hex: ,
        # Number.Integer: ,
        # Number.Integer.Long: ",
        # Number.Oct: ,
        Operator: Colors.cyan,
        # Operator.Word: Colors.purple,
        # Punctuation: ,
        # Punctuation.Marker: ,
        Comment: Colors.comment,
        # Comment.Hashbang: ,
        Comment.Multiline: "italic",
        Comment.Preproc: Colors.purple,
        Comment.PreprocFile: Colors.green,
        Comment.Single: "italic",
        # Comment.Special: ,
        # Generic: ,
        Generic.Deleted: Colors.red,
        Generic.Emph: f"italic {Colors.purple}",
        Generic.Error: Colors.error,
        Generic.Heading: Colors.red,
        Generic.Inserted: Colors.green,
        Generic.Output: Colors.green,
        Generic.Prompt: Colors.gray,
        Generic.Strong: Colors.orange,
        Generic.Subheading: Colors.red,
        # Generic.EmphStrong: f"italic bold {Colors.foreground}",
        Generic.Traceback: Colors.error,
    }
