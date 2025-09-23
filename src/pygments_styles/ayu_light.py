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

__all__ = ["AyuLightStyle"]


class Colors:
    # https://github.com/ayu-theme/ayu-colors
    syntax_tag = "#55B4D4"
    syntax_func = "#F2AE49"
    syntax_entity = "#399EE6"
    syntax_string = "#86B300"
    syntax_regexp = "#4CBF99"
    syntax_doc = syntax_regexp
    syntax_markup = "#F07171"
    syntax_keyword = "#FA8D3E"
    syntax_special = "#E6BA7E"
    syntax_comment = "#ADAFB2"  # convert from 787B8099
    syntax_constant = "#A37ACC"
    syntax_operator = "#ED9366"

    vcs_added = "#6CBF43"
    vcs_modified = "#478ACC"
    vcs_removed = "#FF7388"

    editor_foreground = "#3C6166"
    editor_background = "#FCFCFC"
    editor_gutter = "#E7E9EA"  #  #8A91992E on #FCFCFC

    accent = "#FFAA33"
    error = "#E65050"


class AyuLightStyle(Style):
    name = "ayu-light"
    aliases = ["Ayu Light"]

    background_color = Colors.editor_background
    highlight_color = Colors.editor_gutter

    # https://github.com/ayu-theme/vscode-ayu/blob/master/ayu-light.json#L98
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
