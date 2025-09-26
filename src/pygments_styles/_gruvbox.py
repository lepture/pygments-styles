from __future__ import annotations
from typing import Type
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

# https://github.com/morhetz/gruvbox


class BaseColors:
    red = "#cc241d"
    green = "#98971a"
    yellow = "#d79921"
    blue = "#458588"
    purple = "#b16286"
    aqua = "#689d6a"
    orange = "#d65d0e"
    gray = "#928374"


class DarkColors(BaseColors):
    bg = "#282828"
    fg = "#ebdbb2"
    bg0_h = "#1d2021"
    bg0_s = "#32302f"
    bg1 = "#3c3836"
    bg2 = "#504945"

    red = "#fb4934"
    green = "#b8bb26"
    yellow = "#fabd2f"
    blue = "#83a598"
    purple = "#d3869b"
    aqua = "#8ec07c"
    orange = "#fe8019"
    gray = "#a89984"


class LightColors(BaseColors):
    bg = "#fbf1c7"
    fg = "#3c3836"
    bg0_h = "#f9f5d7"
    bg0_s = "#f2e5bc"
    bg1 = "#ebdbb2"
    bg2 = "#d5c4a1"

    red = "#9d0006"
    green = "#79740e"
    yellow = "#b57614"
    blue = "#076678"
    purple = "#8f3f71"
    aqua = "#427b58"
    orange = "#af3a03"
    gray = "#7c6f64"


def build_token_styles(colors: Type[DarkColors] | Type[LightColors]):
    return {
        Text: colors.fg,
        # Whitespace: ,
        Escape: colors.red,
        Error: BaseColors.red,
        # Other: ,
        Keyword: BaseColors.red,
        Keyword.Constant: colors.purple,
        Keyword.Declaration: colors.orange,
        # Keyword.Namespace: ,
        # Keyword.Pseudo: ,
        # Keyword.Reserved: ,
        Keyword.Type: colors.yellow,
        # Name: Colors.foreground,
        Name.Attribute: colors.yellow,
        Name.Builtin: colors.orange,
        # Name.Builtin.Pseudo: ,
        Name.Class: colors.yellow,
        Name.Constant: colors.blue,
        Name.Decorator: colors.yellow,
        Name.Entity: colors.blue,
        Name.Exception: colors.blue,
        Name.Function: colors.aqua,
        # Name.Function.Magic: colors.aqua,
        Name.Property: colors.blue,
        Name.Label: BaseColors.gray,
        # Name.Namespace: ,
        # Name.Other: ,
        Name.Tag: f"bold {colors.aqua}",
        Name.Variable: colors.blue,
        # Name.Variable.Class: ,
        # Name.Variable.Global: ,
        # Name.Variable.Instance: ,
        # Name.Variable.Magic: ,
        Literal: colors.green,
        # Literal.Date: ,
        String: colors.green,
        String.Affix: BaseColors.red,
        String.Backtick: colors.aqua,
        # String.Char: ,
        # String.Delimiter: ,
        # String.Doc: ,
        # String.Double: ,
        String.Escape: colors.red,
        # String.Heredoc: ,
        String.Interpol: colors.purple,
        # String.Other: ,
        String.Regex: colors.orange,
        # String.Single: ,
        String.Symbol: colors.purple,
        Number: colors.purple,
        # Number.Bin: ,
        # Number.Float: ,
        # Number.Hex: ,
        # Number.Integer: ,
        # Number.Integer.Long: ",
        # Number.Oct: ,
        Operator: colors.aqua,
        Operator.Word: colors.aqua,
        # Punctuation: ,
        # Punctuation.Marker: ,
        Comment: BaseColors.gray,
        # Comment.Hashbang: ,
        Comment.Multiline: "italic",
        Comment.Preproc: colors.aqua,
        Comment.PreprocFile: colors.green,
        Comment.Single: "italic",
        # Comment.Special: ,
        # Generic: ,
        Generic.Deleted: BaseColors.orange,
        Generic.Emph: "italic",
        Generic.Error: colors.red,
        Generic.Heading: f"bold {colors.orange}",
        Generic.Inserted: colors.green,
        Generic.Output: colors.green,
        Generic.Prompt: colors.aqua,
        Generic.Strong: f"bold {colors.orange}",
        Generic.Subheading: colors.orange,
        Generic.EmphStrong: "italic bold",
        Generic.Traceback: colors.red,
    }
