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
    Text,
)

__all__ = ["PlasticStyle"]


class Colors:
    sunglo = "#E06C75"
    fountain_blue = "#56B6C2"
    cornflower_blue = "#61AFEF"
    olivine = "#98C379"
    whiskey = "#D19A66"
    harvest_gold = "#E5C07B"
    lavender = "#B57EDC"
    shuttle_gray = "#5F6672"
    cadet_blue = "#A9B2C3"
    ghost = "#C6CCD7"

    woodsmoke = "#181A1F"
    valencia = "#D74E42"


class PlasticStyle(Style):
    """
    Pygments style based on the Plastic VS Code theme.

    https://github.com/will-stone/plastic
    """

    name = "plastic"

    background_color = Colors.woodsmoke
    highlight_color = "#A9B2C333"
    line_number_color = Colors.shuttle_gray

    styles = {
        Text: Colors.cadet_blue,
        # Whitespace: ,
        # Escape: Colors.aqua,
        Error: Colors.valencia,
        # Other: ,
        Keyword: Colors.sunglo,
        Keyword.Constant: Colors.fountain_blue,
        Keyword.Declaration: Colors.cornflower_blue,
        # Keyword.Namespace: ,
        # Keyword.Pseudo: ,
        # Keyword.Reserved: ,
        Keyword.Type: Colors.cornflower_blue,
        # Name: Colors.foreground,
        Name.Attribute: Colors.whiskey,
        Name.Builtin: Colors.harvest_gold,
        # Name.Builtin.Pseudo: ,
        Name.Class: Colors.harvest_gold,
        Name.Constant: Colors.fountain_blue,
        Name.Decorator: Colors.harvest_gold,
        # Name.Entity: Colors.blue,
        Name.Exception: Colors.harvest_gold,
        Name.Function: Colors.lavender,
        # Name.Function.Magic: Colors.blue,
        # Name.Property: Colors.blue,
        Name.Label: Colors.olivine,
        # Name.Namespace: Colors.foreground,
        # Name.Other: ,
        Name.Tag: Colors.harvest_gold,
        # Name.Variable: Colors.foreground,
        # Name.Variable.Class: Colors.orange,
        # Name.Variable.Global: ,
        # Name.Variable.Instance: ,
        # Name.Variable.Magic: ,
        Literal: Colors.olivine,
        # Literal.Date: ,
        String: Colors.olivine,
        String.Affix: Colors.cornflower_blue,
        # String.Backtick: Colors.blue,
        # String.Char: ,
        # String.Delimiter: ,
        # String.Doc: ,
        # String.Double: ,
        # String.Escape: ,
        # String.Heredoc: ,
        String.Interpol: Colors.fountain_blue,
        # String.Other: ,
        # String.Regex: Colors.aqua,
        # String.Single: ,
        String.Symbol: Colors.fountain_blue,
        Number: Colors.fountain_blue,
        # Number.Bin: ,
        # Number.Float: ,
        # Number.Hex: ,
        # Number.Integer: ,
        # Number.Integer.Long: ",
        # Number.Oct: ,
        Operator: Colors.sunglo,
        # Operator.Word: Colors.blue,
        # Punctuation: ,
        # Punctuation.Marker: ,
        Comment: Colors.shuttle_gray,
        # Comment.Hashbang: ,
        # Comment.Multiline: ,
        Comment.Preproc: Colors.sunglo,
        Comment.PreprocFile: Colors.olivine,
        # Comment.Single: ,
        # Comment.Special: ,
        # Generic: ,
        Generic.Deleted: Colors.sunglo,
        Generic.Emph: "italic",
        Generic.Error: Colors.sunglo,
        # Generic.Heading: ,
        Generic.Inserted: Colors.olivine,
        Generic.Output: Colors.olivine,
        Generic.Prompt: Colors.sunglo,
        Generic.Strong: "bold",
        # Generic.Subheading: ,
        Generic.EmphStrong: "italic bold",
        Generic.Traceback: Colors.sunglo,
    }
