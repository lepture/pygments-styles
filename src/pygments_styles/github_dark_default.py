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

__all__ = ["GitHubDarkDefaultStyle"]


class Colors:
    foreground = "#e6edf3"
    background = "#0d1117"
    highlight = "#3fb95040"  # editor.selectionHighlightBackground
    error = "#ffa198"

    gray = "#8b949e"
    red = "#ff7b72"
    orange = "#ffa657"
    blue = "#79c0ff"
    purple = "#d2a8ff"
    green = "#7ee787"
    aqua = "#a5d6ff"


class GitHubDarkDefaultStyle(Style):
    """
    Pygments style based on the GitHub Dark (default) VS Code theme.

    https://github.com/primer/github-vscode-theme
    """

    name = "github-dark-default"

    background_color = Colors.background
    highlight_color = Colors.highlight
    line_number_color = "#6e7681" # "editorLineNumber.foreground"

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
