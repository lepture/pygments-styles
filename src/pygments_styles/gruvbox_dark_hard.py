from pygments.style import Style
from ._gruvbox import DarkColors, build_token_styles


class GruvboxDarkHardStyle(Style):
    """
    Pygments style based on the Gruvbox Dark (hard) VS Code theme.

    https://github.com/jdinhify/vscode-theme-gruvbox
    """

    name = "gruvbox-dark-hard"

    background_color = DarkColors.bg0_h
    highlight_color = DarkColors.bg1
    line_number_color = DarkColors.gray

    styles = build_token_styles(DarkColors)
