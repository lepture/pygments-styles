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
    foreground = "#abb2bf"
    background = "#282c34"
    highlight = "#67769660"
    comment = "#7f848e"

    gray = "#5c6370"
    blue = "#61afef"
    cyan = "#56b6c2"
    green = "#98c379"
    red = "#e06c75"
    orange = "#d19a66"
    purple = "#c678dd"
    yellow = "#e5c07b"


class OneDarkProStyle(Style):
    """
    Pygments style based on the One Dark Pro VS Code theme.

    https://github.com/Binaryify/OneDark-Pro
    """

    name = "one-dark-pro"

    background_color = Colors.background
    highlight_color = Colors.highlight

    styles = {
        Text: Colors.foreground,
        # Whitespace: ,
        Escape: Colors.cyan,
        Error: Colors.red,
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
        # Name.Exception: Colors.blue,
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
        Generic.Error: Colors.red,
        Generic.Heading: Colors.red,
        Generic.Inserted: Colors.green,
        Generic.Output: Colors.green,
        Generic.Prompt: Colors.gray,
        Generic.Strong: Colors.orange,
        Generic.Subheading: Colors.red,
        # Generic.EmphStrong: f"italic bold {Colors.foreground}",
        Generic.Traceback: Colors.red,
    }
