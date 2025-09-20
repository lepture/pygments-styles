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
    background = "#07090F"
    foreground = "#EEFFFF"
    highlight = "#262E47"
    comment = "#546E7A"
    error = "#FF5370"

    syntax_keyword = "#C792EA"
    syntax_operator = "#89DDFF"
    syntax_regex = "#89DDFF"
    syntax_escape = "#89DDFF"
    syntax_tag = "#f07178"
    syntax_func = "#82AAFF"
    syntax_variable = syntax_tag
    syntax_constant = "#F78C6C"
    syntax_number = syntax_constant
    syntax_string = "#C3E88D"
    syntax_class = "#FFCB6B"
    syntax_property = "#B2CCD6"
    syntax_attribute = "#FFCB6B"

    diff_inserted = "#C3E88D"
    diff_removed = "#FF5370"


class AuroraXStyle(Style):
    """
    Pygments style based on the Aurora X VS Code theme.

    https://github.com/marqu3ss/Aurora-X
    """

    name = "aurora-x"
    aliases = ["Aurora X"]

    background_color = Colors.background
    highlight_color = Colors.highlight

    styles = {
        Text: Colors.foreground,
        Error: Colors.error,
        Comment: Colors.comment,
        Comment.Single: "italic",
        Comment.Multiline: "italic",
        Comment.Preproc: Colors.syntax_operator,
        Comment.PreprocFile: Colors.syntax_string,
        Keyword: Colors.syntax_keyword,
        Keyword.Constant: Colors.syntax_constant,
        Keyword.Namespace: Colors.syntax_operator,
        Keyword.Other: Colors.syntax_operator,
        Operator: Colors.syntax_operator,
        Punctuation: Colors.syntax_operator,
        Name.Attribute: f"italic {Colors.syntax_attribute}",
        Name.Builtin: Colors.syntax_keyword,
        Name.Class: Colors.syntax_class,
        Name.Constant: Colors.syntax_constant,
        Name.Decorator: f"italic {Colors.syntax_func}",
        Name.Entity: Colors.syntax_tag,
        Name.Exception: Colors.error,
        Name.Function: Colors.syntax_func,
        Name.Label: Colors.syntax_func,
        Name.Tag: Colors.syntax_tag,
        Name.Variable: Colors.foreground,
        Literal: Colors.syntax_string,
        String: Colors.syntax_string,
        String.Escape: Colors.syntax_escape,
        String.Regex: Colors.syntax_regex,
        Number: Colors.syntax_number,
        Generic.Deleted: Colors.diff_removed,
        Generic.Inserted: Colors.diff_inserted,
        Generic.Emph: "italic",
        Generic.Strong: "bold",
        Generic.Error: Colors.error,
        Generic.Traceback: Colors.error,
        Generic.Heading: Colors.syntax_string,
        Generic.Subheading: Colors.syntax_string,
        Generic.Output: Colors.syntax_string,
        Generic.Prompt: Colors.comment,
    }
