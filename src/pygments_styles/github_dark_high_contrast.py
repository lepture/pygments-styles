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

__all__ = ["GitHubDarkHighContrastStyle"]


class Colors:
    foreground = "#f0f3f6"
    background = "#0a0c10"
    highlight = "#26cd4d40"  # editor.selectionHighlightBackground
    error = "#ffb1af"

    gray = "#bdc4cc"
    red = "#ff9492"
    orange = "#ffb757"
    blue = "#91cbff"
    purple = "#dbb7ff"
    green = "#72f088"
    aqua = "#addcff"


class GitHubDarkHighContrastStyle(Style):
    """
    Pygments style based on the GitHub Dark (high-contrast) VS Code theme.

    https://github.com/primer/github-vscode-theme
    """

    name = "github-dark-high-contrast"

    background_color = Colors.background
    highlight_color = Colors.highlight
    line_number_color = "#9ea7b3" # "editorLineNumber.foreground"

    styles = {
        Text: Colors.foreground,
        # Whitespace: ,
        Escape: Colors.aqua,
        Error: Colors.error,
        # Other: ,
        Keyword: Colors.red,
        Keyword.Constant: Colors.blue,
        # Keyword.Declaration: ,
        # Keyword.Namespace: ,
        # Keyword.Pseudo: ,
        # Keyword.Reserved: ,
        Keyword.Type: Colors.orange,
        # Name: Colors.foreground,
        Name.Attribute: Colors.blue,
        Name.Builtin: Colors.blue,
        # Name.Builtin.Pseudo: ,
        Name.Class: Colors.orange,
        Name.Constant: Colors.blue,
        Name.Decorator: Colors.blue,
        Name.Entity: Colors.blue,
        Name.Exception: Colors.blue,
        Name.Function: Colors.purple,
        Name.Function.Magic: Colors.blue,
        Name.Property: Colors.blue,
        Name.Label: Colors.aqua,
        # Name.Namespace: Colors.foreground,
        # Name.Other: ,
        Name.Tag: Colors.green,
        # Name.Variable: Colors.foreground,
        Name.Variable.Class: Colors.orange,
        # Name.Variable.Global: ,
        # Name.Variable.Instance: ,
        # Name.Variable.Magic: ,
        Literal: Colors.aqua,
        # Literal.Date: ,
        String: Colors.aqua,
        String.Affix: Colors.red,
        String.Backtick: Colors.blue,
        # String.Char: ,
        # String.Delimiter: ,
        # String.Doc: ,
        # String.Double: ,
        # String.Escape: ,
        # String.Heredoc: ,
        String.Interpol: Colors.red,
        # String.Other: ,
        String.Regex: Colors.aqua,
        # String.Single: ,
        String.Symbol: Colors.blue,
        Number: Colors.blue,
        # Number.Bin: ,
        # Number.Float: ,
        # Number.Hex: ,
        # Number.Integer: ,
        # Number.Integer.Long: ",
        # Number.Oct: ,
        Operator: Colors.red,
        Operator.Word: Colors.blue,
        # Punctuation: ,
        # Punctuation.Marker: ,
        Comment: Colors.gray,
        # Comment.Hashbang: ,
        # Comment.Multiline: ,
        Comment.Preproc: Colors.red,
        Comment.PreprocFile: Colors.aqua,
        # Comment.Single: ,
        # Comment.Special: ,
        # Generic: ,
        Generic.Deleted: Colors.error,
        Generic.Emph: f"italic {Colors.foreground}",
        Generic.Error: Colors.error,
        Generic.Heading: f"bold {Colors.blue}",
        Generic.Inserted: Colors.green,
        Generic.Output: Colors.aqua,
        Generic.Prompt: Colors.red,
        Generic.Strong: f"bold {Colors.foreground}",
        Generic.Subheading: Colors.blue,
        Generic.EmphStrong: f"italic bold {Colors.foreground}",
        Generic.Traceback: Colors.error,
    }
