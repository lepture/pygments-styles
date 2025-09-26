from pygments.style import Style
from ._gruvbox import DarkColors, build_token_styles


class GruvboxDarkSoftStyle(Style):
    """
    Pygments style based on the Gruvbox Dark (soft) VS Code theme.

    https://github.com/jdinhify/vscode-theme-gruvbox
    """

    name = "gruvbox-dark-soft"

    background_color = DarkColors.bg0_s
    highlight_color = DarkColors.bg2
    line_number_color = DarkColors.gray

    styles = build_token_styles(DarkColors)
