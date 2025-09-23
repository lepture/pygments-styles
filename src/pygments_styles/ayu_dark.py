# https://github.com/ayu-theme/ayu-colors

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


__all__ = ["AyuDarkStyle"]


class Colors:
    syntax_tag = "#39BAE6"
    syntax_func = "#FFB454"
    syntax_entity = "#59C2FF"
    syntax_string = "#AAD94C"
    syntax_regexp = "#95E6CB"
    syntax_doc = syntax_regexp
    syntax_markup = "#F07178"
    syntax_keyword = "#FF8F40"
    syntax_special = "#E6B673"
    syntax_comment = "#646B73"  # convert from ACB6BF8C
    syntax_constant = "#D2A6FF"
    syntax_operator = "#F29668"

    vcs_added = "#7FD962"
    vcs_modified = "#73B8FF"
    vcs_removed = "#F26D78"

    editor_foreground = "#BFBDB6"
    editor_background = "#0D1017"
    editor_gutter = "#3D424C"  #  #6C738080 on #0D1017

    accent = "#E6B450"
    error = "#D95757"


class AyuDarkStyle(Style):
    name = "ayu-dark"
    aliases = ["Ayu Dark"]

    background_color = Colors.editor_background
    highlight_color = Colors.editor_gutter
    line_number_color = "#6c738099"

    styles = {
        Text: Colors.editor_foreground,
        Error: Colors.error,
        Comment: Colors.syntax_comment,
        Comment.Multiline: "italic",
        Comment.Single: "italic",
        Comment.Preproc: Colors.syntax_keyword,
        Comment.PreprocFile: Colors.syntax_string,
        Keyword: Colors.syntax_keyword,
        Keyword.Type: Colors.syntax_entity,
        Keyword.Constant: Colors.syntax_constant,
        Keyword.Declaration: Colors.accent,
        Operator: Colors.syntax_operator,
        Name.Attribute: Colors.syntax_func,
        Name.Builtin: Colors.syntax_markup,
        Name.Class: Colors.syntax_tag,
        Name.Constant: Colors.syntax_constant,
        Name.Decorator: Colors.syntax_special,
        Name.Function: Colors.syntax_func,
        Name.Tag: Colors.syntax_tag,
        Name.Variable.Instance: Colors.accent,
        Name.Variable.Magic: f"italic {Colors.syntax_tag}",
        String: Colors.syntax_string,
        String.Backtick: Colors.syntax_operator,
        String.Char: Colors.syntax_string,
        String.Doc: f"italic {Colors.syntax_doc}",
        String.Escape: Colors.syntax_string,
        String.Regex: Colors.syntax_regexp,
        String.Symbol: Colors.syntax_string,
        Number: Colors.syntax_constant,
        Generic: Colors.editor_foreground,
        Generic.Deleted: Colors.vcs_removed,
        Generic.Inserted: Colors.vcs_added,
        Generic.Emph: f"italic {Colors.syntax_func}",
        Generic.Strong: f"bold {Colors.syntax_func}",
        Generic.Heading: f"bold {Colors.syntax_func}",
        Generic.Output: Colors.syntax_string,
        Generic.Prompt: Colors.syntax_comment,
        Generic.Error: Colors.error,
        Generic.Traceback: Colors.error,
    }
