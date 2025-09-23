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

__all__ = ["AyuMirageStyle"]


class Colors:
    # https://github.com/ayu-theme/ayu-colors
    syntax_tag = "#5CCFE6"
    syntax_func = "#FFD173"
    syntax_entity = "#73D0FF"
    syntax_string = "#D5FF80"
    syntax_regexp = "#95E6CB"
    syntax_doc = syntax_regexp
    syntax_markup = "#F28779"
    syntax_keyword = "#FFAD66"
    syntax_special = "#FFDFB3"
    syntax_comment = "#6E7C8E"  # convert from B8CFE680
    syntax_constant = "#DFBFFF"
    syntax_operator = "#F29E74"

    vcs_added = "#87D96C"
    vcs_modified = "#80BFFF"
    vcs_removed = "#F27983"

    editor_foreground = "#CCCAC2"
    editor_background = "#242936"
    editor_gutter = "#363C48"  #  #8A91992E on #242936

    accent = "#FFCC66"
    error = "#FF6666"


class AyuMirageStyle(Style):
    name = "ayu-mirage"
    aliases = ["Ayu Mirage"]

    background_color = Colors.editor_background
    highlight_color = Colors.editor_gutter
    # https://github.com/ayu-theme/vscode-ayu/blob/master/ayu-mirage.json#L98
    line_number_color = "#8a919966"

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
