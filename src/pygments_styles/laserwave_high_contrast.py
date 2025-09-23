from pygments.style import Style
from pygments.token import (
    Comment,
    # Escape,
    Keyword,
    Name,
    String,
    Literal,
    Error,
    Generic,
    Number,
    Operator,
    Punctuation,
    Text,
)

__all__ = ["LaserwaveHighContrastStyle"]


class Colors:
    maximum_blue = "#1ed3ec"
    hot_pink = "#ff52bf"
    powder_blue = "#acdfef"
    african_violet = "#d887f5"
    pearl_aqua = "#3feabf"
    old_lavender = "#b4abbe"
    roman_silver = "#b4a8c8"
    mustard = "#ffe261"
    white = "#ffffff"
    raisin_black = "#19151e"


class LaserwaveHighContrastStyle(Style):
    """
    Pygments style based on the LaserWave VS Code theme.

    https://github.com/Jaredk3nt/laserwave
    """

    name = "laserwave-high-contrast"

    background_color = Colors.raisin_black
    highlight_color = "#eb64b927"
    line_number_color = Colors.roman_silver

    styles = {
        Text: Colors.white,
        # Whitespace: ,
        # Escape: Colors.aqua,
        Error: Colors.hot_pink,
        # Other: ,
        Keyword: Colors.maximum_blue,
        Keyword.Constant: Colors.african_violet,
        Keyword.Declaration: Colors.african_violet,
        # Keyword.Namespace: ,
        # Keyword.Pseudo: ,
        # Keyword.Reserved: ,
        Keyword.Type: Colors.african_violet,
        # Name: Colors.foreground,
        Name.Attribute: Colors.hot_pink,
        Name.Builtin: Colors.mustard,
        # Name.Builtin.Pseudo: ,
        Name.Class: Colors.hot_pink,
        Name.Constant: Colors.african_violet,
        Name.Decorator: Colors.pearl_aqua,
        # Name.Entity: Colors.blue,
        # Name.Exception: Colors.blue,
        Name.Function: Colors.hot_pink,
        # Name.Function.Magic: Colors.blue,
        Name.Property: Colors.maximum_blue,
        Name.Label: Colors.african_violet,
        # Name.Namespace: Colors.foreground,
        # Name.Other: Colors.pearl_aqua,
        Name.Tag: Colors.pearl_aqua,
        # Name.Variable: Colors.foreground,
        # Name.Variable.Class: Colors.orange,
        # Name.Variable.Global: ,
        # Name.Variable.Instance: ,
        # Name.Variable.Magic: ,
        Literal: Colors.powder_blue,
        # Literal.Date: ,
        String: Colors.powder_blue,
        # String.Affix: Colors.red,
        String.Backtick: Colors.hot_pink,
        # String.Char: ,
        # String.Delimiter: ,
        # String.Doc: ,
        # String.Double: ,
        # String.Escape: ,
        # String.Heredoc: ,
        # String.Interpol: Colors.red,
        # String.Other: ,
        # String.Regex: Colors.aqua,
        # String.Single: ,
        # String.Symbol: Colors.blue,
        Number: Colors.african_violet,
        # Number.Bin: ,
        # Number.Float: ,
        # Number.Hex: ,
        # Number.Integer: ,
        # Number.Integer.Long: ",
        # Number.Oct: ,
        Operator: Colors.pearl_aqua,
        # Operator.Word: Colors.blue,
        Punctuation: Colors.roman_silver,
        # Punctuation.Marker: ,
        Comment: Colors.old_lavender,
        # Comment.Hashbang: ,
        # Comment.Multiline: ,
        Comment.Preproc: Colors.maximum_blue,
        Comment.PreprocFile: Colors.powder_blue,
        # Comment.Single: ,
        # Comment.Special: ,
        # Generic: ,
        Generic.Deleted: Colors.hot_pink,
        Generic.Emph: "italic",
        Generic.Error: Colors.hot_pink,
        Generic.Heading: f"bold {Colors.maximum_blue}",
        Generic.Inserted: Colors.pearl_aqua,
        Generic.Output: Colors.powder_blue,
        Generic.Prompt: Colors.old_lavender,
        Generic.Strong: "bold",
        Generic.Subheading: "bold",
        Generic.EmphStrong: "italic bold",
        Generic.Traceback: Colors.hot_pink,
    }
