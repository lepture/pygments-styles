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
    # https://github.com/microsoft/vscode/blob/main/extensions/theme-defaults/themes/light_plus.json

    foreground = "#000000"
    background = "#FFFFFF"
    highlight = "#ADD6FF80"
    comment = "#008000"
    error = "#cd3131"

    syntax_string = "#A31515"
    syntax_number = "#098658"
    syntax_keyword = "#AF00DB"
    syntax_tag = "#800000"
    syntax_constant = "#0451A5"
    syntax_regex = "#811f3f"
    syntax_class = "#267f99"
    syntax_func = "#795E26"
    syntax_label = "#000000"
    syntax_attribute = "#E50000"
    syntax_pseudo = "#800000"

    diff_inserted = "#098658"
    diff_deleted = "#a31515"


class LightPlusStyle(Style):
    name = "light-plus"
    aliases = ["Light Plus"]

    background_color = Colors.background
    highlight_color = Colors.highlight

    styles = {
        Text: Colors.foreground,
        Error: Colors.error,
        Comment: Colors.comment,
        Comment.Preproc: Colors.syntax_keyword,
        Comment.PreprocFile: Colors.syntax_string,
        Keyword: Colors.syntax_keyword,
        Keyword.Constant: Colors.syntax_constant,
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
        Number: Colors.syntax_number,
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
