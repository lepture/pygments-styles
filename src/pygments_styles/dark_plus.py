from pygments.style import Style
from pygments.token import (
    Comment,
    Keyword,
    Name,
    String,
    Error,
    Generic,
    Number,
    Text,
    Literal,
)


class Colors:
    # https://github.com/microsoft/vscode/blob/main/extensions/theme-defaults/themes/dark_plus.json

    foreground = "#D4D4D4"
    background = "#1E1E1E"
    highlight = "#ADD6FF26"
    comment = "#6A9955"
    error = "#f44747"

    syntax_string = "#ce9178"
    syntax_keyword = "#C586C0"
    syntax_tag = "#569cd6"
    syntax_constant = "#b5cea8"
    syntax_regex = "#d16969"
    syntax_class = "#4EC9B0"
    syntax_func = "#DCDCAA"
    syntax_label = "#C8C8C8"
    syntax_attribute = "#9cdcfe"
    syntax_pseudo = "#d7ba7d"

    diff_inserted = "#b5cea8"
    diff_deleted = "#ce9178"


class DarkPlusStyle(Style):
    name = "dark-plus"
    aliases = ["Dark Plus"]

    background_color = Colors.background
    highlight_color = Colors.highlight

    styles = {
        Text: Colors.foreground,
        Error: Colors.error,
        Comment: Colors.comment,
        Comment.Preproc: Colors.syntax_keyword,
        Comment.PreprocFile: Colors.syntax_string,
        Keyword: Colors.syntax_keyword,
        Keyword.Constant: Colors.syntax_string,
        Keyword.Pseudo: Colors.syntax_pseudo,
        Keyword.Type: Colors.syntax_tag,
        Name.Attribute: Colors.syntax_attribute,
        Name.Builtin: Colors.syntax_func,
        Name.Builtin.Pseudo: Colors.syntax_pseudo,
        Name.Class: Colors.syntax_class,
        Name.Constant: Colors.syntax_constant,
        Name.Decorator: Colors.syntax_func,
        Name.Exception: Colors.syntax_class,
        Name.Function: Colors.syntax_func,
        Name.Tag: Colors.syntax_tag,
        Name.Label: Colors.syntax_label,
        Name.Other: Colors.foreground,
        Literal: Colors.syntax_string,
        String: Colors.syntax_string,
        String.Interpol: Colors.syntax_tag,
        String.Regex: Colors.syntax_regex,
        Number: Colors.syntax_constant,
        Generic.Deleted: Colors.diff_deleted,
        Generic.Inserted: Colors.diff_inserted,
        Generic.Error: Colors.error,
        Generic.Emph: "italic",
        Generic.Strong: f"bold {Colors.syntax_tag}",
        Generic.Heading: Colors.syntax_tag,
        Generic.Subheading: Colors.syntax_tag,
        Generic.Output: Colors.syntax_string,
        Generic.Prompt: Colors.syntax_label,
        Generic.Traceback: Colors.error,
    }
